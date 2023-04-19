# import necessary modules
import subprocess
import random
import os
from pynput import keyboard

# Global variable to control the script termination
terminate_script = False

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


def on_press(key):
    global terminate_script
    try:
        if key == keyboard.Key.space:
            print("space bar is pressed")
        elif keyboard.Key.esc:
            terminate_script = True
            return False
    except AttributeError:
        pass


def main():
    global terminate_script
    print("Press the space key to print a random file or 'R' to exit")

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while not terminate_script:
        listener.join(1)

    listener.stop()


if __name__ == '__main__':
    main()
