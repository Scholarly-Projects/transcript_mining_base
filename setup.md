# Setup 

## Prerequisites
- Python 3.8 or later

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python3 script.py

- Every new CSV in `A/` is read and scanned against the terms defined in `TAGS` near the top of the script.
- A tagged copy of each new file is written to `B/` with a `tags` column added, semicolon-separated where more than one tag applies to a row.
- A tally of every tag and term across **all** transcripts currently in `B/` is written to `C/tag_tally.csv` (alphabetical by tag, then by term count within each tag) and printed to the terminal in the same order.

## Where the tags column lands
The `tags` column is inserted into the rightmost empty column of each file in `A/` — usually column D, but if a file already has data further out (e.g. an existing notes column), it lands in E or F automatically.
