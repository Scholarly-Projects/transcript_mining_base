import pandas as pd
import string
from nltk.corpus import stopwords
from collections import Counter
import re

# Download NLTK stopwords data
import nltk
nltk.download('stopwords')

# Define preprocess_text function
def preprocess_text(text):
    if isinstance(text, str):  # Check if text is a string
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
directory = "/Users/andrewweymouth/Documents/GitHub/transcript_mining_base/CSV"

# List of CSV file names
file_names = [
    'context_01.csv', 'context_02.csv', 'context_03.csv', 'context_04.csv', 'context_05.csv',
    'context_06.csv', 'context_07.csv', 'context_08.csv', 'context_09.csv', 'context_10.csv',
    'context_11.csv', 'context_12.csv', 'context_13.csv', 'context_14.csv', 'context_15.csv',
    'context_16.csv', 'context_17.csv', 'context_18.csv', 'context_19.csv', 'context_20.csv',
    'context_21.csv', 'context_22.csv', 'context_23.csv', 'context_24.csv', 'context_25.csv',
    'context_26.csv', 'context_27.csv', 'context_28.csv', 'context_29.csv', 'context_30.csv',
    'context_32.csv', 'context_34.csv', 'context_35.csv', 'context_36.csv', 'context_38.csv',
    'context_39.csv', 'context_40.csv', 'context_42.csv', 'context_44.csv', 'context_46.csv',
    'context_48.csv', 'context_49.csv', 'context_50.csv', 'context_51.csv', 'context_52.csv',
    'context_53.csv', 'context_55.csv', 'context_56.csv', 'context_57.csv', 'context_58.csv',
    'context_59.csv', 'context_60.csv', 'context_61.csv', 'context_62.csv', 'context_63.csv',
    'context_64.csv', 'context_66.csv', 'context_67.csv', 'context_68.csv', 'context_69.csv',
    'context_70.csv', 'context_71.csv', 'context_72.csv', 'context_73.csv', 'context_74.csv',
    'context_75.csv', 'context_76.csv', 'context_77.csv', 'context_78.csv', 'context_79.csv',
    'context_80.csv', 'context_81.csv', 'context_82.csv', 'context_83.csv', 'context_84.csv',
    'context_85.csv', 'context_86.csv', 'context_87.csv', 'context_88.csv', 'context_89.csv',
    'context_90.csv', 'context_91.csv', 'context_92.csv', 'context_93.csv', 'context_94.csv',
    'context_95.csv', 'context_96.csv', 'context_97.csv', 'context_98.csv', 'context_99.csv',
    'context_100.csv', 'context_101.csv', 'context_102.csv', 'context_103.csv', 'context_104.csv',
    'context_105.csv', 'context_106.csv', 'context_107.csv', 'context_108.csv', 'context_109.csv',
    'context_110.csv'
]

# Construct file paths using os.path.join()
file_paths = [os.path.join(directory, file_name) for file_name in file_names]

# Initialize an empty list to hold the DataFrames
dfs = []

# Try reading each CSV file and print which file is being processed
for file_path in file_paths:
    try:
        print(f"Processing: {file_path}")
        # Add quotechar and escapechar for handling CSVs with quotes
        dfs.append(pd.read_csv(file_path, encoding='utf-8', quotechar='"', escapechar='\\'))
    except Exception as e:
        print(f"Error with file {file_path}: {e}")

# Concatenate text data from all dataframes into a single corpus
corpus = ''
for df in dfs:
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

# === General Section ===



def find_agriculture_terms(corpus):
    # Define a list of agriculture-related terms
    agriculture_terms = [term.lower() for term in ["harvest", "tractor", "acreage", "crop", "livestock", "farm field", "barn building", "ranch", "garden", "orchard", "dairy", "cattle", "poultry", "farming equipment", "fertilizer", "seed", "irrigation", "plow", "farmhand", "hoe", "shovel", "milking", "hay", "silage", "compost", "weeding", "crop rotation", "organic", "gmo", "sustainable", "farming", "rural", "homestead", "grain crop", "wheat", "corn maize", "soybean", "potato", "apple fruit", "berry", "honey", "apiary", "pasture", "combine harvester", "trailer", "baler", "thresher"
    ]]

    # Initialize a Counter to tally occurrences of agriculture-related terms
    agriculture_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in agriculture_terms:
            agriculture_word_freq[word] += 1

    # Return the top 20 most common agriculture-related terms
    return agriculture_word_freq.most_common(20)

# Call the function to find agriculture-related terms in the corpus
top_agriculture_terms = find_agriculture_terms(corpus)

# Print the top 50 agriculture-related terms
print("## agriculture")
for word, count in top_agriculture_terms:
    print(f"{word}: {count}")



def find_animal_terms(corpus):
    # Define a list of the top fifty most common Spanish animal-related terms
    animal_terms = [term.lower() for term in ["moose", "Ewe", "horse", "salmon hatchery", "goat", "pig", "chicken", "turkey", "duck", "quail", "rabbit", "squirrel", "herd", "stag", "buck", "doe", "paw", "bear den", "cougars", "coyote", "wolves", "fox", "mountain lions", "raccoon", "skunk", "badger", "possum", "weasel", "ferret", "mink", "otter", "beaver", "muskrat", "marmot", "gopher", "prairie dog", "chipmunk", "bison", "buffalo", "lizard", "snake bite", "frog", "toad", "newt", "salamander", "owl", "hawk", "eagle", "raven", "crow", "sparrow", "finch", "bluebird", "squirrel", "lamb", "wolf pack", "whale pod", "Gaggle", "hawks", "steelhead", 
    ]]  # Add more as needed

    # Initialize a Counter to tally occurrences of animal terms
    animal_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in animal_terms:
            animal_word_freq[word] += 1

    # Return the top 20 most common animal terms
    return animal_word_freq.most_common(20)

# Call the function to find animal terms in the corpus
top_animal_terms = find_animal_terms(corpus)

# Print the top 150 animal terms
print("## wildlife")
for word, count in top_animal_terms:
    print(f"{word}: {count}")



def find_fashion_terms(corpus):
    # Define a list of fashion-related terms
    fashion_terms = [term.lower() for term in ["clothing", "fashion", "apparel", "outfit", "wardrobe", "jeans", "t-shirt", "sweater", "jacket", "skirt", "pants", "shoes", "boots", "sneakers", "hat", "cap", "scarf", "gloves", "socks", "underwear", "outerwear", "workwear", "uniform", "overalls", "apron", "denim", "flannel", "plaid", "cotton", "polyester", "fabric", "stitching", "seamstress", "tailor", "alterations", "thrift", "secondhand", "shopping", "retail", "department store"
    ]]

    # Initialize a Counter to tally occurrences of fashion-related terms
    fashion_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in fashion_terms:
            fashion_word_freq[word] += 1

    # Return the top 20 most common fashion-related terms
    return fashion_word_freq.most_common(20)

# Call the function to find fashion-related terms in the corpus
top_fashion_terms = find_fashion_terms(corpus)

# Print the top 50 fashion-related terms
print("## clothing")
for word, count in top_fashion_terms:
    print(f"{word}: {count}")



def find_conflict_terms(corpus):
    # Define a list of conflict-related terms
    conflict_terms = [term.lower() for term in ["war", "battle", "combat", "soldier", "military", "deployment", "combatant", "veteran", "casualty", "maim", "ptsd", "invasion", "military occupation", "resistance", "rebellion", "revolution", "mobilization", "genocide", "ethnic cleansing", "conscription", "alliance", "enemy", "foe", "ally", "peacekeeping", "ceasefire", "treaty", "negotiation", "diplomacy", "sanctions", "arms", "weapons", "missile", "bomb", "gunfire"
    ]]

    # Initialize a Counter to tally occurrences of conflict-related terms
    conflict_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in conflict_terms:
            conflict_word_freq[word] += 1

    # Return the top 20 most common conflict-related terms
    return conflict_word_freq.most_common(20)

# Call the function to find conflict-related terms in the corpus
top_conflict_terms = find_conflict_terms(corpus)

# Print the top 50 conflict-related terms
print("## conflict")
for word, count in top_conflict_terms:
    print(f"{word}: {count}")
  


