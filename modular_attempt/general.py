from collections import Counter
import re

def find_agriculture_terms(corpus):
    # Define a list of agriculture-related terms
    agriculture_terms = ["harvest", "tractor", "acreage", "crop", "livestock", "field", "barn", "ranch", "garden", "orchard", "dairy", "cattle", "poultry", "equipment", "fertilizer", "seed", "irrigation", "plow", "farmhand", "hoe", "shovel", "milking", "hay", "silage", "compost", "weeding", "crop rotation", "organic", "gmo", "sustainable", "farming", "rural", "homestead", "grain", "wheat", "corn", "soybean", "potato", "apple", "berry", "honey", "apiary", "pasture", "combine", "trailer", "baler", "thresher"]

    # Initialize a Counter to tally occurrences of agriculture-related terms
    agriculture_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is an agriculture-related term
        if word in agriculture_terms:
            agriculture_word_freq[word] += 1

    # Return the top 50 most common agriculture-related terms
    return agriculture_word_freq.most_common(50)

# Call the function to find agriculture-related terms in the corpus
top_agriculture_terms = find_agriculture_terms(corpus)

# Print the top 50 agriculture-related terms
print("*agriculture")
for word, count in top_agriculture_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_animal_terms(corpus):
    # Define a list of the top fifty most common Spanish animal-related terms
    animal_terms = ["cow", "sheep", "horse", "goat", "pig", "chicken", "turkey", "duck", "quail", "rabbit", "squirrel", "moose", "elk", "deer", "bear", "coyote", "wolf", "fox", "mountain lion", "raccoon", "skunk", "badger", "possum", "weasel", "ferret", "mink", "otter", "beaver", "muskrat", "marmot", "gopher", "prairie dog", "chipmunk", "bison", "buffalo", "lizard", "snake", "frog", "toad", "newt", "salamander", "owl", "hawk", "eagle", "raven", "crow", "sparrow", "finch", "bluebird", "cougar"]  # Add more as needed

    # Initialize a Counter to tally occurrences of animal terms
    animal_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is an animal term
        if word in animal_terms:
            animal_word_freq[word] += 1

    # Return the top 150 most common animal terms
    return animal_word_freq.most_common(150)

# Call the function to find animal terms in the corpus
top_animal_terms = find_animal_terms(corpus)

# Print the top 150 animal terms
print("*animals")
for word, count in top_animal_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_fashion_terms(corpus):
    # Define a list of fashion-related terms
    fashion_terms = ["clothing", "fashion", "style", "apparel", "outfit", "wardrobe", "jeans", "t-shirt", "sweater", "jacket", "dress", "skirt", "pants", "shoes", "boots", "sneakers", "hat", "cap", "scarf", "gloves", "socks", "underwear", "outerwear", "workwear", "uniform", "overalls", "apron", "denim", "flannel", "plaid", "cotton", "polyester", "fabric", "stitching", "seamstress", "tailor", "alterations", "thrift", "secondhand", "budget", "affordable", "sale", "discount", "clearance", "shopping", "store", "retail", "department", "mall"]

    # Initialize a Counter to tally occurrences of fashion-related terms
    fashion_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a fashion-related term
        if word in fashion_terms:
            fashion_word_freq[word] += 1

    # Return the top 50 most common fashion-related terms
    return fashion_word_freq.most_common(50)

# Call the function to find fashion-related terms in the corpus
top_fashion_terms = find_fashion_terms(corpus)

# Print the top 50 fashion-related terms
print("*clothing")
for word, count in top_fashion_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_conflict_terms(corpus):
    # Define a list of conflict-related terms
    conflict_terms = ["conflict", "war", "battle", "combat", "soldier", "military", "deployment", "combatant", "veteran", "casualty", "injury", "wound", "trauma", "ptsd", "violence", "aggression", "hostility", "tension", "fear", "anxiety", "safety", "security", "protection", "defense", "attack", "invasion", "occupation", "resistance", "rebellion", "revolution", "mobilization", "draft", "conscription", "alliance", "enemy", "foe", "ally", "peacekeeping", "ceasefire", "treaty", "negotiation", "diplomacy", "sanctions", "arms", "weapons", "missile", "bomb", "gunfire"]

    # Initialize a Counter to tally occurrences of conflict-related terms
    conflict_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a conflict-related term
        if word in conflict_terms:
            conflict_word_freq[word] += 1

    # Return the top 50 most common conflict-related terms
    return conflict_word_freq.most_common(50)

