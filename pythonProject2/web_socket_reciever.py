import asyncio
import websockets
import json
import os

# Define the directory where files will be saved
SAVE_DIR = r"D:\wallpapers\eshwar reddy\ML_PROJECTS\pythonProject2\received_files"

# Ensure the save directory exists
os.makedirs(SAVE_DIR, exist_ok=True)

# Function to receive data through the WebSocket
async def receive_data():
    # Connect to the WebSocket server where the sender is running
    uri = "ws://localhost:8766"
    async with websockets.connect(uri) as websocket:
        # Wait to receive the data from the sender
        received_data = await websocket.recv()

        # Convert the received text back into a usable format
        data_as_dict = json.loads(received_data)

        # Print the received API key
        print("API Key:", data_as_dict["key"])

        # Iterate through the received files and save them locally
        print("Saving received files...")
        for file_name, content in data_as_dict["files"].items():
            # Create the full path for each file
            file_path = os.path.join(SAVE_DIR, file_name)

            # Save (or overwrite) the file content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                print(f"Updated: {file_path}")

            # Print the content of the saved file
            print(f"\n--- Content of {file_name} ---\n{content}\n")

        print("All files have been saved and updated if they already existed.")

# Run the receiver WebSocket
asyncio.run(receive_data())