def find_crime_terms(corpus):
    # Define a list of the top fifty most common Spanish crime-related terms
    crime_terms = [term.lower() for term in ["crime", "violence", "theft", "robbery", "burglary", "assault", "homicide", "murder", "rape", "domestic violence", "gangs", "drugs", "trafficking", "possession", "distribution", "addiction", "prostitution", "gambling", "corruption", "bribery", "fraud", "embezzlement", "extortion", "racketeering", "money laundering", "forgery", "identity theft", "cybercrime", "vandalism", "arson", "illegal immigration", "detention", "arrest", "interrogation", "trial", "plea bargain", "conviction", "sentencing", "imprisonment", "probation", "parole", "rehabilitation", "recidivism", "police", "detective", "officer", "investigation", "forensics"
    ]]

    # Initialize a Counter to tally occurrences of crime terms
    crime_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in crime_terms:
            crime_word_freq[word] += 1

    return crime_word_freq.most_common(20)

# Call the function to find crime terms in the corpus
top_crime_terms = find_crime_terms(corpus)

# Print the top 150 crime terms
print("## crime")
for word, count in top_crime_terms:
    print(f"{word}: {count}")



def find_culture_terms(corpus):
    # Define a list of culture-related terms
    culture_terms = [term.lower() for term in ["tradition", "folklore", "customs", "rituals", "celebration", "cuisine", "festivals", "dialect", "belonging", "neighborhood", "gathering", "gatherings", "socializing", "folktales", "legends", "crafts", "craftsmanship", "oral tradition", "ethnicity", "diversity", "inclusion", "community centers", "street fairs", "parades", "food trucks", "ethnic foods", "local traditions", "folk dance", "folk art", "cultural exchange", "cultural identity", "cultural pride", "multiculturalism", "ethnic neighborhoods"
    ]]

    # Initialize a Counter to tally occurrences of culture-related terms
    culture_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in culture_terms:
            culture_word_freq[word] += 1

    return culture_word_freq.most_common(20)

# Call the function to find culture-related terms in the corpus
top_culture_terms = find_culture_terms(corpus)

# Print the top 50 culture-related terms
print("## culture")
for word, count in top_culture_terms:
    print(f"{word}: {count}")



def find_economic_terms(corpus):
    # Define a list of the top fifty most common Spanish economic-related terms
    economic_terms = [term.lower() for term in ["great depression", "employment", "wage", "salary", "income", "paycheck", "earnings", "livelihood", "vocation", "profession", "skilled trade", "skill", "craftsman", "manual labor", "blue-collar", "white-collar", "layoff", "dismissal", "termination", "retrenchment", "redundancy", "job search", "job interview", "resume document", "cover letter", "application", "hiring", "apprenticeship", "promotion", "advancement", "salary increase", "employee benefits", "pension", "retirement", "savings", "investment", "budgeting", "financial planning", "debt", "credit loan", "loan", "mortgage"
    ]]

    # Initialize a Counter to tally occurrences of economic terms
    economic_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in economic_terms:
            economic_word_freq[word] += 1

    return economic_word_freq.most_common(20)

# Call the function to find economic terms in the corpus
top_economic_terms = find_economic_terms(corpus)

# Print the top 150 economic terms
print("## economy")
for word, count in top_economic_terms:
    print(f"{word}: {count}")



def find_education_terms(corpus):
    # Define a list of the top fifty most common Spanish education-related terms
    education_terms = [term.lower() for term in ["School", "Classroom", "Teacher", "Student", "Learning", "Literacy", "Numeracy", "Curriculum", "Assignment", "Homework", "Exam", "Test", "Grade", "Report card", "Diploma", "Degree", "Certificate", "academia", "scholarship", "Transcript", "Textbook", "Library", "Study", "Research", "Group work", "Peer review", "Tutoring", "Principal", "Administrator", "Counselor", "Resource center", "Special education", "Individualized education plan (IEP)", "Field trip", "Extracurricular", "Athletics", "Club", "Parent-teacher conference", "Back-to-school night", "Open house", "Graduation", "Prom", "Financial aid", "Scholarship", "Grant", "Loan", "Work-study program"
    ]] 

    # Initialize a Counter to tally occurrences of education terms
    education_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in education_terms:
            education_word_freq[word] += 1

    return education_word_freq.most_common(20)

# Call the function to find education terms in the corpus
top_education_terms = find_education_terms(corpus)

# Print the top 150 education terms
print("## education")
for word, count in top_education_terms:
    print(f"{word}: {count}")



def find_environment_terms(corpus):
    # Define a list of environment-related terms
    environment_terms = environment_terms = [term.lower() for term in ["Environment", "Nature", "Ecology", "Ecosystem", "Biodiversity", "Conservation", "Sustainability", "Climate", "Climate change", "Global warming", "Pollution", "Air pollution", "Water pollution", "Soil pollution", "Deforestation", "Habitat destruction", "Waste management", "Recycling", "Renewable energy", "Solar energy", "Wind energy", "Hydropower", "Geothermal energy", "Carbon footprint", "Greenhouse gases", "Ozone depletion", "Wildlife", "Endangered species", "Natural resources", "Land conservation", "Water conservation", "Energy efficiency", "Environmental impact", "Environmental policy", "Environmental regulation", "Environmental awareness", "Environmental education", "Environmental activism", "Sustainable development", "Urbanization", "Rural development", "Land use", "Land degradation", "Desertification", "Ocean conservation", "Marine life", "Coral reefs", "Sea level rise", "Water scarcity", "Drought", "Flood", "Natural disaster", "Ecotourism", "Green spaces", "Parks", "Forests", "Wetlands", "Mountains", "Rivers", "Lakes", "Oceans", "Beaches", "Glaciers", "Tundra", "Grasslands"
    ]] 

    # Initialize a Counter to tally occurrences of environment terms
    environment_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in environment_terms:
            environment_word_freq[word] += 1

    return environment_word_freq.most_common(20)

# Call the function to find environment terms in the corpus
top_environment_terms = find_environment_terms(corpus)

# Print the top 150 environment terms
print("## environment")
for word, count in top_environment_terms:
    print(f"{word}: {count}")



def find_family_terms(corpus):
    # Define a list of the top fifty most common Spanish family-related terms
    family_terms = [term.lower() for term in ["Parent", "Mother", "Father", "Child", "Sibling", "Brother", "Sister", "Grandparent", "Grandfather", "Grandmother", "Grandchild", "Cousin", "Aunt", "Uncle", "Nephew", "Niece", "Step-parent", "Step-sibling", "Step-brother", "Step-sister", "Stepchild", "Spouse", "Husband", "Wife", "Partner", "Boyfriend", "Girlfriend", "Fiance", "Fiancee", "Domestic partner", "Marriage", "Wedding", "Divorce", "Single parent", "Orphan", "Adoptive parent", "Adopted child", "Foster parent", "Foster child", "Guardian", "Legal guardian", "Custody", "Child support", "Family gathering", "Family dinner", "Family tradition"
    ]]  # Add more as needed

    # Initialize a Counter to tally occurrences of family terms
    family_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in family_terms:
            family_word_freq[word] += 1

    return family_word_freq.most_common(20)

# Call the function to find family terms in the corpus
top_family_terms = find_family_terms(corpus)

# Print the top 150 family terms
print("## family")
for word, count in top_family_terms:
    print(f"{word}: {count}")



def find_food_and_drink_terms(corpus):
    # Define a list of the top fifty most common Spanish food and drink terms
    food_and_drink_terms = [term.lower() for term in ["Beans", "Beef", "Pork", "Chicken", "Milk", "Bread", "Butter", "Eggs", "Cheese", "Apple", "Pie", "Peach", "Biscuit", "Coffee", "Tea", "Beer", "Whiskey", "Soda", "Soup", "Stew", "Salad", "Corn", "Wheat", "Barley", "Oats", "Onion", "Garlic", "Salt", "Pepper", "Lard", "Marmalade", "Honey", "Cider", "Vinegar", "Bacon", "Sausage", "Jerky", "Pickles", "Fruit spread", "Cake", "Cookies", "Doughnuts", "Ice cream", "Candy", "Chocolate", "Almonds", "Raisins"
    ]]

    # Initialize a Counter to tally occurrences of food and drink terms
    food_and_drink_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in food_and_drink_terms:
            food_and_drink_word_freq[word] += 1

    return food_and_drink_word_freq.most_common(20)

# Call the function to find food and drink terms in the corpus
top_food_and_drink_terms = find_food_and_drink_terms(corpus)

# Print the top 150 food and drink terms
print("## food and drink")
for word, count in top_food_and_drink_terms:
    print(f"{word}: {count}")