# Call the function to find conflict-related terms in the corpus
top_conflict_terms = find_conflict_terms(corpus)

# Print the top 50 conflict-related terms
print("*conflict")
for word, count in top_conflict_terms:
    print(f"{word.capitalize()}: {count}")
  
from collections import Counter
import re

def find_crime_terms(corpus):
    # Define a list of the top fifty most common Spanish crime-related terms
    crime_terms = ["crime", "violence", "theft", "robbery", "burglary", "assault", "homicide", "murder", "rape", "domestic violence", "gangs", "drugs", "trafficking", "possession", "distribution", "addiction", "prostitution", "gambling", "corruption", "bribery", "fraud", "embezzlement", "extortion", "racketeering", "money laundering", "forgery", "identity theft", "cybercrime", "vandalism", "arson", "illegal immigration", "detention", "arrest", "interrogation", "trial", "plea bargain", "conviction", "sentencing", "imprisonment", "probation", "parole", "rehabilitation", "recidivism", "police", "detective", "officer", "investigation", "evidence", "forensics"]  # Add more as needed

    # Initialize a Counter to tally occurrences of crime terms
    crime_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a crime term
        if word in crime_terms:
            crime_word_freq[word] += 1

    # Return the top 150 most common crime terms
    return crime_word_freq.most_common(150)

# Call the function to find crime terms in the corpus
top_crime_terms = find_crime_terms(corpus)

# Print the top 150 crime terms
print("*crime")
for word, count in top_crime_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_culture_terms(corpus):
    # Define a list of culture-related terms
    culture_terms = ["tradition", "folklore", "customs", "rituals", "celebration", "values", "community", "cuisine", "festivals", "art", "music", "dance", "language", "dialect", "family", "history", "identity", "belonging", "neighborhood", "gathering", "gatherings", "socializing", "stories", "folk", "legends", "crafts", "skills", "craftsmanship", "oral tradition", "ethnicity", "diversity", "inclusion", "community centers", "street fairs", "parades", "food trucks", "ethnic foods", "local traditions", "folk music", "folk dance", "folk art", "cultural exchange", "cultural identity", "cultural pride", "multiculturalism", "ethnic neighborhoods"]

    # Initialize a Counter to tally occurrences of culture-related terms
    culture_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a culture-related term
        if word in culture_terms:
            culture_word_freq[word] += 1

    # Return the top 50 most common culture-related terms
    return culture_word_freq.most_common(50)

# Call the function to find culture-related terms in the corpus
top_culture_terms = find_culture_terms(corpus)

# Print the top 50 culture-related terms
print("*culture")
for word, count in top_culture_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_economic_terms(corpus):
    # Define a list of the top fifty most common Spanish economic-related terms
    economic_terms = ["employment", "job", "work", "labor", "wage", "salary", "income", "paycheck", "earnings", "livelihood", "occupation", "career", "profession", "trade", "skill", "craft", "manual labor", "blue-collar", "white-collar", "joblessness", "layoff", "dismissal", "termination", "retrenchment", "redundancy", "job search", "interview", "resume", "cover letter", "application", "hiring", "training", "apprenticeship", "promotion", "advancement", "raise", "benefits", "pension", "retirement", "savings", "investment", "budgeting", "financial planning", "debt", "credit", "loan", "mortgage"]  # Add more as needed

    # Initialize a Counter to tally occurrences of economic terms
    economic_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is an economic term
        if word in economic_terms:
            economic_word_freq[word] += 1

    # Return the top 150 most common economic terms
    return economic_word_freq.most_common(150)

# Call the function to find economic terms in the corpus
top_economic_terms = find_economic_terms(corpus)

# Print the top 150 economic terms
print("*economy")
for word, count in top_economic_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_education_terms(corpus):
    # Define a list of the top fifty most common Spanish education-related terms
    education_terms = ["School", "Classroom", "Teacher", "Student", "Learning", "Literacy", "Numeracy", "Curriculum", "Assignment", "Homework", "Exam", "Test", "Grade", "Report card", "Diploma", "Degree", "Certificate", "Transcript", "Textbook", "Library", "Study", "Research", "Project", "Group work", "Peer review", "Tutoring", "Principal", "Administrator", "Counselor", "Resource center", "Special education", "Individualized education plan (IEP)", "Field trip", "Extracurricular", "Athletics", "Club", "Volunteer", "Parent-teacher conference", "Back-to-school night", "Open house", "Graduation", "Prom", "Financial aid", "Scholarship", "Grant", "Loan", "Work-study program"]  # Add more as needed

    # Initialize a Counter to tally occurrences of education terms
    education_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is an education term
        if word in education_terms:
            education_word_freq[word] += 1

    # Return the top 150 most common education terms
    return education_word_freq.most_common(150)

