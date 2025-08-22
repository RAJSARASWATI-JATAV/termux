import csv

# Termux Basic Commands for Beginners
basic_commands = [
    {
        "Command": "pkg update",
        "Description": "Package list को update करता है",
        "Usage": "pkg update",
        "Category": "Package Management",
        "Frequency": "Daily"
    },
    {
        "Command": "pkg upgrade", 
        "Description": "Installed packages को upgrade करता है",
        "Usage": "pkg upgrade",
        "Category": "Package Management", 
        "Frequency": "Daily"
    },
    {
        "Command": "termux-setup-storage",
        "Description": "Android storage access permission देता है",
        "Usage": "termux-setup-storage",
        "Category": "System Setup",
        "Frequency": "One-time"
    },
    {
        "Command": "ls",
        "Description": "Files और directories list करता है", 
        "Usage": "ls -la",
        "Category": "File Management",
        "Frequency": "Very High"
    },
    {
        "Command": "cd",
        "Description": "Directory change करने के लिए",
        "Usage": "cd /path/to/directory", 
        "Category": "Navigation",
        "Frequency": "Very High"
    },
    {
        "Command": "pwd",
        "Description": "Current working directory show करता है",
        "Usage": "pwd",
        "Category": "Navigation",
        "Frequency": "High"
    },
    {
        "Command": "mkdir",
        "Description": "New directory create करता है",
        "Usage": "mkdir foldername",
        "Category": "File Management", 
        "Frequency": "High"
    },
    {
        "Command": "rm",
        "Description": "Files या directories delete करता है",
        "Usage": "rm filename या rm -rf foldername",
        "Category": "File Management",
        "Frequency": "Medium"
    },
    {
        "Command": "cp",
        "Description": "Files या directories copy करता है",
        "Usage": "cp source destination",
        "Category": "File Management",
        "Frequency": "Medium"
    },
    {
        "Command": "mv",
        "Description": "Files को move या rename करता है", 
        "Usage": "mv oldname newname",
        "Category": "File Management",
        "Frequency": "Medium"
    },
    {
        "Command": "cat",
        "Description": "File content display करता है",
        "Usage": "cat filename",
        "Category": "File Viewing",
        "Frequency": "High"
    },
    {
        "Command": "nano",
        "Description": "Text editor (beginner-friendly)",
        "Usage": "nano filename",
        "Category": "Text Editing",
        "Frequency": "High"
    },
    {
        "Command": "chmod",
        "Description": "File permissions change करता है",
        "Usage": "chmod +x filename",
        "Category": "System Administration",
        "Frequency": "Medium"
    },
    {
        "Command": "clear",
        "Description": "Terminal screen clear करता है",
        "Usage": "clear",
        "Category": "Utility",
        "Frequency": "High"
    },
    {
        "Command": "exit",
        "Description": "Termux session close करता है",
        "Usage": "exit",
        "Category": "Session Management", 
        "Frequency": "High"
    }
]

# Termux Installation Steps
installation_steps = [
    {
        "Step": 1,
        "Title": "Download F-Droid",
        "Action": "F-Droid APK download करें https://f-droid.org से",
        "Time_Required": "2 minutes",
        "Difficulty": "Easy"
    },
    {
        "Step": 2,
        "Title": "Install F-Droid",
        "Action": "Downloaded APK को install करें (Allow from unknown sources)",
        "Time_Required": "1 minute", 
        "Difficulty": "Easy"
    },
    {
        "Step": 3,
        "Title": "Search Termux",
        "Action": "F-Droid app में Termux search करें",
        "Time_Required": "30 seconds",
        "Difficulty": "Easy"
    },
    {
        "Step": 4,
        "Title": "Install Termux",
        "Action": "Termux app को install करें F-Droid से",
        "Time_Required": "3-5 minutes",
        "Difficulty": "Easy"
    },
    {
        "Step": 5,
        "Title": "First Launch", 
        "Action": "Termux को पहली बार open करें",
        "Time_Required": "30 seconds",
        "Difficulty": "Easy"
    },
    {
        "Step": 6,
        "Title": "Update Packages",
        "Action": "pkg update && pkg upgrade command run करें",
        "Time_Required": "5-10 minutes",
        "Difficulty": "Easy"
    },
    {
        "Step": 7,
        "Title": "Setup Storage",
        "Action": "termux-setup-storage command run करें",
        "Time_Required": "1 minute",
        "Difficulty": "Easy"
    },
    {
        "Step": 8,
        "Title": "Install Basic Tools",
        "Action": "pkg install git curl wget nano",
        "Time_Required": "3-5 minutes", 
        "Difficulty": "Easy"
    }
]

