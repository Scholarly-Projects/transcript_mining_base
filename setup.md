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
pip install pandas nltk
```

---

## Format CSVs for Text Mining

In Apps Script:

function downloadSheetsAsCSV() {
  // Specify the folder ID of the folder containing the Google Sheets
  var folderId = 'folder-id';  // Replace with your folder ID
  var folder = DriveApp.getFolderById(folderId);
  var files = folder.getFiles();
  
  // Loop through each file in the folder
  while (files.hasNext()) {
    var file = files.next();
    
    // Check if the file is a Google Sheet
    if (file.getMimeType() === MimeType.GOOGLE_SHEETS) {
      var spreadsheet = SpreadsheetApp.openById(file.getId());
      var sheets = spreadsheet.getSheets();
      
      // Loop through all sheets and download each as CSV
      for (var i = 0; i < sheets.length; i++) {
        var sheet = sheets[i];
        var csv = convertSheetToCSV(sheet);
        
        // Create a new CSV file in the same folder
        var csvFile = folder.createFile(sheet.getName() + '.csv', csv, MimeType.CSV);
        Logger.log('Downloaded: ' + csvFile.getName());
      }
    }
  }
}

function convertSheetToCSV(sheet) {
  var data = sheet.getDataRange().getValues();
  
  // Find the index of the "words" column and replace it with "text"
  var headerRow = data[0];
  var wordsIndex = headerRow.indexOf('words');  // Locate the "words" column index
  
  if (wordsIndex !== -1) {
    headerRow[wordsIndex] = 'text';  // Change "words" to "text"
  }
  
  // Start building the CSV with the header row
  var csv = 'text\n';
  
  // Loop through rows and extract the "words" column, removing line breaks
  for (var i = 1; i < data.length; i++) {  // Start from 1 to skip the header row
    var row = data[i];
    
    // Extract the "words" column (index of "words" column)
    var cell = row[wordsIndex];
    
    // Remove all line breaks (carriage returns, newlines, etc.) within the "words" data
    if (typeof cell === 'string') {
      cell = cell.replace(/(\r\n|\n|\r)/gm, ' ');  // Replace all line breaks with space
      cell = cell.replace(/[^\w\s,.'"-]/g, '');  // Remove punctuation except for some valid ones
    }
    
    // Enclose the text in quotes to avoid column splitting due to commas
    cell = '"' + cell + '"';
    
    // Add the cleaned "text" to the CSV output
    csv += cell + '\n';
  }
  
  return csv;
}


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

To extract CSV file names from a Drive folder, use this Apps Script:

function listFilesInFolder() {
    var folderId = "folder-id";  // Replace with your actual folder ID
    var folder = DriveApp.getFolderById(folderId);
    var files = folder.getFiles();
    var fileNames = [];
    
    while (files.hasNext()) {
        var file = files.next();
        fileNames.push(file.getName());
    }
    
    Logger.log(fileNames.join("\n"));
}

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

---

## Connecting Individual Transcripts to Tag Sheet

In the transcript, enter the Apps Script extension and enter:

function fillTags() {
  // Get the active spreadsheet
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  
  // Get the transcript sheet by name
  var transcriptSheet = spreadsheet.getSheetByName("transcript_name");
  if (!transcriptSheet) {
    Logger.log("Transcript sheet not found");
    return;
  }
  
  // Get the tags spreadsheet by URL
  var tagsSpreadsheet = SpreadsheetApp.openByUrl("tag_sheet_url");
  if (!tagsSpreadsheet) {
    Logger.log("Tags spreadsheet not found");
    return;
  }
  
  // Get the tags sheet within the tags spreadsheet
  var tagsSheet = tagsSpreadsheet.getSheetByName("tags");
  if (!tagsSheet) {
    Logger.log("Tags sheet not found");
    return;
  }
  
  // Get the range of the transcript column
  var transcriptRange = transcriptSheet.getRange("D1:D" + transcriptSheet.getLastRow());
  var transcriptValues = transcriptRange.getValues();
  
  // Get the range of example words and tags in the tags sheet
  var exampleWordsRange = tagsSheet.getRange("B2:B" + tagsSheet.getLastRow());
  var tagsRange = tagsSheet.getRange("A2:A" + tagsSheet.getLastRow());
  var exampleWordsValues = exampleWordsRange.getValues();
  var tagsValues = tagsRange.getValues();
  
  // Create a map of example words to tags
  var tagsMap = {};
  for (var i = 0; i < exampleWordsValues.length; i++) {
    var word = exampleWordsValues[i][0].toLowerCase();
    var tag = tagsValues[i][0];
    tagsMap[word] = tag;
  }
  
  // Initialize an array to store the tags for each transcript entry
  var transcriptTags = [];
  
  // Loop through each transcript entry
  for (var i = 0; i < transcriptValues.length; i++) {
    var text = transcriptValues[i][0];
    var uniqueTags = [];
    
    if (typeof text === 'string') {
      // Use regular expression to extract words and handle punctuation
      var words = text.match(/\b\w+['-]?\w*|\w+['-]?\w*\b/g);
      
      // Check each word in the transcript entry against the tags map
      if (words) {
        for (var j = 0; j < words.length; j++) {
          var word = words[j].toLowerCase().replace(/[.,!?;:()]/g, '');
          if (tagsMap.hasOwnProperty(word) && !uniqueTags.includes(tagsMap[word])) {
            uniqueTags.push(tagsMap[word]);
          }
        }
      }
    }
    
    // Add the determined tags to the array
    transcriptTags.push([uniqueTags.join(";")]);
  }
  
  // Get the range of the tags column in the transcript sheet
  var tagsColumn = transcriptSheet.getRange("E1:E" + transcriptTags.length);
  
  // Set the values in the tags column to the determined tags
  tagsColumn.setValues(transcriptTags);
}
