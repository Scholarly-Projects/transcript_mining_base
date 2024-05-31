import pandas as pd
import string
from nltk.corpus import stopwords
from collections import Counter
import re
from textblob import TextBlob

# Download NLTK stopwords data
import nltk
nltk.download('stopwords')

# Define preprocess_text function
def preprocess_text(text):
    if isinstance(text, str):  # Check if text is a string
        text = re.sub(r'\b\w{1,4}\b', '', text)  # Remove short words (length <= 4)
        text = text.translate(str.maketrans('', '', string.punctuation)) 
        text = text.lower()  # Convert text to lowercase
    else:
        text = ''  # Replace NaNs with an empty string
    return text

# Load stopwords for both Spanish and English
stop_words_spanish = set(stopwords.words('spanish'))
stop_words_english = set(stopwords.words('english'))

# Combine both sets of stopwords
stop_words = stop_words_spanish.union(stop_words_english)

import os

# Directory containing CSV files
directory = 'C:\\Users\\aweymouth\\Documents\\Github\\transcript_mining_RWHP\\CSV'

# List of CSV file names
file_names = [
    'rwhp070.csv',
    'rwhp075.csv',
    'rwhp079.csv',
    'rwhp083.csv',
    'rwhp088.csv',
    'rwhp109.csv',
    'rwhp123.csv',
    'rwhp174.csv',
    'rwhp225.csv',
    'rwhp261.csv',
    'rwhp277.csv',
    'rwhp297.csv',
    'rwhp320.csv',
    'rwhp323.csv',
    'rwhp378.csv',
    'rwhp385.csv',
    'rwhp410.csv',
    'rwhp418.csv',
    'rwhp420.csv',
    'rwhp421.csv',
    'rwhp422.csv',
    'rwhp425.csv',
    'rwhp426.csv',
    'rwhp427.csv'
]

# Construct file paths using os.path.join()
file_paths = [os.path.join(directory, file_name) for file_name in file_names]

# Load and concatenate text data from all dataframes into a single corpus
corpus = ''
for file_path in file_paths:
    df = pd.read_csv(file_path, encoding='utf-8')
    text_series = df['text'].fillna('').astype(str).str.lower().str.strip()  # Extract and preprocess text column
    corpus += ' '.join(text_series) + ' '  # Concatenate preprocessed text with space delimiter

# Preprocess the entire corpus
cleaned_corpus = preprocess_text(corpus)

# Remove stopwords from the corpus
filtered_words = [word for word in cleaned_corpus.split() if word not in stop_words and len(word) >= 5]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Get top 100 most frequent distinctive words with occurrences
top_distinctive_words = word_freq.most_common(100)

# Print the top 100 most frequent distinctive words
for word, freq in top_distinctive_words:
    print(f'{word}: {freq}')
