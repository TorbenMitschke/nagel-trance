# import necessary modules
import subprocess
import random
import sys
import termios
import tty
import os
import time
from pynput import keyboard

# Global variable to control the script termination
stop_listener = False

# Add a global variable to store the last time the print function was called
last_print_time = None

# Define the minimum time between print function calls (in seconds)
min_time_between_prints = 60  # 1 minute

# define the function to randomly select a file and send it to the default printer job queue


def print_random_file():
    # specify source and destination path
    source_path = "./pdf"

    # get a list of .pdf files in the source folder
    pdf_files = [f for f in os.listdir(source_path) if f.endswith(".pdf")]

    # select a random file
    random_file = random.choice(pdf_files)
    print("random_file: " + random_file)

    # print the random file -> send file to default printer queue
    subprocess.run(["lp", os.path.join(source_path, random_file)])
    print("random artwork " + random_file +
          " was selected and sent to the printer")

    # Display the instruction message again
    RED = "\033[31m"
    RESET = "\033[0m"
    print(
        f"\n{RED}Do not press the left key!{RESET}")


def on_press(key):
    global stop_listener, last_print_time
    try:
        if key.char.lower() == 'y':
            current_time = time.time()

            # Check if the print function can be called
            if last_print_time is None or (current_time - last_print_time) >= min_time_between_prints:
                print_random_file()
                last_print_time = current_time
            else:
                print(
                    "Don't be wasteful and wait some time before printing again. Wait for the red prompt.")
        elif key.char.lower() == 'w':
            print("\nNageltrance ist Nageltrance.\n")
        elif key.char.lower() == 'q':
            stop_listener = True
            return False
    except AttributeError:
        pass


def main():
    # ANSI escape code for purple text
    RED = "\033[31m"
    # ANSI escape code to reset the text formatting
    RESET = "\033[0m"

    print(
        f"\n{RED}Do not press the left key!{RESET}")

    # Save the current terminal settings
    old_settings = termios.tcgetattr(sys.stdin)

    try:
        # Disable terminal echoing
        tty.setcbreak(sys.stdin.fileno())

        listener = keyboard.Listener(on_press=on_press)
        listener.start()

        while not stop_listener:
            listener.join(1)

        listener.stop()

    finally:
        # Restore the terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


if __name__ == '__main__':
    main()