def find_health_terms(corpus):
    # Define a list of health-related terms
    health_terms = [term.lower() for term in ["doctor", "nurse", "hospital", "clinic", "medicine", "prescription", "insurance", "appointment", "check up", "emergency", "pharmacy", "surgery", "ambulance", "patient", "care", "treatment", "therapy", "recovery", "vaccine", "vaccination", "flu", "cold", "fever", "cough", "sore throat", "headache", "pain", "injury", "wound", "bandage", "cast", "physical therapy", "mental health", "diet plan", "workout", "body weight", "blood pressure", "cholesterol", "diabetes", "asthma", "allergy", "immunity", "virus", "bacteria", "healthcare"
    ]]

    # Initialize a Counter to tally occurrences of health-related terms
    health_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in health_terms:
            health_word_freq[word] += 1

    return health_word_freq.most_common(20)

# Call the function to find health-related terms in the corpus
top_health_terms = find_health_terms(corpus)

# Print the top 50 health-related terms
print("## health")
for word, count in top_health_terms:
    print(f"{word}: {count}")



def find_history_terms(corpus):
    # Define a list of history-related terms
    history_terms = [term.lower() for term in ["ancestors", "traditions", "lineage", "legacy", "ancestral", "heritage", "oral history", "ancestral home", "ancestral land", "pioneers", "settlers", "frontiersmen", "colonial", "revolutionary", "founding fathers", "historic sites", "historical landmarks", "ancestral knowledge", "historic preservation", "historical records", "local history", "family history", "explorers", "trailblazers", "historical events", "heritage sites", "cultural heritage", "community history", "historical artifacts", "historical society", "genealogy", "civil rights", "labor history", "historical documents", "archaeology", "historic buildings", "traditional crafts", "ancestral language"
    ]]

    # Initialize a Counter to tally occurrences of history-related terms
    history_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in history_terms:
            history_word_freq[word] += 1

    return history_word_freq.most_common(20)

# Call the function to find history-related terms in the corpus
top_history_terms = find_history_terms(corpus)

# Print the top 50 history-related terms
print("## history")
for word, count in top_history_terms:
    print(f"{word}: {count}")
    


def find_cinema_terms(corpus):
    # Define a list of the top fifty most common cinema-related terms
    cinema_terms = [term.lower() for term in [
        "Cinema", "Film", "Movie", "Screenplay", "Script", "Producer", 
        "Cinematography", "Editing", "Soundtrack", "Score", "Dialogue", "Actor", 
        "Actress", "Cast", "Crew", "Scene", "Shot", "Frame", "Close-up", "Long shot", 
        "Mid shot", "Wide shot", "Tracking shot", "Montage", "Climax", "Plot", 
        "Storyline", "Narrative", "Character", "Antagonist", "Protagonist", 
        "Screenwriter", "Camerawork", "Film noir", "Blockbuster", "Independent film", 
        "Silent film", "Documentary", "Mockumentary", "Animation", "Feature film", 
        "Short film", "Opening credits", "Closing credits", "Cameo", "Stunt", 
        "Special effects", "Visual effects", "Voice-over"
    ]]

    # Initialize a Counter to tally occurrences of cinema terms
    cinema_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in cinema_terms:
            cinema_word_freq[word] += 1

    return cinema_word_freq.most_common(20)

# Call the function to find cinema terms in the corpus
top_cinema_terms = find_cinema_terms(corpus)

# Print the top 150 cinema terms
print("## cinema")
for word, count in top_cinema_terms:
    print(f"{word}: {count}")
    


def find_literature_terms(corpus):
    # Define a list of the top fifty most common literature-related terms
    literature_terms = [term.lower() for term in [
        "Literature", "Novel", "Poetry", "Prose", "Fiction", "Nonfiction", "Narrative", 
        "Plot", "Theme", "Character", "Dialogue", "Metaphor", "Simile", 
        "Alliteration", "Allegory", "Symbolism", "Irony", "Foreshadowing", 
        "Flashback", "Epilogue", "Prologue", "Manuscript", "Draft", "Editing", 
        "Publishing", "Author", "Writer", "Playwright", "Essayist", "Verse", 
        "Sonnet", "Haiku", "Epic poem", "Free verse", "Short story", "Novella", 
        "Fable", "Mythology", "Folktale", "Biography", "Autobiography", 
        "Memoir", "Criticism", "Literary theory", "Genre fiction", "Classic literature", 
    ]]

    # Initialize a Counter to tally occurrences of literature terms
    literature_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in literature_terms:
            literature_word_freq[word] += 1

    return literature_word_freq.most_common(20)

# Call the function to find literature terms in the corpus
top_literature_terms = find_literature_terms(corpus)

# Print the top 150 literature terms
print("## literature")
for word, count in top_literature_terms:
    print(f"{word}: {count}")



def find_theater_terms(corpus):
    # Define a list of the top fifty most common theater-related terms
    theater_terms = [term.lower() for term in [
        "Theater", "Drama", "Comedy", "Melodrama", "Monologue", 
        "Stage", "Backstage", "Front stage", "Playwright", "Script", 
        "Blocking", "Dramaturgy", "Actor", 
        "Actress", "Cast", "Ensemble", "Understudy", "Set design", "Prop", 
        "Costume", "Lighting design", "Sound design", "Curtain call", "Matinee", 
        "Broadway", "Off-Broadway", "Box office", "Standing ovation", "Fourth wall", 
        "Break character", "Dress rehearsal", "Cold reading", "Soliloquy", 
        "Prologue", "Epilogue", "Improvisation", "Method acting", "Stage directions", 
        "Tech rehearsal", "House lights", "Exit stage", "Upstage"
    ]]

    # Initialize a Counter to tally occurrences of theater terms
    theater_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in theater_terms:
            theater_word_freq[word] += 1

    return theater_word_freq.most_common(20)

# Call the function to find theater terms in the corpus
top_theater_terms = find_theater_terms(corpus)

# Print the top 150 theater terms
print("## theater")
for word, count in top_theater_terms:
    print(f"{word}: {count}")



def find_music_terms(corpus):
    # Define a list of the top fifty most common music-related terms
    music_terms = [term.lower() for term in [
        "Music", "Melody", "Harmony", "Rhythm", "Tempo", "Dynamics", "Notation", 
        "Composition", "Improvisation", "Orchestration", "Counterpoint", "Cadence", 
        "Crescendo", "Decrescendo", "Timbre", "Chord", "Key signature", 
        "Time signature", "Interval", "Arpeggio", "Sight reading", "Ear training", 
        "Music theory", "Conducting", "Score study", "Vibrato", 
        "Resonance", "Acoustics", "Concert", "Recital", "Rehearsal", 
        "Ensemble", "Soloist", "Choir", "Orchestra", "Chamber music", "Woodwind", 
        "Brass instrument", "String instrument", "Percussion", "Piano technique", 
        "Guitar technique", "Vocal training", "Breath control", "Stage presence", 
        "Musical phrasing"
    ]]

    # Initialize a Counter to tally occurrences of music terms
    music_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in music_terms:
            music_word_freq[word] += 1

    return music_word_freq.most_common(20)

# Call the function to find music terms in the corpus
top_music_terms = find_music_terms(corpus)

# Print the top 150 music terms
print("## music")
for word, count in top_music_terms:
    print(f"{word}: {count}")




def find_indigenous_terms(corpus):
    # Define a list of indigenous-related terms specific to tribes of Idaho
    indigenous_terms = [term.lower() for term in ["Shoshone", "tribe", "reservation", "native american", "indigenous","Bannock", "Nez Perce", "Coeur d'Alene indian", "Kootenai", "Salish", "Spokane indian", "Shoshone-Bannock", "Fort Hall indian", "Lemhi", "Shoshone-Paiute", "Shoshoni", "Tukudeka", "Sheepeater", "Camas Prairie", "Nimíipuu", "Sahaptin", "Atsina", "Kalispel indian", "Pend d'Oreille", "Yakama indian", "Flathead", "Wenatchi", "Methow", "Entiat indian", "Chelan indian", "Sinkiuse-Columbia", "Wenatchee indian", "Palus", "Cayuse indian", "Umatilla indian", "Tenino indian", "Walla Walla indian", "Nez Percé", "Yakama indian", "Colville indian", "Coeur d'Alene indian", "Spokane indian", "Columbia indian", "Willamette Valley indian", "Clearwater indian", "Salmon River indian", "Payette indian", "Bruneau indian", "Owyhee", "Snake River indian", "Lemhi River indian"
    ]]

    # Initialize a Counter to tally occurrences of indigenous-related terms
    indigenous_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in indigenous_terms:
            indigenous_word_freq[word] += 1

    return indigenous_word_freq.most_common(20)

