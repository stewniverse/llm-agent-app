import os

def get_files_info(working_directory, directory="."): 
    working_dir_abs = os.path.abspath(os.getcwd())
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    # find the common directoty 
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if valid_target_dir == False:
        f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    # iterate over each item in the directory
    dir_list = os.listdir(directory)
    dir_list.sort()
    for item in dir_list:
        print(item)
        #  +": " +"file_size="+ str(os.stat(item).st_size)+"bytes, is_dir="
        # str(os.DirEntry.is_dir(item)