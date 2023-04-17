# import necessary modules
import os
import shutil
import random
import subprocess

# define the function to randomly select a file and put it in a folder


def copy_random_jpeg():
    # specify source and destination path
    source_path = "./jpeg"
    destination_path = "./randomJpeg"

    # get a list of .jpeg files in the source folder
    jpeg_files = [f for f in os.listdir(source_path) if f.endswith(".jpeg")]

    # select a random file
    random_file = random.choice(jpeg_files)
    print("random_file: " + random_file)

    # specify destination path if not existing
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # move the random file to the destination folder
    if os.path.exists(destination_path):
        shutil.copy(os.path.join(source_path, random_file),
                    os.path.join(destination_path, random_file))
        print("random jpeg was selected and copied to the folder 'randomJpeg'")


def main():
    isRunOnce = False
    while True:
        # if isRunOnce:
        # subprocess.run(["clear"])
        print("\nEnter 'random' to copy a random JPEG or 'quit' to exit:  ")
        user_input = input()
        if user_input == "random":
            isRunOnce = True
            copy_random_jpeg()
        elif user_input == "quit":
            break
        else:
            isRunOnce = True
            print("\nInvalid input, please try again.")


if __name__ == '__main__':
    main()
