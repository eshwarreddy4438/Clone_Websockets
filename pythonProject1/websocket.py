import os
import asyncio
import websockets


# Function to clone the repository
def clone_repository(repo_url, clone_dir):
    # Ensure the destination directory exists
    os.makedirs(clone_dir, exist_ok=True)

    # Construct and run the git clone command
    git_clone_command = f"git clone {repo_url} {clone_dir}"
    print(f"Cloning repository from {repo_url} to {clone_dir}...")
    os.system(git_clone_command)
    print(f"Repository cloned into {clone_dir}")


# Function to read the repository contents
def get_repository_data(repo_path):
    print(f"Starting to read files from: {repo_path}")
    files_data = {}
    for root, dirs, files in os.walk(repo_path):
        print(f"Accessing directory: {root}")
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Reading file: {file_path}")
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    files_data[file_path] = f.read()  # Store file content as a string
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
    print("Finished reading repository data.")
    return files_data


# WebSocket handler function
async def send_repo_data(websocket, path):
    print("WebSocket connection established.")
    repo_path = r"D:\wallpapers\eshwar reddy\ML_PROJECTS\pythonProject1\clone_files"

    # Get repository data
    repo_data = get_repository_data(repo_path)

    # Send the data over WebSocket
    print("Sending repository data over WebSocket...")
    await websocket.send(str(repo_data))  # Convert dictionary to string for sending
    print("Repository data sent.")


# WebSocket server setup
async def start_server():
    print("Starting WebSocket server...")
    async with websockets.serve(send_repo_data, "localhost", 8765):  # Server on port 8765
        print("WebSocket server is running on ws://localhost:8765")
        await asyncio.Future()  # Run forever


# Main execution function
if __name__ == "__main__":
    # Step 1: Clone the repository
    repository_url = "https://github.com/rrg/ListOpenFiles"
    destination_dir = r"D:\wallpapers\eshwar reddy\ML_PROJECTS\pythonProject1\clone_files"
    clone_repository(repository_url, destination_dir)

    # Step 2: Start the WebSocket server
    asyncio.run(start_server())
