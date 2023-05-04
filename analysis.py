import os, git, shutil
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# .env variables
DATA_DIR = os.getenv('DATA_DIR')
PROJECT_INPUT_DATA_DIR = os.getenv('PROJECT_INPUT_DATA_DIR')
PROJECT_DIR = os.getenv('PROJECT_DIR')

# Main IN and OUT variables for convenience
INPUT = DATA_DIR # set whether DATA_DIR or PROJECT_INPUT_DATA_DIR is the source
OUTPUT = PROJECT_DIR

def perform_analysis():
    files_and_folders = os.listdir(INPUT)
    with open(os.path.join(OUTPUT, "results.txt"), "w") as analysis_file:
        analysis_file.write(f"Folders and files in {OUTPUT} direcory:\n")
        analysis_file.write(",".join(files_and_folders))


def main():
    perform_analysis()
    
if __name__  == "__main__":
    main()