# Call the function to find education terms in the corpus
top_education_terms = find_education_terms(corpus)

# Print the top 150 education terms
print("*education")
for word, count in top_education_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_environment_terms(corpus):
    # Define a list of environment-related terms
    environment_terms = environment_terms = ["Environment", "Nature", "Ecology", "Ecosystem", "Biodiversity", "Conservation", "Sustainability", "Climate", "Climate change", "Global warming", "Pollution", "Air pollution", "Water pollution", "Soil pollution", "Deforestation", "Habitat destruction", "Waste management", "Recycling", "Renewable energy", "Solar energy", "Wind energy", "Hydropower", "Geothermal energy", "Carbon footprint", "Greenhouse gases", "Ozone depletion", "Wildlife", "Endangered species", "Natural resources", "Land conservation", "Water conservation", "Energy efficiency", "Environmental impact", "Environmental policy", "Environmental regulation", "Environmental awareness", "Environmental education", "Environmental activism", "Sustainable development", "Urbanization", "Rural development", "Land use", "Land degradation", "Desertification", "Ocean conservation", "Marine life", "Coral reefs", "Sea level rise", "Water scarcity", "Drought", "Flood", "Natural disaster", "Ecotourism", "Green spaces", "Parks", "Forests", "Wetlands", "Mountains", "Rivers", "Lakes", "Oceans", "Beaches", "Glaciers", "Tundra", "Grasslands"] # Add more as needed

    # Initialize a Counter to tally occurrences of environment terms
    environment_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is an environment term
        if word in environment_terms:
            environment_word_freq[word] += 1

    # Return the top 150 most common environment terms
    return environment_word_freq.most_common(150)

# Call the function to find environment terms in the corpus
top_environment_terms = find_environment_terms(corpus)

# Print the top 150 environment terms
print("*environment")
for word, count in top_environment_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_family_terms(corpus):
    # Define a list of the top fifty most common Spanish family-related terms
    family_terms = ["Family", "Parent", "Mother", "Father", "Child", "Sibling", "Brother", "Sister", "Grandparent", "Grandfather", "Grandmother", "Grandchild", "Cousin", "Aunt", "Uncle", "Nephew", "Niece", "Step-parent", "Step-sibling", "Step-brother", "Step-sister", "Stepchild", "Spouse", "Husband", "Wife", "Partner", "Boyfriend", "Girlfriend", "Fiance", "Fiancee", "Domestic partner", "Marriage", "Wedding", "Divorce", "Separation", "Single parent", "Orphan", "Adoptive parent", "Adopted child", "Foster parent", "Foster child", "Guardian", "Legal guardian", "Custody", "Child support", "Family gathering", "Family dinner", "Family tradition"]  # Add more as needed

    # Initialize a Counter to tally occurrences of family terms
    family_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a family term
        if word in family_terms:
            family_word_freq[word] += 1

    # Return the top 150 most common family terms
    return family_word_freq.most_common(150)

# Call the function to find family terms in the corpus
top_family_terms = find_family_terms(corpus)

# Print the top 150 family terms
print("*family")
for word, count in top_family_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_food_and_drink_terms(corpus):
    # Define a list of the top fifty most common Spanish food and drink terms
    food_and_drink_terms = ["Potato", "Beans", "Beef", "Pork", "Chicken", "Milk", "Bread", "Butter", "Eggs", "Cheese", "Apple", "Pie", "Peach", "Biscuit", "Coffee", "Tea", "Beer", "Whiskey", "Soda", "Water", "Soup", "Stew", "Salad", "Corn", "Wheat", "Barley", "Oats", "Onion", "Garlic", "Salt", "Pepper", "Lard", "Jam", "Honey", "Cider", "Vinegar", "Bacon", "Sausage", "Jerky", "Pickles", "Preserves", "Cake", "Cookies", "Doughnuts", "Ice cream", "Candy", "Chocolate", "Nuts", "Raisins"]  # Add more as needed

    # Initialize a Counter to tally occurrences of food and drink terms
    food_and_drink_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a food and drink term
        if word in food_and_drink_terms:
            food_and_drink_word_freq[word] += 1

    # Return the top 150 most common food and drink terms
    return food_and_drink_word_freq.most_common(150)