# Call the function to find indigenous-related terms in the corpus
top_indigenous_terms = find_indigenous_terms(corpus)

# Print the top 50 indigenous-related terms
print("## indigenous")
for word, count in top_indigenous_terms:
    print(f"{word}: {count}")
    


def find_mining_terms(corpus):
    # Define a list of the top fifty most common mining-related terms
    mining_terms = [term.lower() for term in [
        "Mining", "Ore", "Extraction", "Prospecting", "Drilling", "Blasting", 
        "Excavation", "Fracking", "hydraulic fracturing", "Tunneling", "Shaft sinking", "Open pit", "Underground mining", 
        "Strip mining", "Quarrying", "Mineral deposit", "Ore body", "Tailings", 
        "Mine reclamation", "Smelting", "Refining", "Flotation process", "Heap leaching", 
        "Hydrometallurgy", "Pyrometallurgy", "Drift mining", "Slope mining", 
        "Room and pillar", "Longwall mining", "Hard rock mining", "Placer mining", 
        "Dredging", "Coal seam", "Geological survey", "Assay", "Mine ventilation", 
        "Mine safety", "Explosive charge", "Miner's lamp", "Haul truck", "Conveyor belt", 
        "Ore grade", "Rock fragmentation", "Mining permit", "Extraction rate", 
        "Strip ratio", "Reclamation bond", "Processing plant", "Slurry", 
        "Geotechnical analysis", "Mine closure", "Environmental impact", "Mine drainage"
    ]]

    # Initialize a Counter to tally occurrences of mining terms
    mining_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in mining_terms:
            mining_word_freq[word] += 1

    return mining_word_freq.most_common(20)

# Call the function to find mining terms in the corpus
top_mining_terms = find_mining_terms(corpus)

# Print the top 150 mining terms
print("## mining")
for word, count in top_mining_terms:
    print(f"{word}: {count}")



def find_timber_terms(corpus):
    # Define a list of the top fifty most common timber-related terms
    timber_terms = [term.lower() for term in [
        "Timber", "Lumber", "Logging", "Forestry", "Sawing", "Felling", 
        "Deforestation", "Reforestation", "Sawmill", "Plywood", "Hardwood", "Softwood", 
        "Board foot", "Timberland", "Woodlot", "Log yard", "Milling process", "Kiln drying", 
        "Air drying", "Wood grain", "Lumber grading", "Plank", "Beam", "Log scaler", 
        "Chainsaw", "Skidder", "Debarking", "Pulpwood", "Chipboard", 
        "Veneer", "Crosscut", "Rip cut", "Lath", "Timber frame", "Wood treatment", 
        "Sustainable forestry", "Clear cutting", "Selective cutting", "Silviculture", 
        "Tree farm", "Stumpage", "Hectare yield", "Logging permit", "Timber stand", 
        "Tree felling", "Woodworker", "Wood processing", "Forest conservation", 
        "Wood preservation"
    ]]

    # Initialize a Counter to tally occurrences of timber terms
    timber_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in timber_terms:
            timber_word_freq[word] += 1

    return timber_word_freq.most_common(20)

# Call the function to find timber terms in the corpus
top_timber_terms = find_timber_terms(corpus)

# Print the top 150 timber terms
print("## timber")
for word, count in top_timber_terms:
    print(f"{word}: {count}")



def find_manufacturing_terms(corpus):
    # Define a list of the top fifty most common manufacturing-related terms
    manufacturing_terms = [term.lower() for term in [
        "Manufacturing", "Fabrication", "Assembly line", "Machining", 
        "Casting", "Forging", "Molding", "CNC machining", "Lean manufacturing", 
        "Quality control", "Process optimization", "Supply chain", "Raw materials", 
        "Industrial robotics", "Prototyping", "Batch production", "Mass production", 
        "Just-in-time", "Six Sigma", "Kaizen", "Additive manufacturing", "3D printing", 
        "Tooling", "Precision engineering", "Injection molding", "Extrusion", "Welding", 
        "Sheet metal", "Die casting", "Material handling", "Assembly process", 
        "Industrial safety", "Factory layout", "Workstation", "Operational efficiency", 
        "Machine calibration", "Inventory management", "Continuous improvement", 
        "Computer-aided design", "Computer-aided manufacturing", "Automation process", 
        "Labor productivity", "Quality assurance", "Standardization", "Lean process", 
        "Production planning", "Equipment maintenance", "Industrial engineering", 
        "Production workflow"
    ]]

    # Initialize a Counter to tally occurrences of manufacturing terms
    manufacturing_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in manufacturing_terms:
            manufacturing_word_freq[word] += 1

    return manufacturing_word_freq.most_common(20)

# Call the function to find manufacturing terms in the corpus
top_manufacturing_terms = find_manufacturing_terms(corpus)

# Print the top 150 manufacturing terms
print("## manufacturing")
for word, count in top_manufacturing_terms:
    print(f"{word}: {count}")



def find_transportation_terms(corpus):
    # Define a list of the top fifty most common railroad and transportation-related terms
    transportation_terms = [term.lower() for term in [
        "Railroad", "Railway", "Locomotive", "Freight train", "Passenger train", 
        "High-speed rail", "Commuter rail", "Light rail", "Subway system", "Monorail", 
        "Streetcar", "Tramway", "Track gauge", "Railcar", "Diesel engine", "Electric train", 
        "Steam locomotive", "Bullet train", "Rail yard", "Train station", "Rail bridge", 
        "Grade crossing", "Switch track", "Rolling stock", "Signal system", "Train dispatch", 
        "Rail tunnel", "Track maintenance", "Level crossing", "Railroad tie", "Ballast bed", 
        "Freight corridor", "Passenger corridor", "Intermodal terminal", "Container transport", 
        "Right of way", "Rail infrastructure", "Train conductor", "Brakeman", "Engineer", 
        "Freight manifest", "Waybill", "Cargo handling", "Rail logistics", "Timetable", 
        "Train schedule", "Platform edge", "Railway safety", "Commuter pass", "Transit hub"
    ]]

    # Initialize a Counter to tally occurrences of transportation terms
    transportation_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in transportation_terms:
            transportation_word_freq[word] += 1

    return transportation_word_freq.most_common(20)

# Call the function to find transportation terms in the corpus
top_transportation_terms = find_transportation_terms(corpus)

# Print the top 150 transportation terms
print("## railroads and transportation")
for word, count in top_transportation_terms:
    print(f"{word}: {count}")



def find_manual_labor_terms(corpus):
    # Define a list of the top fifty most common Spanish labor-related terms
    manual_labor_terms = [term.lower() for term in ["Factory", "labor union", "Union", "Worker", "Laborer", "Employee", "Employer", "Vocation", "Wage", "Salary", "Paycheck", "Hourly Wage", "Daily Wage", "Weekly Wage", "Overtime", "Minimum wage", "Living wage", "Health Insurance", "Healthcare", "Retirement", "Pension", "Sick leave", "Vacation", "Maternity leave", "Paternity leave", "Paid time off", "Layoff", "Dismissal", "Termination", "Hiring", "Firing", "Training", "Manual labor", "Blue-collar", "Workplace", "Factory floor", "Assembly line", "Warehouse", "Construction", "Maintenance", "Janitorial", "Service industry", "Service Worker"
    ]]

    # Initialize a Counter to tally occurrences of labor terms
    manual_labor_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in manual_labor_terms:
            manual_labor_word_freq[word] += 1

    return manual_labor_word_freq.most_common(20)

# Call the function to find labor terms in the corpus
top_manual_labor_terms = find_manual_labor_terms(corpus)

# Print the top 150 labor terms
print("## labor")
for word, count in top_manual_labor_terms:
    print(f"{word}: {count}")



