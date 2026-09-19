# Setup 

## Prerequisites
- Python 3.8 or later

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

caffeinate -di python3 script.py

- Every new CSV in `A/` is read and scanned against the terms defined in `TAGS` near the top of the script.
- A tagged copy of each new file is written to `B/` with a `tags` column added, semicolon-separated where more than one tag applies to a row.
- A tally of every tag and term across **all** transcripts currently in `B/` is written to `C/tag_tally.csv` (alphabetical by tag, then by term count within each tag) and printed to the terminal in the same order.

## Where the tags column lands
The `tags` column is inserted into the rightmost empty column of each file in `A/` — usually column D, but if a file already has data further out (e.g. an existing notes column), it lands in E or F automatically.

## Lower case all output in the B Folder in only the tags and terms columns

for f in B/*.csv; do
  python3 -c "
import pandas as pd
import sys

path = sys.argv[1]
df = pd.read_csv(path, encoding='utf-8', quotechar='\"', escapechar='\\\\')
for col in ('tags', 'terms'):
    if col in df.columns:
        df[col] = df[col].fillna('').astype(str).str.lower()
df.to_csv(path, index=False)
" "$f"
done