# Call the function to find food and drink terms in the corpus
top_food_and_drink_terms = find_food_and_drink_terms(corpus)

# Print the top 150 food and drink terms
print("*food and drink")
for word, count in top_food_and_drink_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_happiness_terms(corpus):
    # Define a list of happiness-related terms
    happiness_terms = ["Joy", "Contentment", "Bliss", "Elation", "Cheer", "Pleasure", "Happiness", "Well-being", "Serenity", "Hopefulness", "Enjoyment", "Comfort", "Comfortable", "Euphoria", "Glee", "Amusement", "Thrill", "Radiance", "Laughter", "Smile", "Giggles", "Goodwill", "Warmth", "Affection", "Closeness","Friendship", "Companionship", "Bonding", "Belonging", "Acceptance", "Acknowledgment", "Approval", "Gratefulness", "Thankfulness"]

    # Initialize a Counter to tally occurrences of happiness-related terms
    happiness_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a happiness-related term
        if word in happiness_terms:
            happiness_word_freq[word] += 1

    # Return the top 50 most common happiness-related terms
    return happiness_word_freq.most_common(50)

# Call the function to find happiness-related terms in the corpus
top_happiness_terms = find_happiness_terms(corpus)

# Print the top happiness-related terms
print("*happiness")
for word, count in top_happiness_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_struggle_terms(corpus):
    # Define a list of the top fifty most common Spanish struggle or hardship-related terms
    struggle_terms = ["poverty", "unemployment", "stress", "exhaustion", "overwork", "inequality", "disenfranchisement", "exploitation", "insecurity", "uncertainty", "eviction", "foreclosure", "strife", "discontent", "privation", "oppression", "discrimination", "disillusionment", "desperation", "hopelessness", "resistance", "challenge", "adversity", "sacrifice", "strain", "alienation", "isolation", "loneliness", "estrangement", "disadvantage", "injustice", "abuse", "neglect", "abandonment", "victimization", "precariousness", "instability", "shame", "guilt", "depression", "trauma", "loss", "grief", "anguish", "heartache", "disappointment", "frustration"]  # Add more as needed

    # Initialize a Counter to tally occurrences of struggle terms
    struggle_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a struggle term
        if word in struggle_terms:
            struggle_word_freq[word] += 1

    # Return the top 150 most common struggle terms
    return struggle_word_freq.most_common(150)

# Call the function to find struggle terms in the corpus
top_struggle_terms = find_struggle_terms(corpus)

# Print the top 150 struggle terms
print("*hardship")
for word, count in top_struggle_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_health_terms(corpus):
    # Define a list of health-related terms
    health_terms = ["doctor", "nurse", "hospital", "clinic", "medicine", "prescription", "insurance", "appointment", "check-up", "emergency", "pharmacy", "surgery", "ambulance", "patient", "care", "treatment", "therapy", "recovery", "vaccine", "vaccination", "flu", "cold", "fever", "cough", "sore throat", "headache", "pain", "injury", "wound", "bandage", "cast", "physical therapy", "mental health", "diet", "exercise", "weight", "blood pressure", "cholesterol", "diabetes", "asthma", "allergy", "immunity", "virus", "bacteria", "healthcare"]

    # Initialize a Counter to tally occurrences of health-related terms
    health_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a health-related term
        if word in health_terms:
            health_word_freq[word] += 1

    # Return the top 50 most common health-related terms
    return health_word_freq.most_common(50)

# Call the function to find health-related terms in the corpus
top_health_terms = find_health_terms(corpus)

# Print the top 50 health-related terms
print("*health")
for word, count in top_health_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_history_terms(corpus):
    # Define a list of history-related terms
    history_terms = ["ancestors", "traditions", "roots", "lineage", "legacy", "ancestral", "heritage", "culture", "oral history", "ancestral home", "ancestral land", "pioneers", "settlers", "frontiersmen", "colonial", "revolutionary", "founding fathers", "indigenous", "tribal", "historic sites", "historical landmarks", "ancestral knowledge", "historic preservation", "historical records", "local history", "family history", "immigrants", "migrants", "explorers", "trailblazers", "historical events", "ancestral stories", "heritage sites", "cultural heritage", "community history", "historical artifacts", "historical society", "genealogy", "civil rights", "labor history", "historical documents", "archaeology", "historic buildings", "traditional crafts", "ancestral language"]

    # Initialize a Counter to tally occurrences of history-related terms
    history_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a history-related term
        if word in history_terms:
            history_word_freq[word] += 1

    # Return the top 50 most common history-related terms
    return history_word_freq.most_common(50)

