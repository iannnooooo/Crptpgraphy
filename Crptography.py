from cryptography.fernet import Fernet
from PIL import Image
import os

# Generate a random encryption key
key = Fernet.generate_key()
fernet = Fernet(key)

# Define the folder containing the pictures you want to encrypt
input_folder = "input_pictures"

# Define the folder where you want to save the encrypted pictures
output_folder = "encrypted_pictures"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all files in the input folder
files = os.listdir(input_folder)

for file in files:
    input_path = os.path.join(input_folder, file)
    output_path = os.path.join(output_folder, file)

    # Open the image using Pillow
    image = Image.open(input_path)

    # Convert the image to bytes
    image_bytes = image.tobytes()

    # Encrypt the image bytes
    encrypted_data = fernet.encrypt(image_bytes)

    # Save the encrypted data to the output folder
    with open(output_path, "wb") as output_file:
        output_file.write(encrypted_data)

print("Encryption completed.")
print(f"Encryption key: {key.hex()}")
