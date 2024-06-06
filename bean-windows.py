import os
import platform
import win32api
import shutil

# Define image path within the repository
image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "beans.jpg")

# Check if the current platform is Windows
if platform.system() == "Windows":
    release = platform.release()
    if release:
        print(f"Windows {release} detected.")
    else:
        print("Windows detected, but release can't be determined.")
else:
    # Print a message if the platform is not supported and exit the script
    print(f"{platform.system()} not supported.")
    quit()

# Get a list of available drives on the system
get_drives = win32api.GetLogicalDriveStrings()
list_of_drives = get_drives.split("\x00")
drive_list = [drive for drive in list_of_drives if drive]

# Copy the image to specified locations on available drives
for drive in drive_list:
    if os.path.isdir(drive):
        file_path = os.path.join(drive, "beans.jpg")
        try:
            shutil.copyfile(image_path, file_path)
            print(f"Success! {file_path} created")
        except Exception as e:
            print(f"Error occurred while copying to {file_path}: {e}")
    else:
        print(f"{drive} is not a valid drive.")

print("Finished copying image.")
