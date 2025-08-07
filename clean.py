#!/usr/bin/python3
import os

# Get the current working directory
root_dir = os.getcwd()

# Walk through all directories and files
for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith('.pem'):
                file_path = os.path.join(dirpath, file)
                try:
                 os.remove(file_path)
                 print(f"Deleted: {file_path}")
                except Exception as e:
                 print(f"Failed to delete {file_path}: {e}")
