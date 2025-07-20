# Basic-Keylogger-Program
Basic keylogger program that records and logs keystrokes
# Basic Keylogger Project

This is a simple Python-based keylogger program designed for educational purposes to demonstrate how to capture and log keystrokes to a file. **Important**: Use this software ethically and only on devices you own or have explicit permission to monitor. Unauthorized use of keyloggers is illegal and unethical in most jurisdictions.

## Features
- Captures and logs keystrokes with timestamps.
- Saves logs to a file named `keystrokes.txt`.
- Handles special keys (e.g., space, enter, backspace) with readable labels.
- Stops logging when the ESC key is pressed.
- Includes error handling for robust operation.

## Prerequisites
- Python 3.x installed.
- The `keyboard` Python library.

## Installation
1. **Install Python**: Ensure Python 3.x is installed on your system. Download it from [python.org](https://www.python.org/downloads/) if needed.
2. **Install the `keyboard` library**:
   ```bash
   pip install keyboard
   ```
3. **Clone or download the project**: Copy the keylogger script (`keylogger.py`) to your working directory.

## Usage
1. **Run the script**:
   - On Windows, run the script with administrator privileges (required for keyboard hooks):
     ```bash
     python keylogger.py
     ```
   - On Linux/macOS, use sudo for elevated permissions:
     ```bash
     sudo python keylogger.py
     ```
2. **Start logging**: The program will start capturing keystrokes and saving them to `keystrokes.txt` in the same directory.
3. **Stop logging**: Press the ESC key to stop the keylogger.
4. **View logs**: Open `keystrokes.txt` to see the logged keystrokes with timestamps.

## Example Log Output
The `keystrokes.txt` file will look like this:
```
Keylogger Log
2025-07-20 06:20:45: h
2025-07-20 06:20:46: e
2025-07-20 06:20:46: l
2025-07-20 06:20:47: l
2025-07-20 06:20:48: o
2025-07-20 06:20:49: [SPACE]
2025-07-20 06:20:50: [ENTER]
```

## Steps Taken to Create the Project
1. **Project Planning**:
   - Defined the goal: Create a simple keylogger for educational purposes.
   - Identified key features: Capture keystrokes, log with timestamps, handle special keys, and stop on ESC.
   - Chose Python with the `keyboard` library for cross-platform compatibility and ease of use.
2. **Library Selection**:
   - Selected the `keyboard` library for its robust key event handling.
   - Included `datetime` for timestamp logging and `os` for file handling.
3. **Code Development**:
   - Created a function (`log_keystroke`) to process key events and format special keys (e.g., space as " ", enter as "[ENTER]").
   - Implemented file appending to `keystrokes.txt` with timestamps.
   - Added a main loop to start/stop the keylogger using the ESC key.
   - Included error handling for keyboard interrupts and general exceptions.
4. **Ethical Considerations**:
   - Added clear warnings about ethical use and legal implications.
   - Emphasized the need for consent and compliance with local laws.
5. **Testing**:
   - Tested on a local machine to ensure key capture, file logging, and proper handling of special keys.
   - Verified that the program stops cleanly on ESC and handles errors gracefully.
6. **Documentation**:
   - Created this README to explain setup, usage, and ethical considerations.
   - Included example output and detailed steps for reproducibility.

## Ethical and Legal Considerations
- **Consent**: Only use this keylogger on devices you own or have explicit permission to monitor.
- **Legality**: Unauthorized keylogging is illegal in many jurisdictions. Always verify local laws before use.
- **Purpose**: This project is for educational purposes only. Do not use it to harm or spy on others.
- **Security**: Protect the log file, as it may contain sensitive information like passwords.

## Limitations
- Requires elevated permissions (admin/root) to capture keystrokes on some systems.
- Does not capture mouse events, clipboard data, or other inputs.
- Logs are stored in plain text; no encryption is implemented.
- The `keyboard` library may not work on all systems without configuration.

## Troubleshooting
- Requires elevated permissions (admin/root) to capture keystrokes on some systems.
- Does not capture mouse events, clipboard data, or other inputs.
- Logs are stored in plain text; no encryption is implemented.
- The `keyboard` library may not work on all systems without configuration.

