import time
import curses
import math
import json
import subprocess
import os
from curses import wrapper
from os.path import commonprefix, exists, isdir
from os import sep
import glob
import re
import sys
import contextlib

# local
from . import config
from . import command
from . import popularity


class Notification:
    """Simple notification system for displaying messages"""
    
    @staticmethod
    def show(stdscr, message, duration=0.5):
        """
        Show a notification message for a specified duration
        """
        import time
        start_time = time.time()
        
        # Get terminal dimensions
        max_y, max_x = stdscr.getmaxyx()
        
        # Calculate notification position (top right)
        notification_width = len(message) + 4
        notification_x = max_x - notification_width - 2
        notification_y = 1
        
        # Create notification window
        notification_win = curses.newwin(3, notification_width, notification_y, notification_x)
        notification_win.border()
        notification_win.addstr(1, 2, message)
        notification_win.refresh()
        
        # Wait for duration
        while time.time() - start_time < duration:
            stdscr.refresh()
            time.sleep(0.1)
        
        # Clear notification
        notification_win.clear()
        notification_win.refresh()
        del notification_win

    @staticmethod
    def show_instant(stdscr, message):
        """
        Show a notification message instantly (for use in argument menu)
        """
        # Get terminal dimensions
        max_y, max_x = stdscr.getmaxyx()
        
        # Calculate notification position (top right)
        notification_width = len(message) + 4
        notification_x = max_x - notification_width - 2
        notification_y = 1
        
        # Create notification window
        notification_win = curses.newwin(3, notification_width, notification_y, notification_x)
        notification_win.border()
        notification_win.addstr(1, 2, message)
        notification_win.refresh()


def detect_current_terminal():
    """
    Detect the current terminal being used and return the appropriate command to open a new window
    """
    import os
    import subprocess
    
    # Check for macOS terminals first
    if os.environ.get('TERM_PROGRAM') == 'iTerm.app':
        return ['osascript', '-e', 'tell application "iTerm" to create window with default profile command "{cmd}"']
    elif os.environ.get('TERM_PROGRAM') == 'Apple_Terminal':
        return ['osascript', '-e', 'tell application "Terminal" to do script "{cmd}"']
    
    # Check for kitty terminal
    if os.environ.get('TERM') == 'xterm-kitty':
        return ['kitty', 'new-window', '--new-tab', '--', 'bash', '-c', '{cmd}']
    
    # Check for Konsole (KDE) - most reliable detection
    if os.environ.get('KONSOLE_DBUS_SERVICE') or os.environ.get('KONSOLE_DBUS_WINDOW'):
        return ['konsole', '-e', 'bash', '-c', '{cmd}']
    
    # Check for gnome-terminal
    if os.environ.get('GNOME_TERMINAL_SERVICE') or os.environ.get('GNOME_TERMINAL_SCREEN'):
        return ['gnome-terminal', '--', 'bash', '-c', '{cmd}']
    
    # Check for xfce4-terminal
    if os.environ.get('TERM') == 'xterm-256color' and os.path.exists('/usr/bin/xfce4-terminal'):
        return ['xfce4-terminal', '-e', 'bash', '-c', '{cmd}']
    
    # Check for mate-terminal
    if os.environ.get('TERM') == 'xterm-256color' and os.path.exists('/usr/bin/mate-terminal'):
        return ['mate-terminal', '-e', 'bash', '-c', '{cmd}']
    
    # Check for lxterminal
    if os.environ.get('TERM') == 'xterm-256color' and os.path.exists('/usr/bin/lxterminal'):
        return ['lxterminal', '-e', 'bash', '-c', '{cmd}']
    
    # Check for termite
    if os.environ.get('TERM') == 'xterm-termite':
        return ['termite', '-e', 'bash', '-c', '{cmd}']
    
    # Check for alacritty
    if os.environ.get('TERM') == 'alacritty':
        return ['alacritty', '-e', 'bash', '-c', '{cmd}']
    
    # Check for st (suckless terminal)
    if os.environ.get('TERM') == 'st-256color':
        return ['st', '-e', 'bash', '-c', '{cmd}']
    
    # Check for urxvt
    if os.environ.get('TERM') == 'rxvt-unicode-256color':
        return ['urxvt', '-e', 'bash', '-c', '{cmd}']
    
    # Check for xterm
    if os.environ.get('TERM') == 'xterm' or os.environ.get('TERM') == 'xterm-256color':
        # Try to detect which terminal is actually running
        try:
            # Check if we're in a Konsole session by checking parent process (most reliable)
            try:
                ppid = os.getppid()
                with open(f'/proc/{ppid}/comm', 'r') as f:
                    parent_comm = f.read().strip()
                    if parent_comm == 'konsole':
                        return ['konsole', '-e', 'bash', '-c', '{cmd}']
            except:
                pass
            
            # Check if we're in a Konsole session via environment
            if os.path.exists('/proc/self/environ'):
                try:
                    with open('/proc/self/environ', 'rb') as f:
                        environ_data = f.read().decode('utf-8', errors='ignore')
                        if 'KONSOLE' in environ_data:
                            return ['konsole', '-e', 'bash', '-c', '{cmd}']
                except:
                    pass
            
            # Check if we're in a gnome-terminal session (avoid X11 calls that cause QObject errors)
            if os.environ.get('WINDOWID'):
                try:
                    # Use a more reliable method that doesn't trigger QObject errors
                    result = subprocess.run(['xprop', '-id', os.environ.get('WINDOWID'), 'WM_CLASS'], 
                                          capture_output=True, text=True, timeout=2)
                    if result.returncode == 0 and 'gnome-terminal' in result.stdout.lower():
                        return ['gnome-terminal', '--', 'bash', '-c', '{cmd}']
                except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
                    # Silently ignore X11-related errors
                    pass
                
        except Exception:
            # Silently ignore any detection errors
            pass
    
    # Fallback: try common terminals in order of preference
    terminals = [
        ('konsole', ['konsole', '-e', 'bash', '-c', '{cmd}']),
        ('gnome-terminal', ['gnome-terminal', '--', 'bash', '-c', '{cmd}']),
        ('xfce4-terminal', ['xfce4-terminal', '-e', 'bash', '-c', '{cmd}']),
        ('mate-terminal', ['mate-terminal', '-e', 'bash', '-c', '{cmd}']),
        ('lxterminal', ['lxterminal', '-e', 'bash', '-c', '{cmd}']),
        ('xterm', ['xterm', '-e', 'bash', '-c', '{cmd}']),
    ]
    
    for term_name, term_cmd in terminals:
        if os.path.exists(f'/usr/bin/{term_name}'):
            return term_cmd
    
    # Final fallback
    return ['x-terminal-emulator', '-e', 'bash', '-c', '{cmd}']