# Essential Packages for Beginners
essential_packages = [
    {
        "Package": "git",
        "Install_Command": "pkg install git",
        "Purpose": "Version control और repositories clone करने के लिए",
        "Size": "~15MB",
        "Priority": "High"
    },
    {
        "Package": "curl",
        "Install_Command": "pkg install curl",
        "Purpose": "Internet से files download करने के लिए",
        "Size": "~5MB",
        "Priority": "High"
    },
    {
        "Package": "wget", 
        "Install_Command": "pkg install wget",
        "Purpose": "Files download करने के लिए (curl का alternative)",
        "Size": "~3MB", 
        "Priority": "Medium"
    },
    {
        "Package": "nano",
        "Install_Command": "pkg install nano",
        "Purpose": "Simple text editor (beginners के लिए best)",
        "Size": "~2MB",
        "Priority": "High"
    },
    {
        "Package": "python",
        "Install_Command": "pkg install python",
        "Purpose": "Python programming language",
        "Size": "~50MB",
        "Priority": "High"
    },
    {
        "Package": "nodejs",
        "Install_Command": "pkg install nodejs",
        "Purpose": "JavaScript runtime environment",
        "Size": "~30MB",
        "Priority": "Medium"
    },
    {
        "Package": "openssh",
        "Install_Command": "pkg install openssh", 
        "Purpose": "SSH client और server functionality",
        "Size": "~8MB",
        "Priority": "Medium"
    },
    {
        "Package": "htop",
        "Install_Command": "pkg install htop",
        "Purpose": "System processes monitor करने के लिए",
        "Size": "~1MB",
        "Priority": "Medium"
    },
    {
        "Package": "zip",
        "Install_Command": "pkg install zip unzip",
        "Purpose": "Archive files create और extract करने के लिए",
        "Size": "~2MB",
        "Priority": "Medium"
    },
    {
        "Package": "termux-api",
        "Install_Command": "pkg install termux-api",
        "Purpose": "Android features access करने के लिए", 
        "Size": "~5MB",
        "Priority": "Low"
    }
]

# Common Beginner Mistakes and Solutions
common_mistakes = [
    {
        "Mistake": "Google Play Store से Termux install करना",
        "Problem": "Outdated version, limited features, compatibility issues",
        "Solution": "F-Droid से latest version install करें",
        "Severity": "High"
    },
    {
        "Mistake": "pkg update नहीं करना",
        "Problem": "Package installation errors, security vulnerabilities",
        "Solution": "Regular basis पर pkg update && pkg upgrade run करें", 
        "Severity": "Medium"
    },
    {
        "Mistake": "Storage permission नहीं देना",
        "Problem": "Files access नहीं कर सकते",
        "Solution": "termux-setup-storage command run करें",
        "Severity": "Medium" 
    },
    {
        "Mistake": "Root access की गलत समझ",
        "Problem": "Termux को root की जरूरत नहीं, बिना root के भी powerful",
        "Solution": "Root के बिना ही Termux use करें",
        "Severity": "Low"
    },
    {
        "Mistake": "Extra keys enable नहीं करना", 
        "Problem": "Typing में difficulty, important keys missing",
        "Solution": "Volume Up + Q press करके extra keys enable करें",
        "Severity": "Low"
    },
    {
        "Mistake": "Files को wrong location में save करना",
        "Problem": "Files access नहीं हो पाते",
        "Solution": "~/storage/ directory use करें shared storage के लिए",
        "Severity": "Medium"
    }
]

# Keyboard Shortcuts
keyboard_shortcuts = [
    {
        "Shortcut": "Volume Down + L",
        "Function": "Clear terminal screen (Ctrl+L)",
        "Usage": "Terminal clear करने के लिए",
        "Category": "Navigation"
    },
    {
        "Shortcut": "Volume Down + C", 
        "Function": "Cancel current command (Ctrl+C)",
        "Usage": "Running process को stop करने के लिए",
        "Category": "Process Control"
    },
    {
        "Shortcut": "Volume Down + D",
        "Function": "Logout/Exit (Ctrl+D)",
        "Usage": "Session close करने के लिए",
        "Category": "Session Control"
    },
    {
        "Shortcut": "Volume Up + Q",
        "Function": "Toggle extra keys",
        "Usage": "Extra keyboard row show/hide करने के लिए",
        "Category": "Interface"
    },
    {
        "Shortcut": "Volume Up + T",
        "Function": "Tab key",
        "Usage": "Auto-completion के लिए",
        "Category": "Text Input"
    },
    {
        "Shortcut": "Volume Up + E", 
        "Function": "Escape key",
        "Usage": "Cancel operations के लिए",
        "Category": "Text Input"
    },
    {
        "Shortcut": "Volume Up + W/A/S/D",
        "Function": "Arrow keys (Up/Left/Down/Right)",
        "Usage": "Navigation और cursor movement",
        "Category": "Navigation"
    },
    {
        "Shortcut": "Volume Up + 1-9",
        "Function": "Function keys F1-F9",
        "Usage": "Function keys का alternative",
        "Category": "Function Keys"
    }
]

# Create CSV files
with open('termux_basic_commands.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Command', 'Description', 'Usage', 'Category', 'Frequency']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(basic_commands)

with open('termux_installation_steps.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Step', 'Title', 'Action', 'Time_Required', 'Difficulty'] 
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(installation_steps)

with open('termux_essential_packages.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Package', 'Install_Command', 'Purpose', 'Size', 'Priority']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(essential_packages)

with open('termux_common_mistakes.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Mistake', 'Problem', 'Solution', 'Severity']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(common_mistakes)

with open('termux_keyboard_shortcuts.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Shortcut', 'Function', 'Usage', 'Category'] 
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(keyboard_shortcuts)

print("✅ All CSV files created successfully!")
print("\n📊 Files Summary:")
print(f"1. Basic Commands: {len(basic_commands)} commands")
print(f"2. Installation Steps: {len(installation_steps)} steps") 
print(f"3. Essential Packages: {len(essential_packages)} packages")
print(f"4. Common Mistakes: {len(common_mistakes)} mistakes")
print(f"5. Keyboard Shortcuts: {len(keyboard_shortcuts)} shortcuts")

print("\n📁 Created Files:")
print("• termux_basic_commands.csv")
print("• termux_installation_steps.csv") 
print("• termux_essential_packages.csv")
print("• termux_common_mistakes.csv")
print("• termux_keyboard_shortcuts.csv")