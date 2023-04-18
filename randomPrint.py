# import necessary modules
import os
import shutil
import random
import subprocess

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


def main():
    isRunOnce = False
    while True:
        # if isRunOnce:
        # subprocess.run(["clear"])
        print("\nEnter 'random' to print a random artwork or 'quit' to exit:  ")
        user_input = input()
        if user_input == "random":
            isRunOnce = True
            print_random_file()
        elif user_input == "quit":
            break
        else:
            isRunOnce = True
            print("\nInvalid input, please try again.")


if __name__ == '__main__':
    main()
