import re
import curses
import textwrap


class Command:
    cmdline = ""
    description = ""
    args = []  # [(name, value)]
    nb_args = 0
    nb_lines_cmd = 1
    nb_lines_desc = 0

    def __init__(self, cheat, gvars):
        self.cmdline = cheat.command
        self.original_cheat = cheat  # Store reference to original cheat for usage tracking

        self.cmd_tags = cheat.command_tags
        self.description = ''
        for tag in self.cmd_tags:
            self.description += '[' + self.cmd_tags[tag] + '] '
        if self.description != '' and cheat.description != '':
            self.description += '\n-----\n'
        self.description += cheat.description

        self.get_args(cheat, gvars)
        self.nb_args = len(self.args)
        # careful this is not the lines number in GUI
        self.nb_lines_cmd = len(cheat.command.split('\n'))
        # careful this is not the lines number in GUI
        self.nb_lines_desc = 0 if cheat.description == '' else len(cheat.description.split('\n'))

    def get_description_cut_by_size(self, size):
        """
        The description cut by lines inside the gui size
        """
        desc_lines = self.description.split('\n')
        result = []
        for line in desc_lines:
            result.extend(textwrap.wrap(line, size))
        return result

    def get_args(self, cheat, gvars):
        """
        Process cmdline from the cheatsheet to get args names
        """
        self.args = []
        # Special handling for >set <var>=<value> pattern
        if cheat.command.strip().startswith('>set'):
            m = re.match(r'>set <([^>]+)>=<value>', cheat.command.strip(), re.IGNORECASE)
            if m:
                varname = m.group(1).lower()
                if varname == 'variable':
                    # Generic set: prompt for variable and value
                    self.args = [['variable', ''], ['value', '']]
                else:
                    # Specific set: prompt for just the variable
                    self.args = [[varname, gvars.get(f'<{varname}>', '')]]
            else:
                # fallback: just show variable
                self.args = [['variable', '']]
            return
        # Extract argument names from the command
        arg_names = re.findall(r'<([^ <>]+)>', cheat.command)
        arg_names = [a.lower() for a in arg_names]
        # Use a list of tuples here instead of dict in case
        # the cmd has multiple args with the same name..
        for arg_name in arg_names:
            if '|' in arg_name:  # Format <name|default_value>
                name, var = arg_name.split("|", 1)
                self.args.append([name, var])
                # Variable has been added to cheat variables before, remove it
                cheat.command = cheat.command.replace(arg_name, name)
                self.cmdline = cheat.command
            elif f'<{arg_name}>' in gvars:
                self.args.append([arg_name, gvars[f'<{arg_name}>']])
            elif arg_name in cheat.variables:
                self.args.append([arg_name, cheat.variables[arg_name]])
            else:
                self.args.append([arg_name, ""])

    def get_command_parts(self):
        # Special handling for internal commands (starting with '>')
        if self.cmdline.startswith('>'):
            return [self.cmdline]
        
        if self.nb_args != 0:
            regex = ''.join('<' + arg[0] + '>|' for arg in self.args)[:-1]
            cmdparts = re.split(regex, self.cmdline)
        else:
            cmdparts = [self.cmdline]
        return cmdparts

    def build(self):
        """
        Called after argument completion
        -> if some args values are still empty do nothing
        -> else build the final command string by adding args values
        """
        # Special handling for internal commands (starting with '>')
        if self.cmdline.startswith('>'):
            return True
            
        if self.nb_args == 0 :
            return True
        argsval = [a[1] for a in self.args]
        if "" not in argsval:
            # split cmdline at each arg position
            regex = ''.join('<' + arg[0] + '>|' for arg in self.args)[:-1]
            cmdparts = re.split(regex, self.cmdline)
            # concat command parts and arguments values to build the command
            self.cmdline = ""
            for i in range(len(cmdparts) + len(self.args)):
                if i % 2 == 0:
                    self.cmdline += cmdparts[i // 2]
                else:
                    self.cmdline += argsval[(i - 1) // 2]
            curses.endwin()

        # build ok ?
        return "" not in argsval
