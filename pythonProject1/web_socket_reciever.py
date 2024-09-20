import asyncio
import websockets
import os

# Define the allowed file extensions
ALLOWED_EXTENSIONS = ('.py', '.txt', 'README.md')

# WebSocket client function to receive and save the repository data
async def receive_repo_data():
    uri = "ws://localhost:8765"  # WebSocket server URI
    async with websockets.connect(uri) as websocket:
        repo_data_str = await websocket.recv()  # Receive the data
        repo_data = eval(repo_data_str)  # Convert string back to dictionary

        # Display all received files
        print("Received files from the server:")
        for file_path in repo_data.keys():
            print(f"- {file_path}")

        # Save the received files locally
        save_path = r"D:\wallpapers\eshwar reddy\ML_PROJECTS\pythonProject1\received_files"  # Specify where to save the repo data

        # Ensure the save directory exists
        os.makedirs(save_path, exist_ok=True)

        for file_path, file_content in repo_data.items():
            # Check if the file has an allowed extension
            if file_path.endswith(ALLOWED_EXTENSIONS):
                local_file_path = os.path.join(save_path, os.path.basename(file_path))
                try:
                    with open(local_file_path, 'w', encoding='utf-8') as f:  # Use utf-8 encoding
                        f.write(file_content)
                    print(f"Saved: {local_file_path}")
                except Exception as e:
                    print(f"Error writing to file {local_file_path}: {e}")
            else:
                print(f"Skipped: {file_path} (not an allowed file type)")

        print("Repository data saved locally.")

# Start the WebSocket client
asyncio.run(receive_repo_data())