def open_in_new_terminal(cmdline):
    """
    Open a command in a new terminal window using the detected terminal
    """
    import subprocess
    try:
        terminal_cmd = detect_current_terminal()
        # Replace {cmd} placeholder with actual command
        if '{cmd}' in str(terminal_cmd):
            terminal_cmd = [part.replace('{cmd}', cmdline) for part in terminal_cmd]
        else:
            # For commands that don't use the {cmd} placeholder
            terminal_cmd.append(cmdline)
        # Suppress all output from the subprocess
        subprocess.Popen(terminal_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception as e:
        return False


class CheatslistMenu:
    globalcheats = []  # all cheats
    cheats = []  # cheats after search
    max_visible_cheats = 0
    input_buffer = ''
    position = 0
    page_position = 0
    ctrl_enter_pressed = False  # Flag to track Ctrl+Enter

    xcursor = None
    x_init = None
    y_init = None
    notification_message = None
    notification_time = 0
    show_clipboard_notification = False  # <-- Add this flag
    
    # Popularity manager for sorting commands
    popularity_manager = None

    @staticmethod
    def draw_prompt():
        """
        Create a prompt box
        at x : 0 / y : 5
        size 5 chars
        :return: the windows created
        """
        y, x = 5, 0
        ncols, nlines = 5, 1
        promptwin = curses.newwin(nlines, ncols, y, x)
        try:
            promptwin.addstr("\u2620  >", curses.color_pair(Gui.BASIC_COLOR))
        except:
            promptwin.addstr(">>>>", curses.color_pair(Gui.BASIC_COLOR))
        promptwin.refresh()
        return promptwin

    def draw_infobox(self):
        """
        Draw the top infobox (4 lines / width from param)
        :return: the window created
        """
        y, x = 0, 0
        ncols, nlines = self.width, 4
        infowin = curses.newwin(nlines, ncols, y, x)
        selected_cheat = self.selected_cheat()
        if selected_cheat is not None:
            infowin.addstr(y + 1, x + 2, Gui.draw_string(selected_cheat.name, self.width - 3),
                           curses.color_pair(Gui.INFO_NAME_COLOR))
            # infowin.addstr(y + 2, x + 2, Gui.draw_string(selected_cheat.description.split('\n')[0], self.width - 3),
            #                curses.color_pair(Gui.INFO_DESC_COLOR))
            infowin.addstr(y + 2, x + 2, Gui.draw_string(selected_cheat.printable_command, self.width - 3),
                           curses.color_pair(Gui.INFO_CMD_COLOR))
        infowin.border()
        infowin.refresh()
        return infowin

    def draw_editbox(self):
        """
        Draw the edition box (in the right of the prompt box
        """
        y, x = 5, 6
        ncols, nlines = self.width - 5, 1
        editwin = curses.newwin(nlines, ncols, y, x)
        editwin.addstr(self.input_buffer, curses.color_pair(Gui.BASIC_COLOR))
        editwin.refresh()
        return editwin

    @staticmethod
    def draw_cheat(win, cheat, selected):
        """
        Draw a cheat line in the cheats list menu
        :param win:
        :param cheat:
        :param selected:
        """
        win_height, win_width = win.getmaxyx()
        prompt = '> '
        max_width = win_width - len(prompt) - 1  # Leave space for newline

        title = cheat.tags if cheat.tags != '' else cheat.str_title

        tags = cheat.get_tags()

        columns_list = ["title", "name", "description"]
        if Gui.with_tags:
            columns_list = ["tags"] + columns_list

        def get_col_size(max_width, ratio):
            """
            Return the column size from the given ratio

            :param max_width: The width maximal of the screen
            :param ratio: The ratio of the column
            """
            return math.floor((max_width * ratio) / 100)

        ratios = Gui.get_ratios_for_column(columns_list)

        # Patch: For set commands, show the current value instead of <value>
        desc = cheat.printable_command
        import re
        m = re.match(r'>set <([^>]+)>=<value>', desc.strip(), re.IGNORECASE)
        if m:
            varname = m.group(1).lower()
            if varname != 'variable':
                current_val = Gui.armouryGlobalVars.get(f'<{varname}>', '')
                desc = f'>set <{varname}>={current_val}'

        columns = {"tags": {"width": get_col_size(max_width, ratios.get("tags", 0)),
                            "val": tags,
                            "color": Gui.COL4_COLOR_SELECT if selected else Gui.COL4_COLOR},
                   "title": {"width": get_col_size(max_width, ratios.get("title", 0)),
                             "val": cheat.str_title,
                             "color": Gui.COL3_COLOR_SELECT if selected else Gui.COL1_COLOR},
                   "name": {"width": get_col_size(max_width, ratios.get("name", 0)),
                            "val": cheat.name,
                            "color": Gui.COL2_COLOR_SELECT if selected else Gui.COL2_COLOR},
                   "description": {"width": get_col_size(max_width, ratios.get("description", 0)),
                                   "val": desc,
                                   "color": Gui.COL3_COLOR_SELECT if selected else Gui.COL3_COLOR}}

        # Check if we have enough space
        if max_width <= 0:
            return

        try:
            if selected:
                win.addstr(prompt, curses.color_pair(Gui.CURSOR_COLOR_SELECT))
            else:
                win.addstr(' ' * len(prompt), curses.color_pair(Gui.BASIC_COLOR))

            for column_name in columns_list:
                win.addstr("{:{}s}".format(Gui.draw_string(columns[column_name]["val"],
                                                           columns[column_name]["width"]),
                                           columns[column_name]["width"]),
                           curses.color_pair(columns[column_name]["color"]))
            win.addstr("\n")
        except curses.error:
            # If we can't fit the content, just skip this line
            pass

    def draw_cheatslistbox(self):
        """
        Draw the box to show the cheats list
        """
        y, x = 6, 0
        ncols, nlines = self.width, self.height - 6
        
        # Ensure we have valid dimensions
        if nlines <= 0:
            nlines = 1
        if ncols <= 0:
            ncols = 1
            
        listwin = curses.newwin(nlines, ncols, y, x)

        visible_cheats = self.cheats[self.page_position:self.max_visible_cheats + self.page_position]
        counter = self.page_position

        for cheat in visible_cheats:
            self.draw_cheat(listwin, cheat, counter == self.position)
            counter += 1

        listwin.refresh()

    def draw_footbox(self, info):
        """
        Draw the footer (number infos)
        :param info: str info to draw
        """
        y, x = self.height - 1, 0
        ncols, nlines = self.width, 1

        # print nb cmd info (bottom left)
        nbinfowin = curses.newwin(nlines, ncols, y, x)
        nbinfowin.addstr(info, curses.color_pair(Gui.BASIC_COLOR))
        
        # Add Ctrl+Enter help text (more compact)
        help_text = " Enter:Copy | Space:Terminal "
        help_text_len = len(help_text)
        
        # If terminal is too small, use even more compact text
        if help_text_len >= ncols - 20:
            help_text = " Enter:Copy | Space:Term "
            help_text_len = len(help_text)
        
        # Make sure there's room for the help text and filename
        if help_text_len < ncols - 20:  # Leave space for filename
            try:
                nbinfowin.addstr(y, ncols - help_text_len, help_text, curses.color_pair(Gui.BASIC_COLOR))
            except curses.error:
                # If we can't fit it, don't show it
                pass
        
        nbinfowin.refresh()

        # print cheatsheet filename (bottom right)
        if self.selected_cheat() is not None:
            cheat_file = self.selected_cheat().filename

            # protection in case screen to small or name too long        
            if len(cheat_file) > self.width - 16:
                cheat_file = cheat_file[0:self.width - 17] + ".."

            fileinfowin = curses.newwin(nlines, ncols, y, self.width - (len(cheat_file) + 3))
            fileinfowin.addstr(cheat_file, curses.color_pair(Gui.BASIC_COLOR))
            fileinfowin.refresh()

    def match(self, cheat):
        """
        Function called by the iterator to verify if the cheatsheet match the entered values
        :param cheat: cheat to check
        :return: boolean
        """
        # if search begin with '>' print only internal CMD
        if self.input_buffer.startswith('>') and not cheat.command.startswith('>'):
            return False

        for value in self.input_buffer.lower().split(' '):
            is_value_excluded = False
            if value.startswith("!") and len(value) > 1:
                value = value[1:]
                is_value_excluded = True

            if (value in cheat.str_title.lower()
                    or value in cheat.name.lower()
                    or value in cheat.tags.lower()
                    or value in "".join(cheat.command_tags.values()).lower()
                    or value in cheat.command.lower()):
                if is_value_excluded:
                    return False

            elif not is_value_excluded:
                return False
        return True

    def get_all_arg_tags(self):
        tags = set()
        for cheat in self.globalcheats:
            for match in re.findall(r'<([^ <>]+)>', cheat.command):
                tags.add(match)
        return sorted(tags, key=lambda x: x.lower())

    def search(self):
        """
        Return the list of cheatsheet who match the searched term
        :return: list of cheatsheet to show
        """
        if self.input_buffer != '':
            list_cheat = list(filter(self.match, self.globalcheats))
        else:
            list_cheat = self.globalcheats
        
        # Sort cheats by popularity and usage if popularity manager is available
        if self.popularity_manager:
            list_cheat = self.popularity_manager.sort_cheats_by_popularity_and_usage(list_cheat)
        
        return list_cheat

    def selected_cheat(self):
        """
        Return the selected cheat in the list
        :return: selected cheat
        """
        if len(self.cheats) == 0:
            return None
        return self.cheats[self.position % len(self.cheats)]

    def draw(self, stdscr):
        """
        Draw the main menu to select a cheatsheet
        :param stdscr: screen
        """
        self.height, self.width = stdscr.getmaxyx()
        self.max_visible_cheats = max(1, self.height - 7)  # Ensure at least 1 visible cheat
        # create prompt windows
        self.draw_prompt()
        # create info windows
        self.draw_infobox()
        # create cheatslist box
        self.draw_cheatslistbox()
        # draw footer
        info = "> %d / %d " % (self.position + 1, len(self.cheats))
        self.draw_footbox(info)
        # create edit windows
        self.draw_editbox()
        # init cursor position (if first draw)
        if self.x_init is None or self.y_init is None or self.xcursor is None:
            self.y_init, self.x_init = curses.getsyx()
            self.xcursor = self.x_init
        # set cursor position
        curses.setsyx(self.y_init, self.xcursor)
        curses.doupdate()

    def move_position(self, step):
        """
        :param step:
        """
        # SCROLL ?
        #
        # 0                                ---------      
        # 1                                |       |
        # 2                       ->   -----------------    <-- self.page_position
        # 3                      |     |   |       |   |       
        # 4 max_visible_cheats = |     |   |       |   |
        # 5                      |     |  >|xxxxxxx|   |    <-- self.position      
        # 6                      |     |   |       |   |       
        # 7                       ->   -----------------    <-- self.page_position+max_visible_cheats
        # 8                                |       |
        # 9                                ---------        <-- len(self.cheats)
        self.position += step

        # clean position
        if self.position < 0: self.position = 0
        if self.position >= len(self.cheats) - 1: self.position = len(self.cheats) - 1

        # move page view UP
        if self.page_position > self.position:
            self.page_position -= (self.page_position - self.position)

            # move page view DOWN
        if self.position >= (self.page_position + self.max_visible_cheats):
            self.page_position += 1 + (self.position - (self.page_position + self.max_visible_cheats))

    def move_page(self, step):
        """
        :param step:
        """
        # only move if it is possible
        if len(self.cheats) > self.max_visible_cheats:
            new_pos = self.page_position + step * self.max_visible_cheats
            # clean position
            if new_pos >= (len(self.cheats) + 1 - self.max_visible_cheats):
                self.position = len(self.cheats) - 1
                self.page_position = len(self.cheats) - self.max_visible_cheats
            elif new_pos < 0:
                self.position = self.page_position = 0
            else:
                self.position = self.page_position = new_pos

    def check_move_cursor(self, n):
        return self.x_init <= (self.xcursor + n) < self.x_init + len(self.input_buffer) + 1

    def run(self, stdscr):
        """
        Cheats selection menu processing..
        :param stdscr: screen
        """
        # init
        Gui.init_colors()
        stdscr.clear()
        self.height, self.width = stdscr.getmaxyx()
        self.max_visible_cheats = self.height - 7
        self.cursorpos = 0

        # (Reverted) No startup notification here

        while True:
            stdscr.refresh()
            self.cheats = self.search()
            self.draw(stdscr)
            # Notification loop: if notification_message is set, show it for 1 second, then clear and continue
            import time as _time
            if self.notification_message:
                notif_start = _time.time()
                # Create notification window once
                notif = self.notification_message
                notif_len = len(notif)
                y_pos = 0
                x_pos = max(0, self.width - notif_len - 2)
                notif_win = curses.newwin(1, notif_len + 2, y_pos, x_pos)
                notif_win.bkgd(' ', curses.color_pair(15))
                notif_win.addstr(0, 1, notif, curses.color_pair(15))
                notif_win.refresh()
                
                # Wait for duration without redrawing the entire screen
                while _time.time() - notif_start < 1.0:
                    _time.sleep(0.1)  # Reduced frequency from 0.05 to 0.1
                
                # Clear notification window
                notif_win.clear()
                notif_win.refresh()
                del notif_win
                
                self.notification_message = None
                self.notification_time = 0
                continue  # Redraw menu after notification
            c = stdscr.getch()
            if c == curses.KEY_ENTER or c == 10 or c == 13:  # Enter key
                self.ctrl_enter_pressed = False
                selected = self.selected_cheat()
                if selected is not None:
                    # Create command object to check if it has arguments
                    Gui.cmd = command.Command(selected, Gui.armouryGlobalVars)
                    
                    # Special handling for internal commands that don't need arguments
                    if selected.command.strip() in ['>exit', '>clear']:
                        if selected.command.strip() == '>clear':
                            Gui.armouryGlobalVars.clear()
                            with open(Gui.savefile, 'w') as f:
                                json.dump(Gui.armouryGlobalVars, f)
                            self.notification_message = "All global variables cleared."
                            import time as _time
                            self.notification_time = _time.time()
                            continue
                        elif selected.command.strip() == '>exit':
                            break
                    
                    # Handle commands with no arguments directly (copy to clipboard)
                    if Gui.cmd.nb_args == 0:
                        # Track usage for non-internal commands
                        if not selected.command.startswith('>') and self.popularity_manager:
                            self.popularity_manager.increment_usage(selected)
                        
                        # Copy command to clipboard
                        try:
                            clipboard_copy(Gui.cmd.cmdline)
                            self.notification_message = "Copied to clipboard."
                            import time as _time
                            self.notification_time = _time.time()
                        except ImportError:
                            self.notification_message = "pyperclip not available."
                            import time as _time
                            self.notification_time = _time.time()
                        continue
                    
                    # For commands with arguments, go through argument menu
                    args_menu = ArgslistMenu(self)
                    args_menu.run(stdscr)
                    # After user input, handle >set commands
                    if selected.command.strip().startswith('>set'):
                        import re
                        m = re.match(r'>set <([^>]+)>=<value>', selected.command.strip(), re.IGNORECASE)
                        if m and m.group(1).lower() == 'variable':
                            # Generic set: get variable and value from args
                            var_name, var_val = Gui.cmd.args[0][1], Gui.cmd.args[1][1]
                            if var_name and var_val:
                                Gui.armouryGlobalVars[f'<{var_name}>'] = var_val
                                with open(Gui.savefile, 'w') as f:
                                    json.dump(Gui.armouryGlobalVars, f)
                                self.notification_message = f"Set <{var_name}> = {var_val}"
                                import time as _time
                                self.notification_time = _time.time()
                            continue
                        elif m:
                            # Specific set: get variable from args
                            arg_name, arg_val = Gui.cmd.args[0]
                            if arg_val:
                                Gui.armouryGlobalVars[f'<{arg_name}>'] = arg_val
                                with open(Gui.savefile, 'w') as f:
                                    json.dump(Gui.armouryGlobalVars, f)
                                self.notification_message = f"Set <{arg_name}> = {arg_val}"
                                import time as _time
                                self.notification_time = _time.time()
                            continue
                    stdscr.refresh()
                    break
            elif c == curses.KEY_F2:  # F2 key for opening in new terminal
                self.ctrl_enter_pressed = True  # Set flag for new terminal
                if self.selected_cheat() is not None:
                    # Create command object to check if it has arguments
                    Gui.cmd = command.Command(self.selected_cheat(), Gui.armouryGlobalVars)
                    # Do nothing if internal/global command (starts with '>')
                    if Gui.cmd.cmdline.strip().startswith('>'):
                        continue
                    # Handle commands with no arguments directly (open in new terminal)
                    if Gui.cmd.nb_args == 0:
                        # Track usage for non-internal commands
                        if not selected.command.startswith('>') and self.popularity_manager:
                            self.popularity_manager.increment_usage(selected)
                        
                        # Open command in new terminal
                        try:
                            if open_in_new_terminal(Gui.cmd.cmdline):
                                self.notification_message = "Opened in new terminal."
                            else:
                                self.notification_message = "Failed to open terminal."
                            import time as _time
                            self.notification_time = _time.time()
                        except Exception as e:
                            self.notification_message = f"Failed to open terminal: {str(e)}"
                            import time as _time
                            self.notification_time = _time.time()
                        continue
                    # For commands with arguments, go through argument menu
                    args_menu = ArgslistMenu(self)
                    args_menu.run(stdscr)
                    stdscr.refresh()
                    break
            elif c == curses.KEY_F10 or c == 27:
                Gui.cmd = None
                break  # Exit the while loop
            elif c == 339 or c == curses.KEY_PPAGE:
                # Page UP
                self.move_page(-1)
            elif c == 338 or c == curses.KEY_NPAGE:
                # Page DOWN
                self.move_page(1)
            elif c == curses.KEY_UP:
                # Move UP
                self.move_position(-1)
            elif c == curses.KEY_DOWN:
                # Move DOWN
                self.move_position(1)
            elif c == curses.KEY_BACKSPACE or c == 127 or c == 8:
                if self.check_move_cursor(-1):
                    i = self.xcursor - self.x_init - 1
                    self.input_buffer = self.input_buffer[:i] + self.input_buffer[i + 1:]
                    self.xcursor -= 1
                    # new search -> reset position
                    self.position = 0
                    self.page_position = 0
            elif c == curses.KEY_DC or c == 127:
                if self.check_move_cursor(1):
                    i = self.xcursor - self.x_init - 1
                    self.input_buffer = self.input_buffer[:i + 1] + self.input_buffer[i + 2:]
                    # new search -> reset position
                    self.position = 0
                    self.page_position = 0
            elif c == curses.KEY_LEFT:
                # Move cursor LEFT
                if self.check_move_cursor(-1): self.xcursor -= 1
            elif c == curses.KEY_RIGHT:
                # Move cursor RIGHT
                if self.check_move_cursor(1): self.xcursor += 1
            elif c == curses.KEY_BEG or c == curses.KEY_HOME:
                # Move cursor to the BEGIN
                self.xcursor = self.x_init
            elif c == curses.KEY_END:
                # Move cursor to the END
                self.xcursor = self.x_init + len(self.input_buffer)
            elif 20 <= c < 127:
                i = self.xcursor - self.x_init
                self.input_buffer = self.input_buffer[:i] + chr(c) + self.input_buffer[i:]
                self.xcursor += 1
                # new search -> reset position
                self.position = 0
                self.page_position = 0


class ArgslistMenu:
    current_arg = 0
    max_preview_size = 0
    prev_lastline_len = 0

    # init arg box margins
    AB_TOP = 0
    AB_SIDE = 0

    xcursor = None
    x_init = None
    y_init = None

    def __init__(self, prev):
        self.previous_menu = prev

    def get_nb_preview_new_lines(self):
        """
        Returns the number of preview lines
        :return:
        """
        next_arg = 0
        nblines = 0
        multiline = '\n' in Gui.cmd.cmdline
        firstline = True
        parts = Gui.cmd.get_command_parts()
        nb_args_todo = len(parts) - 1
        # in case of multiline cmd process each line separately
        # for each line we have to count each char and deduce the
        # number of lines needed to print it
        for line in Gui.cmd.cmdline.split('\n'):
            nbchar = 0

            # for all lines except the first one we have ' >' in addition
            if multiline and (not firstline):
                nbchar = 2
            else:
                firstline = False

            # extract len of args in the current line
            i = 0
            for arg_name, arg_val in Gui.cmd.args:
                if i == next_arg and nb_args_todo > 0:
                    if arg_val != "":
                        # use value len if not empty
                        nbchar += len(arg_val)
                    else:
                        # else use name len + 2 for '<' and '>'
                        nbchar += (len(arg_name) + 2)
                    next_arg += 1
                    nb_args_todo -= 1
                i += 1

            # len of the cmd body
            for p in parts:
                nbchar += len(p)

            nblines += 1 + ((nbchar - 1) // self.max_preview_size)

        return nblines - 1

    def next_arg(self):
        """
        Select the next argument in the list
        """
        # reset cursor position
        self.xcursor = None
        self.x_init = None
        self.y_init = None
        # change selected arg
        if self.current_arg < Gui.cmd.nb_args - 1:
            self.current_arg += 1
        else:
            self.current_arg = 0

    def previous_arg(self):
        """
        Select the previous argument in the list
        """
        # reset cursor position
        self.xcursor = None
        self.x_init = None
        self.y_init = None
        # change selected arg
        if self.current_arg > 0:
            self.current_arg -= 1
        else:
            self.current_arg = Gui.cmd.nb_args - 1

    def draw_preview_part(self, win, text, color):
        """
        Print a part of the preview cmd line
        And start a new line if the last line of the preview is too long
        :param win: window
        :param text: part of the preview to draw
        :param color: color used to draw the text
        """
        for c in text:
            if c == "\n":
                # multi line cmd -> new line
                self.prev_lastline_len = 2
                win.addstr("\n    > ", color)
            elif self.prev_lastline_len < self.max_preview_size:
                # size ok -> print the char
                self.prev_lastline_len += 1
                win.addstr(c, color)
            else:
                # last line too long -> new line
                self.prev_lastline_len = 1
                win.addstr("\n    " + c, color)

    def draw_selected_arg(self, y_pos):
        """
        Draw the selected argument line in the argument menu
        """
        # Skip if no arguments (like for internal commands)
        if Gui.cmd.nb_args == 0:
            return
            
        y, x = self.AB_TOP + y_pos + self.current_arg, self.AB_SIDE + 1
        ncols, nlines = self.width - 2 * (self.AB_SIDE + 1), 1
        arg = Gui.cmd.args[self.current_arg]
        max_size = self.max_preview_size - 4 - len(arg[0])
        selectedargline = curses.newwin(nlines, ncols, y, x)
        selectedargline.addstr("   > ", curses.color_pair(Gui.BASIC_COLOR))
        selectedargline.addstr(arg[0], curses.color_pair(Gui.ARG_NAME_COLOR))
        selectedargline.addstr(" = " + Gui.draw_string(arg[1], max_size), curses.color_pair(Gui.BASIC_COLOR))
        selectedargline.refresh()

    def draw_args_list(self, y_pos):
        """
        Draw the asked arguments list in the argument menu
        """
        # Skip if no arguments (like for internal commands)
        if Gui.cmd.nb_args == 0:
            return
            
        y, x = self.AB_TOP + y_pos, self.AB_SIDE + 1
        ncols, nlines = self.width - 2 * (self.AB_SIDE + 1), Gui.cmd.nb_args + 1
        argwin = curses.newwin(nlines, ncols, y, x)
        for arg in Gui.cmd.args:
            max_size = self.max_preview_size + 4
            argline = Gui.draw_string("     {} = {}".format(*arg), max_size) + "\n"
            argwin.addstr(argline, curses.color_pair(Gui.BASIC_COLOR))
        argwin.refresh()

    def draw_desc_preview(self, argprev, p_x, p_y, description_lines):
        """
        Draw the descriptions_line preview in the preview windows (argprev)
        """
        # draw description
        if len(description_lines) > 0:
            argprev.addstr(p_y, p_x, "-----", curses.color_pair(Gui.BASIC_COLOR))
            p_y += 1
            for description_line in description_lines:
                argprev.addstr(p_y, p_x, description_line, curses.color_pair(Gui.BASIC_COLOR))
                p_y += 1
            p_y += 1
            argprev.refresh()
        return p_y

    def draw_cmd_preview(self, argprev, p_x, p_y=1):
        """
        Draw the cmd preview in the argument menu
        Also used to draw the borders of this menu
        """
        cmdparts = Gui.cmd.get_command_parts()

        # draw command
        argprev.addstr(p_y, p_x, "$ ", curses.color_pair(Gui.BASIC_COLOR))

        # Special handling for generic set command
        import re
        if Gui.cmd.cmdline.strip().startswith('>set'):
            m = re.match(r'>set <variable>=<value>', Gui.cmd.cmdline.strip(), re.IGNORECASE)
            if m and len(Gui.cmd.args) == 2:
                # Show as: >set <variable>=<value>
                var_name = Gui.cmd.args[0][1]
                var_val = Gui.cmd.args[1][1]
                preview = f'>set <{var_name}>={var_val}' if var_name else '>set <variable>=<value>'
                self.draw_preview_part(argprev, preview, curses.color_pair(Gui.BASIC_COLOR))
                argprev.border()
                argprev.refresh()
                return
        # Default: draw preview cmdline interleaved with args
        for i in range(len(cmdparts) + Gui.cmd.nb_args):
            if i % 2 == 0:
                # draw cmd parts in white
                idx = i // 2
                if idx < len(cmdparts):
                    self.draw_preview_part(argprev, cmdparts[idx], curses.color_pair(Gui.BASIC_COLOR))
            else:
                # get argument value
                arg_idx = (i - 1) // 2
                if arg_idx < len(Gui.cmd.args):
                    if Gui.cmd.args[arg_idx][1] == "":
                        # if arg empty use its name
                        arg = '<' + Gui.cmd.args[arg_idx][0] + '>'
                    else:
                        # else its value
                        arg = Gui.cmd.args[arg_idx][1]

                    # draw argument
                    if arg_idx == self.current_arg:
                        # if arg is selected print in blue
                        self.draw_preview_part(argprev, arg, curses.color_pair(Gui.ARG_NAME_COLOR))
                    else:
                        # else in white
                        self.draw_preview_part(argprev, arg, curses.color_pair(Gui.BASIC_COLOR))
        argprev.border()
        argprev.refresh()

    def draw(self, stdscr):
        """
        Draw the arguments menu to ask them
        :param stdscr: screen
        """
        # init vars and set margins values
        self.height, self.width = stdscr.getmaxyx()
        self.AB_SIDE = 5
        padding_text_border = 3
        self.max_preview_size = self.width - (2 * self.AB_SIDE) - (2 * padding_text_border)

        # draw background cheatslist menu (clean resize)
        self.previous_menu.draw(stdscr)

        # draw argslist menu popup
        self.prev_lastline_len = 0
        nbpreviewnewlines = self.get_nb_preview_new_lines()
        # if Gui.cmd.nb_args != 0:
        #     nbpreviewnewlines = self.get_nb_preview_new_lines()
        # else:
        #     nbpreviewnewlines = 0

        # -------------- border
        # cmd
        # nbpreviewnewlines
        # .............. args margin top
        # args
        # ------
        # description
        # .............  description margin
        # ---------- border

        # width - preview
        ncols = self.width - 2 * self.AB_SIDE

        # prepare showed description
        description_lines = Gui.cmd.get_description_cut_by_size(ncols - (padding_text_border * 2))

        border_height = 1
        cmd_height = 1 + nbpreviewnewlines
        args_height = (2 + Gui.cmd.nb_args) if (Gui.cmd.nb_args > 0) else 0
        desc_height = (len(description_lines) + 1 + 1) if (len(description_lines) > 0) else 0

        cmd_pos = 1
        args_pos = border_height + cmd_height + 1
        desc_pos = args_pos + args_height - 1

        nlines = border_height * 2 + cmd_height + args_height + desc_height
        if nlines > self.height:
            nlines = self.height

        self.AB_TOP = (self.height - nlines) // 2
        y, x = self.AB_TOP, self.AB_SIDE

        try:
            argprev = curses.newwin(nlines, ncols, y, x)

            # draw command
            self.draw_cmd_preview(argprev, padding_text_border, cmd_pos)

            # draw description
            self.draw_desc_preview(argprev, padding_text_border, desc_pos, description_lines)

            if len(Gui.cmd.args) > 0:
                self.draw_args_list(args_pos)
                self.draw_selected_arg(args_pos)
                # init cursor position (if first draw)
                if self.x_init is None or self.y_init is None or self.xcursor is None:
                    self.y_init, self.x_init = curses.getsyx()
                    # prefill compatibility
                    self.x_init -= len(Gui.cmd.args[self.current_arg][1])
                    self.xcursor = self.x_init + len(Gui.cmd.args[self.current_arg][1])
                # set cursor position
                curses.setsyx(self.y_init, self.xcursor)
                curses.doupdate()
        except curses.error:
            # catch all curses error to not end with an exception in case of size error
            pass

    def check_move_cursor(self, n):
        if Gui.cmd.nb_args == 0:
            return False
        return self.x_init <= (self.xcursor + n) < self.x_init + len(Gui.cmd.args[self.current_arg][1]) + 1

    def autocomplete_arg(self):
        """
        Autocomplete the current argument
        """
        # current argument value
        argument = Gui.cmd.args[self.current_arg][1]
        # look for all files that match the argument in the working directory
        matches = glob.glob('{}*'.format(argument))

        if not matches:
            return False

        # init the autocompleted argument
        autocompleted_argument = ""
        # autocompleted argument is the longest start common string in all matches
        for i in range(len(min(matches))):
            if not all(min(matches)[:i + 1] == match[:i + 1] for match in matches):
                break
            autocompleted_argument = min(matches)[:i + 1]

        # add a "/" at the end of the autocompleted argument if it is a directory
        if isdir(autocompleted_argument) and autocompleted_argument[-1] != sep:
            autocompleted_argument = autocompleted_argument + sep

        # autocomplete the argument 
        Gui.cmd.args[self.current_arg][1] = autocompleted_argument
        # update cursor position
        self.xcursor = self.x_init + len(autocompleted_argument)

    def run(self, stdscr):
        """
        Arguments selection menu processing..
        :param stdscr: screen
        """
        # init
        Gui.init_colors()
        stdscr.clear()
        while True:
            stdscr.refresh()
            self.draw(stdscr)
            c = stdscr.getch()
            if c == curses.KEY_ENTER or c == 10 or c == 13:
                # try to build the cmd
                # if cmd build is ok -> copy to clipboard and return to main menu
                # else continue in args menu
                if Gui.cmd.build():
                    # Track usage for non-internal commands
                    if not Gui.cmd.cmdline.startswith('>') and hasattr(self.previous_menu, 'popularity_manager') and self.previous_menu.popularity_manager:
                        # Use the original cheat reference stored in the command object
                        if hasattr(Gui.cmd, 'original_cheat'):
                            self.previous_menu.popularity_manager.increment_usage(Gui.cmd.original_cheat)
                    
                    # Persist <ip> and <port> globally if set
                    for arg_name, arg_val in Gui.cmd.args:
                        if arg_name in ['<ip>', 'ip', '<port>', 'port'] and arg_val:
                            # Always store as <ip> or <port>
                            key = '<ip>' if 'ip' in arg_name else '<port>'
                            Gui.armouryGlobalVars[key] = arg_val
                            with open(Gui.savefile, 'w') as f:
                                json.dump(Gui.armouryGlobalVars, f)
                    if hasattr(self.previous_menu, 'ctrl_enter_pressed') and self.previous_menu.ctrl_enter_pressed:
                        # Track usage for non-internal commands
                        if not Gui.cmd.cmdline.startswith('>') and hasattr(self.previous_menu, 'popularity_manager') and self.previous_menu.popularity_manager:
                            if hasattr(Gui.cmd, 'original_cheat'):
                                self.previous_menu.popularity_manager.increment_usage(Gui.cmd.original_cheat)
                        
                        # Open command in new terminal
                        try:
                            if open_in_new_terminal(Gui.cmd.cmdline):
                                Notification.show_instant(stdscr, "Opened in new terminal.")
                            else:
                                Notification.show_instant(stdscr, "Failed to open terminal.")
                        except Exception as e:
                            Notification.show_instant(stdscr, f"Failed to open terminal: {str(e)}")
                        break
                    else:
                        # Copy command to clipboard by default (but not for global variable setting)
                        if not Gui.cmd.cmdline.startswith('>set'):
                            try:
                                clipboard_copy(Gui.cmd.cmdline)
                                if hasattr(self.previous_menu, 'notification_message'):
                                    self.previous_menu.notification_message = "Copied to clipboard."
                                    import time as _time
                                    self.previous_menu.notification_time = _time.time()
                            except ImportError:
                                Notification.show_instant(stdscr, "pyperclip not available.")
                        break
            elif c == curses.KEY_F10 or c == 27:
                # exit args_menu -> return to cheatslist_menu
                self.previous_menu.run(stdscr)
                stdscr.refresh()
                break
            elif c == curses.KEY_DOWN:
                self.next_arg()
            elif c == curses.KEY_UP:
                self.previous_arg()
            elif c == 9:
                if Gui.cmd.args:
                    # autocomplete the current argument
                    if Gui.cmd.args[self.current_arg][1]:
                        self.autocomplete_arg()
                    # go to the next argument
                    else:
                        self.next_arg()
            elif c == 20:
                try:
                    from pyfzf.pyfzf import FzfPrompt
                    files = []
                    for fuzz_dir in config.FUZZING_DIRS:
                        files += glob.glob(fuzz_dir, recursive=True)
                    fzf = FzfPrompt().prompt(files)
                    # autocomplete the argument 
                    Gui.cmd.args[self.current_arg][1] = fzf[0]
                    # update cursor position
                    self.xcursor = self.x_init + len(fzf[0])
                except ImportError:
                    pass
            elif c == curses.KEY_BACKSPACE or c == 127 or c == 8:
                if self.check_move_cursor(-1):
                    i = self.xcursor - self.x_init - 1
                    Gui.cmd.args[self.current_arg][1] = Gui.cmd.args[self.current_arg][1][:i] + \
                                                        Gui.cmd.args[self.current_arg][1][i + 1:]
                    self.xcursor -= 1
            elif c == curses.KEY_DC or c == 127:
                # DELETE key
                if self.check_move_cursor(1):
                    i = self.xcursor - self.x_init - 1
                    Gui.cmd.args[self.current_arg][1] = Gui.cmd.args[self.current_arg][1][:i + 1] + \
                                                        Gui.cmd.args[self.current_arg][1][i + 2:]
            elif c == curses.KEY_LEFT:
                # Move cursor LEFT
                if self.check_move_cursor(-1): self.xcursor -= 1
            elif c == curses.KEY_RIGHT:
                # Move cursor RIGHT
                if self.check_move_cursor(1): self.xcursor += 1
            elif c == curses.KEY_BEG or c == curses.KEY_HOME:
                # Move cursor to the BEGIN
                self.xcursor = self.x_init
            elif c == curses.KEY_END:
                # Move cursor to the END
                self.xcursor = self.x_init + len(Gui.cmd.args[self.current_arg][1])
            elif 20 <= c < 127 and Gui.cmd.nb_args > 0:
                i = self.xcursor - self.x_init
                Gui.cmd.args[self.current_arg][1] = Gui.cmd.args[self.current_arg][1][:i] + chr(c) + \
                                                    Gui.cmd.args[self.current_arg][1][i:]
                self.xcursor += 1


class Gui:
    # result CMD
    cmd = None
    armouryGlobalVars = {}
    savefile = config.savevarfile
    # colors
    BASIC_COLOR = 0  # output std
    COL1_COLOR = 7
    COL2_COLOR = 4  # gold
    COL3_COLOR = 14  # purple light 
    COL4_COLOR = 5  # 26  # violet clair: 14  # 4 yellow  # 6 purple # 7 cyan # 9 dark grey
    COL5_COLOR = 5  # blue
    COL1_COLOR_SELECT = 256  # output std invert
    COL2_COLOR_SELECT = 256
    COL3_COLOR_SELECT = 256
    COL4_COLOR_SELECT = 256
    CURSOR_COLOR_SELECT = 266  # background red
    PROMPT_COLOR = 0
    INFO_NAME_COLOR = 4  # 5
    INFO_DESC_COLOR = 0
    INFO_CMD_COLOR = 0
    ARG_NAME_COLOR = 5
    loaded_menu = False
    with_tags = False

    DEFAULT_RATIOS = {"tags": 14, "title": 8, "name": 23, "description": 55}

    def __init__(self):
        self.cheats_menu = None

    @staticmethod
    def init_colors():
        """ Init curses colors """
        curses.start_color()
        curses.use_default_colors()
        # Try to initialize 256 color pairs if possible
        try:
            for i in range(0, 255):
                curses.init_pair(i + 1, i, -1)
            # Explicitly set color pair 15 as white on black
            curses.init_pair(15, curses.COLOR_WHITE, curses.COLOR_BLACK)
        except Exception:
            # Fallback: just set color pair 15 as white on black
            curses.init_pair(15, curses.COLOR_WHITE, curses.COLOR_BLACK)

    @classmethod
    def get_ratios_for_column(cls, columns_in_use):
        """
        Calculate the column size from the column to print

        :param columns_in_use: List of the column to print when drawing
        :return: The updated ratios size of each columns
        """
        missing_ratio = 0
        for col in cls.DEFAULT_RATIOS.keys():
            if col not in columns_in_use:
                missing_ratio += cls.DEFAULT_RATIOS.get(col)
        if not missing_ratio:
            return cls.DEFAULT_RATIOS

        new_ratio = {}
        for column in columns_in_use:
            new_ratio[column] = math.floor(cls.DEFAULT_RATIOS[column] + missing_ratio / len(columns_in_use))
        return new_ratio

    @staticmethod
    def draw_string(str_value, max_size):
        """
        Return a string of the max size, ended with ... if >= max_size
        :param str_value:
        :param max_size:
        :return:
        """
        result_string = str_value
        if len(str_value) >= max_size:
            result_string = str_value[:max_size - 4] + '...'
        return result_string

    @staticmethod
    def prefix_cmdline_with_prefix():
        if config.PREFIX_GLOBALVAR_NAME in Gui.armouryGlobalVars:
            Gui.cmd.cmdline = f"{Gui.armouryGlobalVars[config.PREFIX_GLOBALVAR_NAME]} {Gui.cmd.cmdline}"

    def run(self, cheatsheets, has_prefix):
        """
        Gui entry point
        :param cheatsheets: cheatsheets dictionary
        """
        if self.cheats_menu is None:
            # Load cheatList if not already done
            self.cheats_menu = CheatslistMenu()
            for value in cheatsheets.values():
                self.cheats_menu.globalcheats.append(value)
            
            # Initialize popularity manager
            self.cheats_menu.popularity_manager = popularity.PopularityManager()

        # if global var save exists load it
        if exists(Gui.savefile):
            with open(Gui.savefile, 'r') as f:
                Gui.armouryGlobalVars = json.load(f)
        # Ensure <ip> and <port> are always present
        if '<ip>' not in Gui.armouryGlobalVars:
            Gui.armouryGlobalVars['<ip>'] = ''
        if '<port>' not in Gui.armouryGlobalVars:
            Gui.armouryGlobalVars['<port>'] = ''

        wrapper(self.cheats_menu.run)
        if Gui.cmd != None and Gui.cmd.cmdline[0] != '>' and has_prefix:
            self.prefix_cmdline_with_prefix()
        return Gui.cmd

def clipboard_copy(text):
    import shutil
    import subprocess
    import sys
    import os
    # Try wl-copy (Wayland)
    if shutil.which('wl-copy'):
        try:
            subprocess.run(['wl-copy'], input=text.encode('utf-8'), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return
        except Exception:
            pass
    # Try xclip (X11)
    if shutil.which('xclip'):
        try:
            subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode('utf-8'), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return
        except Exception:
            pass
    # Try xsel (X11)
    if shutil.which('xsel'):
        try:
            subprocess.run(['xsel', '--clipboard', '--input'], input=text.encode('utf-8'), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return
        except Exception:
            pass
    # Fallback: try pyperclip, but suppress all output
    try:
        import pyperclip
        with open(os.devnull, 'w') as devnull, contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
            pyperclip.copy(text)
    except Exception:
        pass
