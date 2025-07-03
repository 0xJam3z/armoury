#!/usr/bin/python3
import json
import os
from pathlib import Path
from typing import Dict, List, Tuple

# Popularity rankings for common pentesting tools/commands
# Based on industry usage, GitHub stars, and community adoption
POPULARITY_RANKINGS = {
    # Network scanning and enumeration
    "nmap": 100,
    "masscan": 95,
    "netcat": 90,
    "socat": 85,
    "chisel": 80,
    
    # Web application testing
    "sqlmap": 100,
    "burpsuite": 95,
    "nikto": 90,
    "dirb": 85,
    "gobuster": 80,
    "ffuf": 85,
    "wpscan": 75,
    "joomscan": 70,
    
    # Password attacks
    "hashcat": 100,
    "john": 95,
    "hydra": 90,
    "medusa": 80,
    "patator": 75,
    
    # Exploitation frameworks
    "metasploit": 100,
    "searchsploit": 95,
    "msfvenom": 90,
    
    # Active Directory
    "bloodhound": 95,
    "powerview": 90,
    "rubeus": 85,
    "mimikatz": 90,
    "impacket": 85,
    "certipy": 80,
    
    # Wireless
    "aircrack": 90,
    "reaver": 80,
    "wifite": 75,
    
    # Social engineering
    "setoolkit": 85,
    "phishing": 80,
    
    # Post exploitation
    "linpeas": 90,
    "winpeas": 90,
    "linenum": 85,
    "linux-exploit-suggester": 80,
    
    # File transfer
    "wget": 85,
    "curl": 85,
    "scp": 80,
    "rsync": 75,
    
    # Privilege escalation
    "sudo": 90,
    "su": 85,
    "cron": 80,
    "capabilities": 75,
    
    # C2 and persistence
    "cobalt": 90,
    "sliver": 85,
    "havoc": 80,
    
    # Forensics and analysis
    "volatility": 85,
    "autopsy": 80,
    "binwalk": 75,
    
    # Mobile
    "apktool": 80,
    "jadx": 80,
    "objection": 75,
    
    # Cloud
    "aws": 85,
    "azure": 80,
    "gcp": 75,
    
    # Container security
    "docker": 85,
    "kubernetes": 80,
    
    # Reverse engineering
    "ghidra": 85,
    "ida": 80,
    "radare2": 75,
    
    # Cryptography
    "openssl": 90,
    "gpg": 80,
    
    # Database
    "mysql": 80,
    "postgres": 80,
    "mssql": 75,
    "redis": 70,
    
    # Protocol specific
    "smb": 85,
    "ldap": 80,
    "dns": 75,
    "ftp": 70,
    "ssh": 85,
    "telnet": 60,
    "rdp": 75,
    "vnc": 70,
    
    # Misc tools
    "git": 85,
    "docker": 85,
    "kubectl": 80,
    "ansible": 75,
    "terraform": 70,
}

class PopularityManager:
    def __init__(self, savefile_path: str = None):
        if savefile_path is None:
            # Use the same directory as the global vars file
            from . import config
            savefile_path = os.path.join(os.path.dirname(config.savevarfile), ".armoury_usage.json")
        
        self.savefile_path = savefile_path
        self.usage_counts = self._load_usage_counts()
    
    def _load_usage_counts(self) -> Dict[str, int]:
        """Load usage counts from JSON file"""
        try:
            if os.path.exists(self.savefile_path):
                with open(self.savefile_path, 'r') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
        return {}
    
    def _save_usage_counts(self):
        """Save usage counts to JSON file"""
        try:
            with open(self.savefile_path, 'w') as f:
                json.dump(self.usage_counts, f, indent=2)
        except IOError:
            pass
    
    def get_command_popularity_score(self, cheat) -> int:
        """Calculate popularity score for a command based on its content"""
        if not cheat.command or cheat.command.startswith('>'):
            return 0  # Internal commands get 0 score
        
        command_lower = cheat.command.lower()
        name_lower = cheat.name.lower()
        title_lower = cheat.str_title.lower()
        
        # Check for exact matches first
        for tool, score in POPULARITY_RANKINGS.items():
            if tool in command_lower or tool in name_lower or tool in title_lower:
                return score
        
        # Check for partial matches
        for tool, score in POPULARITY_RANKINGS.items():
            if any(part in command_lower for part in tool.split()):
                return score - 10  # Slight penalty for partial matches
        
        # Default score for unknown commands
        return 50
    
    def get_usage_count(self, cheat) -> int:
        """Get usage count for a specific cheat"""
        cheat_id = self._get_cheat_id(cheat)
        return self.usage_counts.get(cheat_id, 0)
    
    def increment_usage(self, cheat):
        """Increment usage count for a specific cheat"""
        cheat_id = self._get_cheat_id(cheat)
        self.usage_counts[cheat_id] = self.usage_counts.get(cheat_id, 0) + 1
        self._save_usage_counts()
    
    def _get_cheat_id(self, cheat) -> str:
        """Generate a unique identifier for a cheat"""
        # Use a combination of filename, title, and name for uniqueness
        return f"{cheat.filename}:{cheat.str_title}:{cheat.name}"
    
    def sort_cheats_by_popularity_and_usage(self, cheats: List) -> List:
        """Sort cheats by popularity score and usage count"""
        def sort_key(cheat):
            # Internal commands (starting with '>') should always be at the top
            if cheat.command.startswith('>'):
                return (1000, 0, 0)  # Highest priority for internal commands
            
            popularity_score = self.get_command_popularity_score(cheat)
            usage_count = self.get_usage_count(cheat)
            
            # Sort by: usage_count (desc), popularity_score (desc), name (asc)
            return (usage_count, popularity_score, cheat.name.lower())
        
        return sorted(cheats, key=sort_key, reverse=True) 