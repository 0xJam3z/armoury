# Popularity-Based Command Ordering Features

## Overview

The armoury tool now includes intelligent command ordering based on popularity and usage statistics. This feature automatically organizes commands by their popularity in the cybersecurity community and tracks individual usage to provide a personalized experience.

## Features

### 1. Popularity-Based Default Ordering

Commands are initially ordered by their popularity in the cybersecurity community, based on:
- Industry usage statistics
- GitHub stars and community adoption
- Tool effectiveness and reliability

**Popularity Rankings Include:**
- **Network Scanning**: nmap (100), masscan (95), netcat (90)
- **Web Testing**: sqlmap (100), burpsuite (95), nikto (90)
- **Password Attacks**: hashcat (100), john (95), hydra (90)
- **Exploitation**: metasploit (100), searchsploit (95)
- **Active Directory**: bloodhound (95), powerview (90), mimikatz (90)
- **And many more...**

### 2. Usage-Based Personalization

- **Automatic Tracking**: Every time you use a command, its usage count is incremented
- **Smart Reordering**: Frequently used commands automatically move to the top of the list
- **Persistent Storage**: Usage statistics are saved between sessions in `.armoury_usage.json`

### 3. Priority System

Commands are ordered by:
1. **Internal Commands** (always at top): `>set`, `>clear`, `>exit`
2. **Usage Count** (descending): Most frequently used commands first
3. **Popularity Score** (descending): Industry-standard popularity
4. **Alphabetical** (ascending): For commands with same usage/popularity

## Implementation Details

### Files Modified

1. **`armoury/modules/popularity.py`** (NEW)
   - Contains popularity rankings for 100+ tools
   - Manages usage tracking and sorting logic
   - Handles JSON persistence of usage data

2. **`armoury/modules/gui.py`**
   - Integrated popularity manager into GUI
   - Added usage tracking for all command execution paths
   - Modified search/sort functionality

3. **`armoury/modules/command.py`**
   - Added reference to original cheat object for usage tracking

### Usage Data Storage

Usage statistics are stored in `~/.armoury_usage.json` with the following format:
```json
{
  "filename:title:name": usage_count,
  "armoury/data/cheats/Scan/nmap.md:Scan:nmap": 15,
  "armoury/data/cheats/Web/sqlmap.md:Web:sqlmap": 8
}
```

### How It Works

1. **Initial Load**: Commands are sorted by popularity score
2. **User Interaction**: When a command is executed (copied to clipboard or opened in terminal), usage is tracked
3. **Dynamic Reordering**: The list is re-sorted after each usage, prioritizing frequently used commands
4. **Persistence**: Usage data is automatically saved and restored between sessions

## Benefits

- **Faster Access**: Most used commands appear at the top
- **Learning Curve**: Popular tools are prioritized for new users
- **Personalization**: Each user's experience becomes more tailored over time
- **No Configuration**: Works automatically without user intervention

## Technical Notes

- Usage tracking is completely transparent to the user
- No performance impact on command execution
- Backward compatible with existing armoury installations
- Usage data is stored locally and privately

## Example Behavior

**Initial Order (by popularity):**
1. >set <variable>=<value>
2. >clear
3. >exit
4. nmap (popularity: 100)
5. sqlmap (popularity: 100)
6. hashcat (popularity: 100)
7. custom_script (popularity: 50)

**After using hashcat 3 times and nmap 1 time:**
1. >set <variable>=<value>
2. >clear
3. >exit
4. hashcat (usage: 3, popularity: 100)
5. nmap (usage: 1, popularity: 100)
6. sqlmap (usage: 0, popularity: 100)
7. custom_script (usage: 0, popularity: 50) 