def find_migration_terms(corpus):
    # Define a list of migration-related terms
    migration_terms = [term.lower() for term in ["immigration", "emigration", "refugee", "asylum", "naturalization", "resettlement", "integration", "exile", "citizenship", "border", "visa", "deportation", "fleeing", "repatriation", "exodus", "transplantation", "dispersion", "exodus", "nomadism", "migrant", "transient", "displacement", "colonization", "settler", "journey", "voyage", "pilgrimage", "relocation", "repopulation", "expatriate", "sojourner", "transmigrating","resettlement", "seeking refuge", "dislocation", "displaced person", "reintegration", "acculturation", "diaspora", "melting pot", "ethnic diversity", "immigrant community", "border crossing", "migration policy", "immigration reform"
    ]]

    # Initialize a Counter to tally occurrences of migration-related terms
    migration_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in migration_terms:
            migration_word_freq[word] += 1

    return migration_word_freq.most_common(20)

# Call the function to find migration-related terms in the corpus
top_migration_terms = find_migration_terms(corpus)

# Print the top 50 migration-related terms
print("## migration")
for word, count in top_migration_terms:
    print(f"{word}: {count}")



def find_leisure_terms(corpus):
    # Define a list of leisure-related terms
    leisure_terms = [term.lower() for term in ["ski", "leisure", "recreation", "entertainment", "activity", "hobby", "pastime", "sports", "game", "fun", "relaxation", "adventure", "pastime", "park", "picnic", "barbecue", "camp", "hike", "trail", "fishing", "hunting", "camping", "bonfire", "campfire", "swimming", "pool", "beach", "lake", "boating", "canoeing", "kayaking", "biking", "cycling", "walking", "running", "hiking", "gardening", "photography", "board game", "card game", "dance"
    ]]

    # Initialize a Counter to tally occurrences of leisure-related terms
    leisure_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in leisure_terms:
            leisure_word_freq[word] += 1

    return leisure_word_freq.most_common(20)

# Call the function to find leisure-related terms in the corpus
top_leisure_terms = find_leisure_terms(corpus)

# Print the top 50 leisure-related terms
print("## recreation")
for word, count in top_leisure_terms:
    print(f"{word}: {count}")



def find_religion_terms(corpus):
    # Define a list of the top fifty most common Spanish religion-related terms
    religion_terms = [term.lower() for term in ["Church", "Temple", "Mosque", "Synagogue", "Prayer", "Worship", "Faith", "Creed", "Spirituality", "Religious", "Devotion", "Ritual", "Ceremony", "Sacred", "Holy", "Blessing", "Preacher", "Minister", "Priest", "Pastor", "Deacon", "Congregation", "Parish", "Fellowship", "Almsgiving", "Devout", "Evangelism", "Revival", "Sermon", "Bible", "Scripture", "Quran", "Torah", "Hymn", "Choir", "Religious education", "Sunday school", "Youth group", "Confirmation", "Bar mitzvah", "Bat mitzvah", "Sacrament", "Communion", "Baptism", "Confession", "Repentance", "Salvation"
    ]]
    
    # Initialize a Counter to tally occurrences of religion terms
    religion_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in religion_terms:
            religion_word_freq[word] += 1

    return religion_word_freq.most_common(20)

# Call the function to find religion terms in the corpus
top_religion_terms = find_religion_terms(corpus)

# Print the top 150 religion terms
print("## religion")
for word, count in top_religion_terms:
    print(f"{word}: {count}")



def find_technology_terms(corpus):
    # Define a list of technology-related terms
    technology_terms = [term.lower() for term in ["Electric Fan", "Oscillating Fan", "Desk Fan", "Box Fan", "Ceiling Fan", "Portable Fan", "Ventilator", "Computer", "PC", "Software", "Hardware", "Data", "Database", "Network", "Internet", "Website", "Browser", "Operating system", "Dataset", "Word processor", "Spreadsheet", "Database", "Modem", "Printer", "Scanner", "Fax machine", "VHS", "Cassette", "Walkman", "Tape recorder", "CD player", "Compact disc", "Video game", "Atari", "Nintendo", "Gameboy", "Sega", "Playstation", "Xbox", "Calculator", "Typewriter", "Telephone", "Answering machine", "Pager", "Television", "VCR", "Remote control", "Antenna", "Cable", "Satellite", "Video cassette", "Walkie-talkie", "Walkie", "Radio", "Cassette player", "Boombox", "Turntable", "Vinyl record", "Record player", "Camera", "Polaroid", "Celluloid", "Flashlight", "Calculator", "Timepiece", "Wristwatch", "Microwave", "Toaster", "Blender", "Vacuum cleaner", "Dishwasher", "Washing machine", "Dryer", "Refrigerator", "Air conditioner", "Ventilator", "Heater", "Thermostat", "Alarm clock"
    ]]

    # Initialize a Counter to tally occurrences of technology terms
    technology_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in technology_terms:
            technology_word_freq[word] += 1

    return technology_word_freq.most_common(20)

# Call the function to find technology terms in the corpus
top_technology_terms = find_technology_terms(corpus)

# Print the top 150 technology terms
print("## technology")
for word, count in top_technology_terms:
    print(f"{word}: {count}")

# === Geographic Section ===



def find_basque_terms(corpus):
    # Define a list of Basque-related terms
    basque_terms = [term.lower() for term in ["Basque", "Basque Country", "Euskadi", "Euskara", "Donostia", "Bilbao", "Vitoria-Gasteiz", "Iruña", "Hondarribia", "Zarautz", "Getaria", "Biarritz", "Bayonne", "Saint-Jean-de-Luz", "Guernica", "Bermeo", "Mutriku", "Ondarroa", "Mundaka", "Lekeitio", "Orio", "Deba", "Zumaia", "Lazkao", "Azpeitia", "Zestoa", "Zarautz", "Hernani", "Amezketa", "Andoain", "Astigarraga", "Ataun", "Beasain", "Errenteria", "Ibarra", "Idiazabal", "Leaburu", "Legazpi", "Leintz-Gatzaga", "Txakoli", "Sagardo", "Pintxo", "Pintxos", "Pilota", "Basque pelota", "Jai alai", "Txapela", "Txistorra", "Idiazabal cheese"
    ]]

    # Initialize a Counter to tally occurrences of Basque terms
    basque_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Basque terms
    for word in tokens:
        if word in basque_terms:
            basque_word_freq[word] += 1

    return basque_word_freq.most_common(5)

# Call the function to find Basque-related terms in the corpus
top_basque_terms = find_basque_terms(corpus)

# Print the top 5 Basque-related terms
print("## basque")
for word, count in top_basque_terms:
    print(f"{word}: {count}")



def find_british_terms(corpus):
    british_terms = [term.lower() for term in ["British", "Britain", "London", "Manchester", "Birmingham", "Liverpool", "Leeds", "Bristol", "Sheffield", "Newcastle", "Cardiff", "Nottingham", "Southampton", "Leicester", "Brighton", "Portsmouth", "Plymouth", "Derby", "Hull", "Middlesbrough", "Northampton", "Luton", "Wolverhampton", "Norwich", "Swansea", "Oxford", "Cambridge", "Exeter", "Yorkshire", "Cornwall", "Essex", "Surrey", "Devon", "England"
    ]]
    
    british_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with British terms
    for word in tokens:
        if word in british_terms:
            british_word_freq[word] += 1

    return british_word_freq.most_common(5)

top_british_terms = find_british_terms(corpus)

print("## britain")
for word, count in top_british_terms:
    print(f"{word}: {count}")



def find_canadian_terms(corpus):
    canadian_terms = [term.lower() for term in ["Canada", "Canadian", "Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton", "Ottawa", "Winnipeg", "Quebec", "Victoria", "Halifax", "Regina", "Saskatoon", "St. John's", "Kitchener", "Burnaby", "Windsor", "Richmond", "Burlington", "Surrey", "Mississauga", "Markham", "Brampton", "Vaughan", "Oakville", "Niagara Falls", "Waterloo", "Guelph", "Cambridge", "Kelowna", "Fredericton", "Charlottetown", "Whitehorse", "Yellowknife", "Iqaluit", "Ontario", "Quebec", "Nova Scotia", "New Brunswick", "Manitoba", 
    ]]

    canadian_word_freq = Counter()
    canadian_term_files = {term: set() for term in canadian_terms}

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Canadian terms
    for word in tokens:
        if word in canadian_terms:
            canadian_word_freq[word] += 1

    return canadian_word_freq.most_common(5)

top_canadian_terms = find_canadian_terms(corpus)

print("## canada")
for word, count in top_canadian_terms:
    print(f"{word}: {count}")



