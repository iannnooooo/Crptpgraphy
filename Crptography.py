from cryptography.fernet import Fernet
from PIL import Image
import os

# Provide the encryption key (use the key from the encryption step)
key_hex = "YOUR_ENCRYPTION_KEY_HEX"
key = Fernet(key_hex.encode())

# Define the folder containing the encrypted pictures you want to decrypt
input_folder = "encrypted_pictures"

# Define the folder where you want to save the decrypted pictures
output_folder = "decrypted_pictures"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all files in the input folder
files = os.listdir(input_folder)

for file in files:
    input_path = os.path.join(input_folder, file)
    output_path = os.path.join(output_folder, file)

    # Read the encrypted data from the input file
    with open(input_path, "rb") as input_file:
        encrypted_data = input_file.read()

    # Decrypt the encrypted data
    decrypted_data = key.decrypt(encrypted_data)

    # Create an image from the decrypted bytes and save it
    image = Image.frombytes("RGB", (500, 500), decrypted_data)
    image.save(output_path)

print("Decryption completed.")