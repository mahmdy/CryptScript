import os
import shutil
from cryptography.fernet import Fernet

# Read the encryption key from the 'key' file
with open('key', 'rb') as key_file:
    encryption_key = key_file.read()

# Remove the 'key' file
# os.remove('key')

# Create an instance of the encryption cipher
cipher = Fernet(encryption_key)

# Get the current directory
current_directory = os.getcwd()

# Iterate over all files in the directory
for root, dirs, files in os.walk(current_directory):
    for file in files:
        # Exclude the script file and key file (if they exist) from decryption
        if file != 'decrypt_files.py' and file != 'key':
            file_path = os.path.join(root, file)

            # Read the file content
            with open(file_path, 'rb') as input_file:
                content = input_file.read()

            try:
                # Decrypt the file content
                decrypted_content = cipher.decrypt(content)

                # Write the decrypted content back to the file
                with open(file_path, 'wb') as output_file:
                    output_file.write(decrypted_content)
            except Exception as e:
                print(f"Error decrypting {file_path}: {str(e)}")