def find_chinese_terms(corpus):
    chinese_terms = [term.lower() for term in ["Chinese", "China", "Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Tianjin", "Chongqing", "Hangzhou", "Nanjing", "Chengdu", "Wuhan", "Xi'an", "Suzhou", "Dalian", "Qingdao", "Shenyang", "Xiamen", "Changsha", "Zhengzhou", "Dongguan", "Wuxi", "Changchun", "Ningbo", "Kunming", "Nanchang", "Hefei", "Taiyuan", "Jinan", "Guiyang", "Fuzhou", "Harbin", "Hohhot", "Ürümqi", "Lanzhou", "Yinchuan", "Lhasa", "Nanning", "Haikou", "Macau", "Hong Kong", "Taipei", "Macao", "Guilin", "Kashgar", "Shijiazhuang", "Jining" 
    ]]
    chinese_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Chinese terms
    for word in tokens:
        if word in chinese_terms:
            chinese_word_freq[word] += 1

    return chinese_word_freq.most_common(5)

# Call the function to find Chinese-related terms in the corpus
top_chinese_terms = find_chinese_terms(corpus)

# Print the top 5 Chinese-related terms
print("## china")
for word, count in top_chinese_terms:
    print(f"{word}: {count}")



def find_finnish_terms(corpus):
    finnish_terms = [term.lower() for term in ["Finnish", "Suomalainen", "Finland", "Suomi", "Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu", "Turku", "Jyväskylä", "Kuopio", "Lahti", "Kouvola", "Pori", "Joensuu", "Lappeenranta", "Vaasa", "Hämeenlinna", "Seinäjoki", "Rovaniemi", "Mikkeli", "Kotka", "Salo", "Porvoo", "Lohja", "Hyvinkää", "Järvenpää", "Rauma", "Kokkola", "Kerava", "Kajaani", "Tuusula", "Kirkkonummi", "Seutula", "Sipoo", "Siuntio", "Karkkila", "Vihti", "Nurmijärvi", "Riihimäki", "Raseborg", "Loviisa", "Hanko", "Lohja", "Nastola", "Hollola", "Asikkala"
    ]]

    finnish_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Finnish terms
    for word in tokens:
        if word in finnish_terms:
            finnish_word_freq[word] += 1

    return finnish_word_freq.most_common(5)

top_finnish_terms = find_finnish_terms(corpus)

print("## finland")
for word, count in top_finnish_terms:
    print(f"{word}: {count}")



def find_french_terms(corpus):
    french_terms = [term.lower() for term in ["French", "France", "Marseille", "Lyon", "Toulouse", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille", "Rennes", "Reims", "Le Havre", "Cergy", "Saint-Étienne", "Toulon", "Angers", "Grenoble", "Dijon", "Nîmes", "Aix-en-Provence", "Saint-Quentin-en-Yvelines", "Brest", "Le Mans", "Amiens", "Limoges", "Clermont-Ferrand", "Villeurbanne", "Besançon", "Orléans", "Metz", "Rouen", "Mulhouse", "Perpignan", "Caen", "Argenteuil", "Saint-Denis", "Roubaix", "Tourcoing", "Avignon", "Poitiers", "Créteil", "Nanterre", "Versailles"
    ]]
    
    french_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with French terms
    for word in tokens:
        if word in french_terms:
            french_word_freq[word] += 1

    return french_word_freq.most_common(5)

top_french_terms = find_french_terms(corpus)

print("## france")
for word, count in top_french_terms:
    print(f"{word}: {count}")



def find_german_terms(corpus):
    german_terms = [term.lower() for term in ["German", "Germany", "Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Düsseldorf", "Dortmund", "Essen", "Leipzig", "Bremen", "Dresden", "Hanover", "Nuremberg", "Duisburg", "Bochum", "Wuppertal", "Bielefeld", "Bonn", "Münster", "Karlsruhe", "Mannheim", "Augsburg", "Wiesbaden", "Gelsenkirchen", "Mönchengladbach", "Braunschweig", "Chemnitz", "Kiel", "Aachen", "Halle", "Magdeburg", "Freiburg", "Krefeld", "Lübeck", "Oberhausen", "Erfurt", "Mainz", "Rostock", "Kassel", "Hagen", "Saarbrücken", "Hamm", "Potsdam", "Leverkusen", "Oldenburg"
    ]]

    german_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with German terms
    for word in tokens:
        if word in german_terms:
            german_word_freq[word] += 1

    return german_word_freq.most_common(5)

top_german_terms = find_german_terms(corpus)

print("## germany")
for word, count in top_german_terms:
    print(f"{word}: {count}")



def find_greek_terms(corpus):
    greek_terms = [term.lower() for term in ["Greek", "Greece", "Athens", "Thessaloniki", "Patras", "Heraklion", "Larissa", "Volos", "Ioannina", "Chania", "Chalcis", "Rethymno", "Serres", "Kavala", "Komotini", "Alexandroupoli", "Katerini", "Veria", "Trikala", "Lamia", "Kozani", "Polichni", "Karditsa", "Sykies", "Nea Ionia", "Ioannis", "Agia Paraskevi", "Palaio Faliro", "Tripoli", "Galatsi", "Agrinio", "Chios", "Mytilene", "Kalamata", "Kavala", "Volos", "Larissa", "Heraklion", "Chalkida", "Thiva", "Sparta", "Corfu", "Lamia", "Karditsa", "Kastoria", "Kavala"
    ]]
    
    greek_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Greek terms
    for word in tokens:
        if word in greek_terms:
            greek_word_freq[word] += 1

    return greek_word_freq.most_common(5)

top_greek_terms = find_greek_terms(corpus)

print("## greece")
for word, count in top_greek_terms:
    print(f"{word}: {count}")



def find_geographic_words(corpus):
    # Define a list of geographic place names in Idaho (converted to lowercase for easier matching)
    idaho_geographic_places = [place.lower() for place in [
        "Caldwell", "Idaho Falls", "Pocatello", "Rupert", "Boise", "Nampa", "Emmett", "Twin Falls", "Burley", 
        "Moscow", "Lewiston", "Mountain Home", "Blackfoot", "Post Falls", "Sandpoint", "Jerome, Idaho", "Weiser", 
        "Eagle, Idaho", "Middleton", "Rathdrum", "Bonners Ferry", "St. Maries", "Spirit Lake", "Glenns Ferry", 
        "Parma", "Kimberly", "St. Anthony", "Gooding", "McCall, Idaho", "Driggs", "American Falls", "Grangeville", "Fountain, Idaho", 
        "Acequia", "Albion", "Arco", "Athol", "Bellevue", "Bloomington", "Bruneau", "Buhl", "Challis", "Clayton", "Clifton", 
        "Cottonwood", "Council, Idaho", "Crouch", "Culdesac", "Dayton, Idaho", "Dover", "Downey", "Drummond", "Dubois", "Elk City", 
        "Fairfield", "Fenn", "Fernwood", "Fort Hall", "Fruitland", "Garden City", "Genesee", "Greenleaf", 
        "Hagerman", "Hansen, Idaho", "Hazelton", "Heyburn", "Holbrook", "Homedale", "Horseshoe Bend", "Huetter", "Huston, Idaho", "Inkom", 
        "Iona", "Julietta", "Kamiah", "Kendrick, Idaho", "Ketchum", "Kooskia", "Kootenai", "Kuna", "Lapwai", "Lava Hot Springs", 
        "Leadore", "Lemhi", "Letha", "Lost River", "Mackay", "Malad City", "Malta", "Marsing", "Melba, Idaho", "Menan", "Mink Creek", 
        "Montpelier", "Monteview", "Montour", "Moore, Idaho", "Mountain Home AFB", "Mud Lake", "Mullan", "Murtaugh", "Newdale", 
        "New Meadows", "New Plymouth", "Nezperce, Idaho", "Notus", "Oakley", "Oldtown", "Onaway", "Orofino", "Osburn, Idaho", 
        "Parker", "Parkline", "Payette", "Peck", "Picabo", "Pinehurst", "Placerville", "Plummer", "Pollock", "Potlatch", 
        "Preston", "Priest Lake", "Priest River", "Rexburg", "Richfield", "Rigby", "Rimini", "Riverside", "Rockford", "Rockland", 
        "Sagle", "Shelley, Idaho", "Shoshone", "Smelterville", "Soda Springs", "Spalding", "Spencer", "Stanley, Idaho", "Sugar City", 
        "Sun Valley", "Swan Valley", "Terry, Idaho", "Teton", "Tetonia", "Troy, Idaho", "Uhland", "Victor, Idaho", "Wallace, Idaho", "Wardner", "Warm River", 
        "Weippe", "Wendell", "Weston", "White Bird", "Wilder", "Winchester", "Worley"]]

    # Initialize a Counter to tally occurrences of geographic place names
    geographic_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in idaho_geographic_places:
            geographic_word_freq[word] += 1

    return geographic_word_freq.most_common(25)

