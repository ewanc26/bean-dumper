# Bean Dumper

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

Test script for learning Python. Windows only. Downloads files and copies them to available drives.

## Requirements

- Python 3.x
- `pywin32` (`pip install pywin32`)
- `requests` (`pip install requests`)

## Usage

```bash
pip install pywin32 requests
python bean-dumper.py
```

## What it does

1. Checks the OS (Windows only, won't work on Linux/macOS)
2. Downloads a file from a URL to your Downloads folder
3. Finds available drives
4. Copies the file to drives that already have files named `beans.jpg`

**Note:** URLs in the script are examples — update them. The script can overwrite existing `beans.jpg` files.

## Licence

MIT
