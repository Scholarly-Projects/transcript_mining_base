# Setup Guide for Running script.py on macOS and Windows

## Prerequisites
Ensure that you have the following installed on your system:
- Python 3.8 or later ([Download Python](https://www.python.org/downloads/))
- pip (included with Python installation)
- Git (optional but recommended)

### Check if Python is Installed
Run the following command in your terminal or command prompt:
```sh
python --version
```
or
```sh
python3 --version
```
If Python is not installed, download and install it from the link above.

---

# Activate the virtual environment
# On macOS/Linux:
source myenv/bin/activate

# On Windows:
myenv\Scripts\activate
```

---

## Installing Dependencies
Once the virtual environment is activated, install the required Python packages by running:
```sh
pip install pandas nltk textblob
```

Additionally, download the necessary NLTK stopwords dataset:
```sh
python -c "import nltk; nltk.download('stopwords')"
```

---

## Configuring the CSV File Directory

By default, `script.py` expects CSV files to be in the following directory on Windows:
```
C:\Users\aweymouth\Documents\Github\transcript_mining_base\CSV
```
If you are on macOS, update the `directory` variable inside `script.py` to match your folder structure. For example:
```python
directory = "/Users/yourusername/Documents/Github/transcript_mining_base/CSV"
```
Ensure that all the CSV files required by the script are placed inside this folder.

---

## Running the Script
With all dependencies installed and the CSV files in place, run the script using:
```sh
python script.py
```
If using a virtual environment, ensure it is activated before running the command.

---

## Troubleshooting

### 3. File Path Errors on macOS
Ensure that file paths use forward slashes (`/`) instead of backslashes (`\`) on macOS.