# Call the function to find geographic words in the corpus
top_geographic_words = find_geographic_words(corpus)

# Print the top 150 geographic place names in Idaho
print("## idaho")
for word, count in top_geographic_words:
    print(f"{word}: {count}")



def find_indian_terms(corpus):
    indian_terms = [term.lower() for term in [
        "Indian", "India", "Hindi", "New Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", 
        "Hyderabad", "Pune", "Ahmedabad", "Surat", "Jaipur", "Kanpur", "Lucknow", "Nagpur", 
        "Patna", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Vadodara", "Firozabad", "Ludhiana", 
        "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot", "Varanasi", "Srinagar", "Aurangabad", 
        "Dhanbad", "Amritsar", "Navi Mumbai", "Allahabad", "Ranchi", "Howrah", "Jabalpur", "Gwalior", 
        "Vijayawada", "Jodhpur", "Raipur", "Kota", "Guwahati", "Chandigarh"
    ]]
    
    indian_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Indian terms
    for word in tokens:
        if word in indian_terms:
            indian_word_freq[word] += 1

    return indian_word_freq.most_common(5)

# Call the function to find Indian-related terms in the corpus
top_indian_terms = find_indian_terms(corpus)

# Print the top 5 Indian-related terms
print("## india")
for word, count in top_indian_terms:
    print(f"{word}: {count}")



def find_irish_terms(corpus):
    irish_terms = [term.lower() for term in ["Irish", "Ireland", "Dublin", "Galway", "Limerick", "Waterford", "Drogheda", "Dundalk", "Bray", "Navan", "Kilkenny", "Ennis", "Carlow", "Tralee", "Newbridge", "Portlaoise", "Balbriggan", "Naas", "Athlone", "Mullingar", "Celbridge", "Wexford", "Letterkenny", "Sligo", "Clonmel", "Greystones", "Malahide", "Carrigaline", "Leixlip", "Lucan", "Skerries", "Tramore", "Killarney", "Arklow", "Kilcock", "Ballina", "Castlebar", "Maynooth", "Thurles", "Monaghan", "Mallow", "Portarlington", "Buncrana", "Gorey", "Tuam", "Cobh", "potato famine"
    ]]
    
    irish_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Irish terms
    for word in tokens:
        if word in irish_terms:
            irish_word_freq[word] += 1

    return irish_word_freq.most_common(5)

top_irish_terms = find_irish_terms(corpus)

print("## ireland")
for word, count in top_irish_terms:
    print(f"{word}: {count}")



def find_italian_terms(corpus):
    italian_terms = [term.lower() for term in ["Italian", "Italy", "Rome", "Milan", "Naples", "Turin", "Palermo", "Genoa", "Bologna", "Florence", "Bari", "Catania", "Venice", "Verona", "Messina", "Padua", "Trieste", "Taranto", "Brescia", "Prato", "Reggio", "Modena", "Reggio", "Emilia", "Perugia", "Livorno", "Ravenna", "Cagliari", "Foggia", "Rimini", "Salerno", "Ferrara", "Sassari", "Latina", "Giugliano", "Monza", "Syracuse", "Bergamo", "Pescara", "Trento", "Forlì", "Vicenza", "Terni", "Bolzano", "Novara", "Piacenza", "Ancona", "Andria", "Udine"
    ]]
    
    italian_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Italian terms
    for word in tokens:
        if word in italian_terms:
            italian_word_freq[word] += 1

    return italian_word_freq.most_common(5)

top_italian_terms = find_italian_terms(corpus)

print("## italy")
for word, count in top_italian_terms:
    print(f"{word}: {count}")



def find_japanese_terms(corpus):
    japanese_terms = [term.lower() for term in ["Japanese", "Japan", "Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo", "Fukuoka", "Kobe", "Kyoto", "Kawasaki", "Saitama", "Hiroshima", "Sendai", "Kitakyushu", "Chiba", "Sakai", "Niigata", "Hamamatsu", "Okayama", "Kumamoto", "Sagamihara", "Kagoshima", "Matsumoto", "Kanazawa", "Naha", "Matsuyama", "Kōchi", "Naha", "Nagasaki", "Toyama", "Otsu", "Wakayama", "Akita", "Aomori", "Asahikawa", "Fukushima", "Fukui", "Gifu", "Hachinohe", "Hakodate", "Higashiosaka", "Himeji", "Iwaki", "Iwakuni", "Kōfu", "Kure"
    ]]
    
    japanese_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Japanese terms
    for word in tokens:
        if word in japanese_terms:
            japanese_word_freq[word] += 1

    return japanese_word_freq.most_common(5)

# Call the function to find Japanese-related terms in the corpus
top_japanese_terms = find_japanese_terms(corpus)

# Print the top 5 Japanese-related terms
print("## japan")
for word, count in top_japanese_terms:
    print(f"{word}: {count}")



def find_mexican_terms(corpus):
    mexican_terms = [term.lower() for term in ["Mexico", "Mexican", "Mexico City", "Guadalajara", "Monterrey", "Puebla", "Tijuana", "León", "Ciudad Juárez", "Chihuahua", "Cancún", "Mérida", "Aguascalientes", "Querétaro", "Toluca", "Hermosillo", "San Luis Potosí", "Culiacán", "Acapulco", "Morelia", "Saltillo", "Veracruz", "Villahermosa", "Tuxtla Gutiérrez", "Durango", "Tepic", "Colima", "Campeche", "La Paz", "Torreón", "Mazatlán", "Reynosa", "Matamoros", "Celaya", "Irapuato", "Nuevo Laredo", "Ensenada", "Coatzacoalcos", "Oaxaca", "Tlalnepantla", "Tampico", "Cuernavaca", "Zacatecas", "Uruapan", "Nogales", "Pachuca", "Cuautitlán", "Tapachula", "Delicias"
    ]]
    
    mexican_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Mexican terms
    for word in tokens:
        if word in mexican_terms:
            mexican_word_freq[word] += 1

    return mexican_word_freq.most_common(5)

# Call the function to find Mexican-related terms in the corpus
top_mexican_terms = find_mexican_terms(corpus)

# Print the top 5 Mexican-related terms
print("## mexico")
for word, count in top_mexican_terms:
    print(f"{word}: {count}")



def find_norwegian_terms(corpus):
    norwegian_terms = [term.lower() for term in ["Norwegian", "Norway", "Oslo", "Bergen", "Trondheim", "Stavanger", "Kristiansand", "Tromsø", "Drammen", "Fredrikstad", "Skien", "Sandnes", "Sarpsborg", "Bodø", "Ålesund", "Haugesund", "Porsgrunn", "Arendal", "Tønsberg", "Hamar", "Ytre Enebakk", "Halden", "Larvik", "Askøy", "Kongsberg", "Harstad", "Molde", "Steinkjer", "Lillehammer", "Gjøvik", "Kristiansund", "Narvik", "Horten", "Leirvik", "Mandal", "Voss", "Mo i Rana", "Namsos", "Lillestrøm", "Sandefjord", "Hønefoss", "Egersund", "Kongsvinger", "Raufoss", "Rjukan"
    ]]

    norwegian_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Norwegian terms
    for word in tokens:
        if word in norwegian_terms:
            norwegian_word_freq[word] += 1

    return norwegian_word_freq.most_common(5)

top_norwegian_terms = find_norwegian_terms(corpus)

print("## norway")
for word, count in top_norwegian_terms:
    print(f"{word}: {count}")



