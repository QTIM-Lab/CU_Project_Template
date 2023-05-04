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
    with open(os.path.join(OUTPUT), "w") as analysis_file:
        analysis_file.write(files_and_folders)

def main():
    if not os.path.exists(OUTPUT):
        os.mkdir(OUTPUT) # create today's analysis folder

    # Get git information
    git_url = git.Repo(os.getcwd()).remote().url
    git_current_commit = git.Repo(os.getcwd()).head.commit.hexsha

    # Make README.md for others in the future
    with open(os.path.join(OUTPUT, "README.md"), "w") as README:
        README.writelines(f"""# Git Repo
{git_url}

# Commit
{git_current_commit}

# Raw Data Source
{INPUT}""")
        
    # Copy .env used to help track 
    shutil.copy(os.path.join(os.getcwd(), ".env"), os.path.join(PROJECT_DIR, ".env"))


if __name__ == "__main__":
    main()