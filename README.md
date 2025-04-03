# Python.org Events Scraper

## Overview
This project uses Selenium to scrape upcoming event data from [python.org](https://www.python.org/events/). It extracts event names and dates, storing them in a nested Python dictionary.

## Prerequisites
Ensure you have the following installed before running the script:
- Python (>= 3.7)
- Google Chrome (latest version)
- ChromeDriver (compatible with your Chrome version)
- Selenium

## Installation
1. **Install Selenium**
   ```bash
   pip install selenium
   ```
2. **Download ChromeDriver**
   - Check your Chrome version: Open `chrome://version/`
   - Download the corresponding ChromeDriver from [here](https://sites.google.com/chromium.org/driver/)
   - Place the downloaded `chromedriver` in your system's PATH or specify its path in the script.

## Usage
1. **Run the Script**
   ```bash
   python scrape_python_events.py
   ```
2. **Expected Output**
   ```python
   [
       {"name": "PyCon US 2025", "time": "April 19, 2025"},
       {"name": "DjangoCon Europe 2025", "time": "May 21, 2025"},
       ...
   ]
   ```

## How It Works
- Opens the Python Events page using Selenium.
- Finds all event elements.
- Extracts event names and dates.
- Stores them in a list of dictionaries.
- Prints the structured event data.

## Notes
- The script automatically closes the browser after execution.
- You can modify the script to save the extracted data to a file.

## License
This project is open-source under the MIT License.

