import os
import shutil
import time
from datetime import datetime, timedelta

def copybara(source, destination, delay_seconds=0):  # 12 hours = 43200 seconds
    """
    Copies each subdirectory and file from the source to the destination with a delay between each copy,
    ignoring system/hidden files.

    :param source: The source directory containing subdirectories and files to copy.
    :param destination: The destination directory where subdirectories and files will be copied.
    :param delay_seconds: Delay between copying each item, in seconds. Default is 43200 seconds (12 hours).
    """

    print(f"\n\n***************************************************************************")
    print(f"***************************************************************************")
    print(f"***************************************************************************")
    print(f"======================Version 2.0, February 5, 2024========================")

    print(f"     _____  ____   _____ __     __ ____            _____")            
    print(f"    / ____|/ __ \\ |  __ \\\\ \\   / /|  _ \\    /\\    |  __ \\     /\\")    
    print(f"   | |    | |  | || |__) |\\ \\_/ / | |_) |  /  \\   | |__) |   /  \\")   
    print(f"   | |    | |  | ||  ___/  \\   /  |  _ <  / /\\ \\  |  _  /   / /\\ \\")  
    print(f"   | |____| |__| || |       | |   | |_) |/ ____ \\ | | \\ \\  / ____ \\")
    print(f"    \\_____|\____/ |_|       |_|   |____//_/    \\_\\|_|  \\_\\/_/    \\_\\\n")

    print(f"=========================Written by Colin Stokes===========================")
    print(f"***************************************************************************")
    print(f"***************************************************************************")
    print(f"***************************************************************************\n")
    
    # Ensure the source directory exists
    if not os.path.exists(source):
        print(f"Source directory {source} does not exist.\n")
        return
    
    # Ensure the source is actually a directory
    if not os.path.isdir(source):
        print(f"Source path {source} is not a directory.\n")
        return

    # Ensure the destination directory exists, create if it doesn't
    if not os.path.exists(destination):
        os.makedirs(destination)
        print(f"Destination directory {destination} was created.\n")

    items_to_copy = sorted(os.listdir(source))  # Sort items alphabetically to ensure a consistent order

    # Filter out system/hidden files like .DS_Store
    items_to_copy = [item for item in items_to_copy if not item.startswith('.')]

    if not items_to_copy:
        print("No items to copy. Exiting.\n")
        return
    
    item_count = 0

    for item in items_to_copy:
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)
        
        if os.path.isdir(source_item):
            if not os.path.exists(destination_item):
                try:
                    #print(f"Initiatied at {(datetime.now()).strftime('%I:%M:%S %p on %A, %B %d, %Y')}.")
                    print(f"COPYING DIRECTORY at {(datetime.now()).strftime('%I:%M:%S %p on %A, %B %d, %Y')}:\n==================\n{source_item}\n>>>to>>>\n{destination_item}\n==================")
                    shutil.copytree(source_item, destination_item)
                    item_count += 1
                    print(f"Completed at {(datetime.now()).strftime('%I:%M:%S %p on %A, %B %d, %Y')}.\n\n")

                except Exception as e:
                    print(f"Failed to copy {source_item} to {destination_item}. Error: {e}\n\n")
            else:
                print(f"Destination directory {destination_item} already exists. Skipping...\n\n")
        else:
            if not os.path.exists(destination_item):
                try:
                    start_time = (datetime.now())
                    #print(f"Initiatied at {(datetime.now()).strftime('%I:%M:%S %p on %A, %B %d, %Y')}.")
                    print(f"COPYING FILE at {(datetime.now()).strftime('%I:%M:%S %p on %A, %B %d, %Y')}:\n==================\n{source_item}\n>>>to>>>\n{destination_item}\n==================")
                    shutil.copy2(source_item, destination_item)
                    item_count += 1
                    print(f"Completed at {(datetime.now()).strftime('%I:%M:%S %p on %A, %B %d, %Y')}.\n\n")

                except Exception as e:
                    print(f"Failed to copy {source_item} to {destination_item}. Error: {e}\n\n")
            else:
                print(f"Destination file {destination_item} already exists. Skipping...\n\n")
        if delay_seconds > 0:
            next_copy_time = datetime.now() + timedelta(seconds=delay_seconds)
            print(f"Waiting for {delay_seconds / 3600:.4f} hours... \nNext copy will begin at {(datetime.now() + timedelta(seconds=delay_seconds)).strftime('%I:%M:%S %p on %A, %B %d, %Y')}.\n\n")
            time.sleep(delay_seconds)
        
        
    print(f"Successfully copied {item_count} items.\n\n")


if __name__ == "__main__":
    source_dir = "/Users/colinstokes/Desktop/folder_01"
    destination_dir = "/Users/colinstokes/Desktop/folder_02"
    delay_hours = 0  # How long to wait between copies, in hours
    delay_seconds = delay_hours * 3600  # Convert hours to seconds for the delay

    copybara(source_dir, destination_dir, delay_seconds)
