import os
import shutil

source_file = 'README.md'
current_dir = os.getcwd()

for root, dirs, files in os.walk(current_dir):
    for dir in dirs:
        dest_path = os.path.join(root, dir)
        shutil.copy(source_file, dest_path)
