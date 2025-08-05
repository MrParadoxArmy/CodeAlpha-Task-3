# Bug Bounty Scanner 🕵️‍♂️

## Objective
This tool helps bug bounty hunters and security researchers detect basic flaws in web applications.

## Features
- Detects common vulnerable paths
- Scans for SQLi and XSS payload reflections
- Logs possible vulnerable endpoints

## Usage
```bash
python3 scanner.py
```

Then input a target URL like:
```
https://example.com
```

## Example Output
```
🔍 Scanning: https://example.com
[+] Possible Issue Found at: https://example.com/admin
[+] Possible Issue Found at: https://example.com/?id=1' OR '1'='1
```

## Requirements
Install dependencies using:
```bash
pip install -r requirements.txt
```

## Disclaimer
This tool is for educational and authorized testing only. Do not use it against systems without permission.