def find_philippine_terms(corpus):
    philippine_terms = [term.lower() for term in ["Philippines", "Filipino", "Tagalog", "Manila", "Quezon City", "Davao City", "Caloocan", "Cebu City", "Zamboanga City", "Antipolo", "Pasig", "Taguig", "Cagayan de Oro", "Parañaque", "Valenzuela", "Las Piñas", "Makati", "Bacolod", "Muntinlupa", "Iloilo City", "Tarlac City", "Baguio", "Batangas City", "General Santos", "Lapu-Lapu", "Iligan", "Olongapo", "Binan", "Santa Rosa", "Tagum", "Tacloban", "Malolos", "Navotas", "Dagupan", "Toledo", "Lucena", "San Fernando", "Cabanatuan", "Ormoc", "Dasmariñas", "San Juan", "Baliuag", "Tuguegarao", "Malabon", "Mabalacat", "Cotabato City", "Puerto Princesa", "Butuan"
    ]]
    
    philippine_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Philippine terms
    for word in tokens:
        if word in philippine_terms:
            philippine_word_freq[word] += 1

    return philippine_word_freq.most_common(5)

# Call the function to find Philippine-related terms in the corpus
top_philippine_terms = find_philippine_terms(corpus)

# Print the top 5 Philippine-related terms
print("## philippines")
for word, count in top_philippine_terms:
    print(f"{word}: {count}")



def find_polish_terms(corpus):
    polish_terms = [term.lower() for term in ["Poland", "Warsaw", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok", "Katowice", "Gdynia", "Częstochowa", "Radom", "Sosnowiec", "Toruń", "Kielce", "Rzeszów", "Gliwice", "Zabrze", "Olsztyn", "Bielsko-Biała", "Bytom", "Zielona Góra", "Rybnik", "Tarnów", "Opole", "Gorzów", "Dąbrowa", "Górnictwo", "Elbląg", "Płock", "Wałbrzych", "Chorzów", "Tychy", "Jaworzno", "Jastrzębie", "Zdrój", "Mysłowice", "Legnica", "Lubin", "Siedlce", "Inowrocław", "Piotrków", "Trybunalski", "Ostrołęka"
    ]]
    
    polish_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Polish terms
    for word in tokens:
        if word in polish_terms:
            polish_word_freq[word] += 1

    return polish_word_freq.most_common(5)

top_polish_terms = find_polish_terms(corpus)

print("## poland")
for word, count in top_polish_terms:
    print(f"{word}: {count}")



def find_portuguese_terms(corpus):
    portuguese_terms = [term.lower() for term in [
        "Portuguese", "Portugal", "Lisbon", "Porto", "Vila Nova", "Amadora", "Braga", 
        "Funchal", "Coimbra", "Setúbal", "Queluz", "Agualva-Cacém", "Aveiro", "Viseu", 
        "Amora", "Rio Tinto", "Matosinhos", "Évora", "Castelo Branco", "Guimarães", 
        "Vila Franca", "Santarém", "Vila do Conde", "Ponte de Lima", "Loures", 
        "Póvoa de Varzim", "Faro", "Sever do Vouga", "Paredes", "Penafiel", "Lagos", 
        "Odivelas", "Ovar", "Maia", "Beja", "Gondomar", "Covilhã", "Águeda", "Fafe", 
        "Almada", "Elvas", "Torres Vedras", "Loulé", "Portalegre", "Barcelos", 
        "Caldas da Rainha", "Leiria"
    ]]
    
    portuguese_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and count only exact matches
    for word in tokens:
        if word in portuguese_terms:
            portuguese_word_freq[word] += 1

    return portuguese_word_freq.most_common(5)

top_portuguese_terms = find_portuguese_terms(corpus)

print("## portugal")
for word, count in top_portuguese_terms:
    print(f"{word}: {count}")



def find_scottish_terms(corpus):
    scottish_terms = [term.lower() for term in ["Scottish", "Scotland", "Edinburgh", "Glasgow", "Aberdeen", "Dundee", "Inverness", "Stirling", "Perth", "Fife", "Falkirk", "Ayr", "East Kilbride", "Livingston", "Cumbernauld", "Kilmarnock", "Greenock", "Coatbridge", "Glenrothes", "Airdrie", "Kirkcaldy", "Dunfermline", "Dumfries", "Motherwell", "Paisley", "Renfrew", "Irvine", "Giffnock", "Newton Mearns", "Cambuslang", "Barrhead", "Blantyre", "Stranraer", "Bellshill", "Kirkintilloch", "Wishaw", "Nairn", "Buckie", "Portree", "Inverurie", "Alloa", "Bathgate", "Dingwall", "Elgin", "Fort William", "Hawick", "Jedburgh"
    ]]
    
    scottish_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for exact matches with Scottish terms
    for word in tokens:
        if word in scottish_terms:
            scottish_word_freq[word] += 1

    return scottish_word_freq.most_common(5)

top_scottish_terms = find_scottish_terms(corpus)

print("## scotland")
for word, count in top_scottish_terms:
    print(f"{word}: {count}")



def find_spanish_terms(corpus):
    spanish_terms = [term.lower() for term in ["Spanish", "Spain", "Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza", "Málaga", "Murcia", "Palma", "Las Palmas", "Bilbao", "Alicante", "Córdoba", "Valladolid", "Vigo", "Gijón", "L'Hospitalet", "A Coruña", "Vitoria", "Granada", "Elche", "Oviedo", "Badalona", "Terrassa", "Cartagena", "Sabadell", "Jerez", "Móstoles", "Santa Cruz", "Alcalá", "Fuenlabrada", "Almería", "Leganés", "San Sebastián", "Getafe", "Burgos", "Albacete", "Santander", "Castellón", "Logroño", "Badajoz", "Huelva", "Salamanca", "Lérida", "Tarragona", "León"
    ]]
  
    spanish_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Spanish terms
    for word in tokens:
        if word in spanish_terms:
            spanish_word_freq[word] += 1

    return spanish_word_freq.most_common(5)

top_spanish_terms = find_spanish_terms(corpus)

print("## spain")
for word, count in top_spanish_terms:
    print(f"{word}: {count}")



def find_swedish_terms(corpus):
    swedish_terms = [term.lower() for term in ["Swedish", "Swede", "Swedes", "Scandinavian", "Stockholm", "Sweden", "Gothenburg", "Malmö", "Uppsala", "Linköping", "Norrköping", "Örebro", "Västerås", "Helsingborg", "Jönköping", "Umeå", "Lund", "Borås", "Sundsvall", "Gävle", "Östersund", "Eskilstuna", "Södertälje", "Halmstad", "Växjö", "Karlstad", "Trollhättan", "Örnsköldsvik", "Kalmar", "Kristianstad", "Falun", "Borlänge", "Skövde", "Karlskrona", "Visby", "Luleå", "Märsta", "Alingsås", "Östersund", "Vänersborg", "Täby", "Hässleholm", "Trelleborg", "Nyköping", "Piteå", "Lidingö"
    ]]

    swedish_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Swedish terms
    for word in tokens:
        if word in swedish_terms:
            swedish_word_freq[word] += 1

    return swedish_word_freq.most_common(5)

top_swedish_terms = find_swedish_terms(corpus)

print("## swedish")
for word, count in top_swedish_terms:
    print(f"{word}: {count}")

# === Custom Section ===




def find_reproductive_rights_terms(corpus):
    reproductive_rights_terms = [term.lower() for term in ["abortion", "contraception", "birth control", "family planning", "reproductive health", "reproductivity", "sterilization", "IVF", "in vitro fertilization", "pregnancy", "miscarriage", "stillbirth", "menstruation", "menstrual health", "menses", "ovulation", "ovarian", "uterus", "womb", "fertility treatment", "assisted reproduction", "egg donation", "sperm donation", "surrogacy", "adoption", "parental leave", "maternity leave", "paternity leave", "reproductive rights", "reproductive justice", "sexual health", "sexual education", "family planning clinic", "Planned Parenthood", "morning-after pill", "RU-486", "emergency contraception", "IUD", "implant", "tubal ligation", "vasectomy", "condom", "diaphragm", "cervical cap", "birth spacing", "reproductive freedom", "pro-choice", "pro-life", "reproductive autonomy"
    ]]

    # Initialize a counter for reproductive rights-related terms
    reproductive_rights_word_freq = Counter()

    # Tokenize the corpus
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        if word in reproductive_rights_terms:
            reproductive_rights_word_freq[word] += 1

    # Return the top 50 most common reproductive rights-related terms
    return reproductive_rights_word_freq.most_common(5)

# Call the function to find reproductive rights-related terms in the corpus
top_reproductive_rights_terms = find_reproductive_rights_terms(corpus)

# Print the top 50 reproductive rights-related terms
print("## reproductive rights")
for word, count in top_reproductive_rights_terms:
    print(f"{word}: {count}")
