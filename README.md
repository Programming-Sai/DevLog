﻿
# DevLog 

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20MacOS-lightgrey)
![Status](https://img.shields.io/badge/Status-In%20Production-orange)
![CLI](https://img.shields.io/badge/CLI-Supported-orange?logo=windows-terminal)


DevLog is a lightweight, terminal-based tool for tracking coding issues, solutions, and lessons learned in Markdown format. It helps developers log problems, document solutions, and compile their records into a structured Markdown file.  

## Features 🚀  
- **Track Coding Issues**: Log issues with descriptions, code snippets, and tags.  
- **Update & Manage Entries**: Modify entries as you find solutions.  
- **Compile to Markdown**: Generates a well-structured `PROBLEMS.md` file.  
- **Simple CLI Usage**: Easily add, update, and manage logs from the terminal.  

## Installation 📥  
Clone the repository:  
```sh
git clone https://github.com/Programming-Sai/DevLog.git
cd DevLog
```

## Usage ⚡  
Initialize the tracker:  
```sh
python main.py --init
```
Add a new issue:  
```sh
python main.py --id 001 --title "Bug in API response" --tag pending --desc "Unexpected response format" --snippet "fetch(url)..."
```
Mark an issue as solved:  
```sh
python main.py --id 001 --tag solved --solution-desc "Fixed by updating headers"
```
Compile to Markdown:  
```sh
python main.py --compile
```
Delete an issue:  
```sh
python main.py --delete <id>
```
Clear all issues:
```sh
python main.py --clear
```
List all issues: 
```sh
python main.py --list
```

## Future Enhancements ✨  
- Add searching/filtering features  
- Support multiple file formats (JSON, YAML, etc.)  
- Interactive mode for managing logs  

## Roadmap 🛣️  
- [x] Basic CLI functionality  
- [x] Markdown file generation  
- [ ] Implement search/filter features  
- [ ] Improve CLI user experience  
- [x] Package as a standalone executable  
- [ ] Add support for multiple file formats (JSON, YAML, etc.)  


### **Changes Made**
- Added `--list` to the usage section.
- Included delete (`--delete`) and clear (`--clear`) options.
- Updated the roadmap to reflect completed features.
