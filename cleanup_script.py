#!/bin/python3

###Note Before You Proceed Please Backup The Data
import os
import time

def cleanup_old_files(directory, days_threshold):
    ####Convert days into seconds####
    seconds_threshold = days_threshold * 24 * 60 * 60
    ####Get The time####
    current_time = time.time()

    deleted_files_count = 0 #Counter for deleted files
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            ##Check the last modified time of the file
            file_mod_time = os.path.getmtime(file_path)
            file_age = current_time - file_mod_time

            if file_age > seconds_threshold:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
                deleted_files_count += 1
    return deleted_files_count

if __name__ == '__main__':
    directory_old_files './sample_dir'
    days_to_keep = 30
    deleted_count = cleanup_old_files(directory_to_cleanup, days_to_keep)
    print(f"Total files deleted: {deleted_count}")
        