# Call the function to find history-related terms in the corpus
top_history_terms = find_history_terms(corpus)

# Print the top 50 history-related terms
print("*history")
for word, count in top_history_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_indigenous_terms(corpus):
    # Define a list of indigenous-related terms specific to tribes of Idaho
    indigenous_terms = ["Shoshone", "Bannock", "Nez Perce", "Coeur d'Alene", "Kootenai", "Salish", "Spokane", "Shoshone-Bannock", "Fort Hall", "Lemhi", "Shoshone-Paiute", "Shoshoni", "Tukudeka", "Sheepeater", "Camas Prairie", "Nimíipuu", "Sahaptin", "Atsina", "Kalispel", "Pend d'Oreille", "Yakama", "Flathead", "Wenatchi", "Methow", "Entiat", "Chelan", "Sinkiuse-Columbia", "Wenatchee", "Palus", "Cayuse", "Umatilla", "Tenino", "Walla Walla", "Nez Percé", "Yakama", "Colville", "Coeur d'Alene", "Spokane", "Columbia", "Snake", "Willamette Valley", "Clearwater", "Salmon River", "Payette", "Boise", "Bruneau", "Owyhee", "Snake River", "Lemhi River"]

    # Initialize a Counter to tally occurrences of indigenous-related terms
    indigenous_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is an indigenous-related term specific to tribes of Idaho
        if word in indigenous_terms:
            indigenous_word_freq[word] += 1

    # Return the top 50 most common indigenous-related terms
    return indigenous_word_freq.most_common(50)

# Call the function to find indigenous-related terms in the corpus
top_indigenous_terms = find_indigenous_terms(corpus)

# Print the top 50 indigenous-related terms
print("*indigenous")
for word, count in top_indigenous_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_manual_labor_terms(corpus):
    # Define a list of the top fifty most common Spanish labor-related terms
    manual_labor_terms = ["Factory", "Shift", "Union", "Worker", "Laborer", "Employee", "Employer", "Job", "Occupation", "Wage", "Salary", "Paycheck", "Hourly", "Daily", "Weekly", "Overtime", "Minimum wage", "Living wage", "Benefits", "Healthcare", "Retirement", "Pension", "Sick leave", "Vacation", "Maternity leave", "Paternity leave", "Paid time off", "Layoff", "Dismissal", "Termination", "Hiring", "Firing", "Training", "Skills", "Experience", "Manual labor", "Blue-collar", "Workplace", "Factory floor", "Assembly line", "Warehouse", "Construction", "Maintenance", "Janitorial", "Service industry", "Hospitality"]  # Add more as needed

    # Initialize a Counter to tally occurrences of labor terms
    manual_labor_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a labor term
        if word in manual_labor_terms:
            manual_labor_word_freq[word] += 1

    # Return the top 150 most common labor terms
    return manual_labor_word_freq.most_common(150)

# Call the function to find labor terms in the corpus
top_manual_labor_terms = find_manual_labor_terms(corpus)

# Print the top 150 labor terms
print("*labor")
for word, count in top_manual_labor_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_migration_terms(corpus):
    # Define a list of migration-related terms
    migration_terms = ["immigration", "emigration", "refugee", "asylum", "naturalization", "resettlement", "integration", "exile", "citizenship", "border", "visa", "deportation", "fleeing", "repatriation", "flight", "transplantation", "dispersion", "exodus", "nomadism", "migrant", "transient", "displacement", "colonization", "settler", "journey", "voyage", "pilgrimage", "relocation", "repopulation", "expatriate", "sojourner", "transmigrating", "travelling", "seeking refuge", "dislocation", "displaced person", "reintegration", "acculturation", "diaspora", "melting pot", "ethnic diversity", "immigrant community", "border crossing", "migration policy", "immigration reform"]

    # Initialize a Counter to tally occurrences of migration-related terms
    migration_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a migration-related term
        if word in migration_terms:
            migration_word_freq[word] += 1

    # Return the top 50 most common migration-related terms
    return migration_word_freq.most_common(50)

