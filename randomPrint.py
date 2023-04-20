# import necessary modules
import subprocess
import random
import sys
import termios
import tty
import os
from pynput import keyboard

# Global variable to control the script termination
stop_listener = False

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
    print("random file " + random_file + "was selected and sent to the printer")

    # Display the instruction message again
    MAGENTA = "\033[35m"
    RESET = "\033[0m"
    print(
        f"\n{MAGENTA}Press the right key to print a random file or the left key to exit{RESET}")


def on_press(key):
    global stop_listener
    try:
        if key.char.lower() == 'p':
            print_random_file()
        elif key.char.lower() == 'q':
            stop_listener = True
            return False
    except AttributeError:
        pass


def main():
    # ANSI escape code for purple text
    MAGENTA = "\033[35m"
    # ANSI escape code to reset the text formatting
    RESET = "\033[0m"

    print(
        f"\n{MAGENTA}Press the left key to print a random file or the right key to exit{RESET}")

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
