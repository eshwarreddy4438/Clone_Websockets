import os

# Define the repository URL and destination directory
repository_url = "https://github.com/rrg/ListOpenFiles"
destination_dir = r"clone_files"

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Construct the git clone command
git_clone_command = f"git clone {repository_url} {destination_dir}"

# Run the command
os.system(git_clone_command)

print(f"Repository cloned into {destination_dir}")