# Call the function to find migration-related terms in the corpus
top_migration_terms = find_migration_terms(corpus)

# Print the top 50 migration-related terms
print("*migration")
for word, count in top_migration_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_leisure_terms(corpus):
    # Define a list of leisure-related terms
    leisure_terms = ["leisure", "recreation", "entertainment", "activity", "hobby", "pastime", "sports", "game", "play", "fun", "relaxation", "outdoor", "indoor", "park", "picnic", "barbecue", "camp", "hike", "trail", "fishing", "hunting", "camping", "bonfire", "campfire", "swimming", "pool", "beach", "lake", "river", "boating", "canoeing", "kayaking", "biking", "cycling", "walking", "running", "hiking", "gardening", "photography", "music", "concert", "movie", "film", "theater", "reading", "library", "board game", "card game", "dance", "bbq"]

    # Initialize a Counter to tally occurrences of leisure-related terms
    leisure_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a leisure-related term
        if word in leisure_terms:
            leisure_word_freq[word] += 1

    # Return the top 50 most common leisure-related terms
    return leisure_word_freq.most_common(50)

# Call the function to find leisure-related terms in the corpus
top_leisure_terms = find_leisure_terms(corpus)

# Print the top 50 leisure-related terms
print("*recreation")
for word, count in top_leisure_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_religion_terms(corpus):
    # Define a list of the top fifty most common Spanish religion-related terms
    religion_terms = ["Church", "Temple", "Mosque", "Synagogue", "Prayer", "Worship", "Faith", "Belief", "Spirituality", "Religious", "Devotion", "Ritual", "Ceremony", "Sacred", "Holy", "Blessing", "Preacher", "Minister", "Priest", "Pastor", "Deacon", "Congregation", "Community", "Fellowship", "Charity", "Mission", "Evangelism", "Revival", "Sermon", "Bible", "Scripture", "Quran", "Torah", "Hymn", "Choir", "Religious education", "Sunday school", "Youth group", "Confirmation", "Bar mitzvah", "Bat mitzvah", "Sacrament", "Communion", "Baptism", "Confession", "Repentance", "Salvation"]  # Add more as needed

    # Initialize a Counter to tally occurrences of religion terms
    religion_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a religion term
        if word in religion_terms:
            religion_word_freq[word] += 1

    # Return the top 150 most common religion terms
    return religion_word_freq.most_common(150)

# Call the function to find religion terms in the corpus
top_religion_terms = find_religion_terms(corpus)

# Print the top 150 religion terms
print("*religion")
for word, count in top_religion_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_technology_terms(corpus):
    # Define a list of technology-related terms
    technology_terms = ["Computer", "PC", "Software", "Hardware", "Program", "Code", "Data", "Database", "Network", "Internet", "Website", "Browser", "Operating system", "Application", "Word processor", "Spreadsheet", "Database", "Modem", "Printer", "Scanner", "Fax machine", "VHS", "Cassette", "Walkman", "Tape recorder", "CD player", "Compact disc", "Video game", "Atari", "Nintendo", "Gameboy", "Sega", "Playstation", "Xbox", "Calculator", "Typewriter", "Telephone", "Answering machine", "Pager", "Television", "VCR", "Remote control", "Antenna", "Cable", "Satellite", "Video cassette", "Walkie-talkie", "Walkie", "Radio", "Cassette player", "Boombox", "Turntable", "Vinyl record", "Record player", "Camera", "Polaroid", "Film", "Flashlight", "Calculator", "Pocket calculator", "Calculator watch", "Pocket watch", "Wristwatch", "Microwave", "Toaster", "Blender", "Vacuum cleaner", "Dishwasher", "Washing machine", "Dryer", "Refrigerator", "Air conditioner", "Fan", "Heater", "Thermostat", "Alarm clock"]

    # Initialize a Counter to tally occurrences of technology terms
    technology_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a technology term
        if word in technology_terms:
            technology_word_freq[word] += 1

    # Return the top 150 most common technology terms
    return technology_word_freq.most_common(150)

# Call the function to find technology terms in the corpus
top_technology_terms = find_technology_terms(corpus)

# Print the top 150 technology terms
print("*technology")
for word, count in top_technology_terms:
    print(f"{word.capitalize()}: {count}")