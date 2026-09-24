import os, sys
from stat import *

def get_files_info(working_directory, directory="."): 
    working_dir_abs = os.path.abspath(os.getcwd())
    print("Working dir: " + working_dir_abs)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    print("Target dir: " + target_dir)

    #check if there is a valid common dir (should be a value larger than '/')
    valid_common_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if directory == ".":
        print("Result for current directory: ")
    else:
        print(f"Result for '{directory}' directory: ")

    
    if not os.path.isdir(directory): 
        print(f'    Error: "{directory}" is not a directory')

    if not valid_common_dir:
        print(f'    Error: Cannot list "{directory}" as it is outside the permitted working directory')
    else: 
        print(f'    Success: "{directory}" is within the working directory')
        # walk the dir 

        for f in os.listdir(directory): 
            pathname = os.path.join(directory, f)
            if os.path.isdir(directory): 
                print(f'    - {f}: file_size={os.path.getsize(f)}, is_dir={os.path.isdir(f)}')
            else: 
                print(f'    - {f}: file_size={os.path.getsize(f)}, is_dir={os.path.isdir(f)}')
