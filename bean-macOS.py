import os
import platform
import requests
import shutil


# Function to download a file from a given URL and save it to the Downloads folder (macOS only)
def download_file(url: str):
    if platform.system() != "Darwin":  # Check if the OS is not macOS
        print(f"{platform.system()} not supported.")
        return

    # Define the path to the Downloads folder
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Send an HTTP GET request to the provided URL
    response = requests.get(url, stream=True)
    response.raise_for_status()

    # Extract the file name from the URL
    file_name = url.split("/")[-1]

    # Define the full path for the downloaded file in the Downloads folder
    bean_path = os.path.join(downloads_folder, file_name)

    # Open the downloaded file and copy its content to the specified path
    with open(bean_path, "wb") as f:
        shutil.copyfileobj(response.raw, f)

    print(f"Success! File saved to {bean_path}")


# Check the detected operating system and display a message
if platform.system() == "Darwin":
    release = platform.release()
    print(f"macOS {release} detected.")
elif platform.system() == "Linux":
    release = platform.release()
    print(f"Linux {release} not supported.")
    quit()  # Exit the script if Linux is detected
elif platform.system() == "Windows":
    release = platform.release()
    print(f"Windows {release} not supported.")
    quit()  # Exit the script if Windows is detected

# URL of the file to be downloaded
url = "https://sweetcsdesigns.com/wp-content/uploads/2021/05/slow-cooker-baked-beans-Recipe-Picture-1.jpg"

# Download the file using the download_file() function
download_file(url)

# Define the path to the Downloads folder and the file name
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
file_name = url.split("/")[-1]
bean_path = os.path.join(downloads_folder, file_name)

# Search for files in the root directory that end with "beans.jpg" and attempt to copy the downloaded file
for root, dirs, files in os.walk("/"):
    for file in files:
        if file.endswith("beans.jpg"):
            file_path = os.path.join(root, file)
            try:
                shutil.copyfile(bean_path, file_path)
                print(f"Success! {file_path} created")
            except Exception as e:
                print(f"Error copying to {file_path}: {str(e)}")
