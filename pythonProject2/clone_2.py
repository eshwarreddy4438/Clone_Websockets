import os

# Define the repository URL and destination directory
repository_url = "https://github.com/Murari-ch/heart-health-prediction-.git"
destination_dir = r"clone_files_2"

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Construct the git clone command
git_clone_command = f"git clone {repository_url} {destination_dir}"

# Run the command
os.system(git_clone_command)

print(f"Repository cloned into {destination_dir}")
