# Bean Dumper

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

This Python script is created solely for the purpose of testing my Python knowledge and is not intended to cause any harm or perform any malicious actions. It performs various operations related to file downloads and copying files to locations on available drives. Please note that this script is only supported on Windows and may not work on other operating systems.

## Requirements

- Python 3.x
- The `pywin32` module for Windows (install it using `pip install pywin32`)
- The `requests` module (install it using `pip install requests`)

## Usage

1. Ensure you have the required modules installed (pywin32 and requests).
2. Run the script using a Python interpreter.

## Script Overview

The script performs the following actions:

1. Checks the operating system and displays a message. It is designed to run on Windows and may not work on Linux or macOS.
2. Downloads a file from a specified URL and saves it to the user's Downloads folder on Windows.
3. Retrieves a list of available drives on Windows.
4. Copies the downloaded file to locations on available drives where files named "beans.jpg" are found.

## Caution

This script is intended for non-malicious purposes only. It copies files to specific locations on available drives and may overwrite existing files named "beans.jpg." Exercise caution when running the script to avoid unintended data loss.

**Note:** The URLs used in this script are examples and may not be available at the time of execution. Update the URLs as needed.

Please use this script responsibly and ensure that it is not used for any malicious purposes.
