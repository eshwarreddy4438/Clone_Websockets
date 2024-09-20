import os
import asyncio
import websockets
import json

# Define the API key as a string of characters
api_key = "AIzaSyDW2KLyD7VFO4Yav92Mx4_8E5WHWSWppng"

# Function to clone the repository
def clone_repository(repo_url, clone_dir):
    # Ensure the destination directory exists
    os.makedirs(clone_dir, exist_ok=True)

    # Construct and run the git clone command
    git_clone_command = f"git clone {repo_url} {clone_dir}"
    print(f"Cloning repository from {repo_url} to {clone_dir}...")
    os.system(git_clone_command)
    print(f"Repository cloned into {clone_dir}")

# Function to send data through the WebSocket
async def send_data(websocket, path):
    # Prepare the data to send, including the API key and file contents
    directory_to_send = r"D:\wallpapers\eshwar reddy\ML_PROJECTS\pythonProject2\clone_files_2"  # Specify your repository path
    files_data = {}

    # Read all files from the specified directory
    for filename in os.listdir(directory_to_send):
        file_path = os.path.join(directory_to_send, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                files_data[filename] = file.read()  # Store filename and content

    # Combine API key and files data into one message
    data_to_send = {
        "key": api_key,
        "files": files_data
    }

    # Convert the data into a text format suitable for sending
    data_as_text = json.dumps(data_to_send)

    # Send the data over the WebSocket
    await websocket.send(data_as_text)
    print("Data has been sent.")

# WebSocket server setup to send the data
async def start_sender():
    print("Starting WebSocket server...")
    async with websockets.serve(send_data, "localhost", 8766):
        print("WebSocket server is running on ws://localhost:8766")
        await asyncio.Future()  # Run forever

# Main execution function
if __name__ == "__main__":
    # Step 1: Clone the repository
    repository_url = "https://github.com/Murari-ch/heart-health-prediction-.git"
    destination_dir = r"D:\wallpapers\eshwar reddy\ML_PROJECTS\pythonProject2\clone_files_2"
    clone_repository(repository_url, destination_dir)

    # Step 2: Start the WebSocket server to send the cloned files
    asyncio.run(start_sender())
