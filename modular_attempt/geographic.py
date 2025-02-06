from collections import Counter
import re

def find_basque_terms(corpus):
    # Define a list of Basque-related terms
    basque_terms = ["Basque", "Basque Country", "Euskadi", "Euskara", "Donostia", "Bilbao", "Vitoria-Gasteiz", "Iruña", "Hondarribia", "Zarautz", "Getaria", "Biarritz", "Bayonne", "Saint-Jean-de-Luz", "Guernica", "Bermeo", "Mutriku", "Ondarroa", "Mundaka", "Lekeitio", "Orio", "Deba", "Zumaia", "Lazkao", "Azpeitia", "Zestoa", "Zarautz", "Hernani", "Amezketa", "Andoain", "Astigarraga", "Ataun", "Beasain", "Errenteria", "Ibarra", "Idiazabal", "Leaburu", "Legazpi", "Leintz-Gatzaga", "Txakoli", "Cider", "Sagardo", "Pintxo", "Pintxos", "Pilota", "Basque pelota", "Jai alai", "Txapela", "Txistorra", "Idiazabal cheese"]

    # Initialize a Counter to tally occurrences of Basque terms
    basque_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Basque terms
    for word in tokens:
        if word.lower() in basque_terms:
            basque_word_freq[word.lower()] += 1

    return basque_word_freq.most_common(5)

# Call the function to find Basque-related terms in the corpus
top_basque_terms = find_basque_terms(corpus)

# Print the top 5 Basque-related terms
print("*basque")
for word, count in top_basque_terms:
    print(f"{word.lower()}: {count}")

from collections import Counter
import re

def find_british_terms(corpus):
    british_terms = ["British", "Britain", "London", "Manchester", "Birmingham", "Liverpool", "Leeds", "Bristol", "Sheffield", "Newcastle", "Cardiff", "Nottingham", "Southampton", "Leicester", "Brighton", "Portsmouth", "Plymouth", "Derby", "York", "Hull", "Middlesbrough", "Northampton", "Luton", "Wolverhampton", "Norwich", "Swansea", "Oxford", "Cambridge", "Exeter", "Yorkshire", "Cornwall", "Essex", "Kent", "Surrey", "Devon", "England"]
    
    british_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with British terms
    for word in tokens:
        # Check for partial matches
        for term in british_terms:
            if term.lower() in word:
                british_word_freq[term.lower()] += 1

    return british_word_freq.most_common(5)

top_british_terms = find_british_terms(corpus)

print("*britain")
for word, count in top_british_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_canadian_terms(corpus):
    canadian_terms = ["Canada", "Canadian", "Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton", "Ottawa", "Winnipeg", "Quebec", "Hamilton", "London", "Victoria", "Halifax", "Regina", "Saskatoon", "St. John's", "Kitchener", "Burnaby", "Windsor", "Richmond", "Burlington", "Surrey", "Mississauga", "Markham", "Brampton", "Vaughan", "Oakville", "Niagara Falls", "Waterloo", "Guelph", "Cambridge", "Kelowna", "Fredericton", "Charlottetown", "Whitehorse", "Yellowknife", "Iqaluit", "Ontario", "Quebec", "Nova Scotia", "New Brunswick", "Manitoba", "British Columbia", "Prince Edward Island", "Saskatchewan", "Alberta", "Newfoundland and Labrador"]

    canadian_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Canadian terms
    for word in tokens:
        # Check for partial matches
        for term in canadian_terms:
            if term.lower() in word:
                canadian_word_freq[term.lower()] += 1

    return canadian_word_freq.most_common(5)

top_canadian_terms = find_canadian_terms(corpus)

print("*canada")
for word, count in top_canadian_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_chinese_terms(corpus):
    chinese_terms = ["Chinese", "China", "Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Tianjin", "Chongqing", "Hangzhou", "Nanjing", "Chengdu", "Wuhan", "Xi'an", "Suzhou", "Dalian", "Qingdao", "Shenyang", "Xiamen", "Changsha", "Zhengzhou", "Dongguan", "Wuxi", "Changchun", "Ningbo", "Kunming", "Nanchang", "Hefei", "Taiyuan", "Jinan", "Guiyang", "Fuzhou", "Harbin", "Hohhot", "Ürümqi", "Lanzhou", "Yinchuan", "Lhasa", "Nanning", "Haikou", "Macau", "Hong Kong", "Taipei", "Macao", "Guilin", "Kashgar", "Shijiazhuang", "Jining"]
    chinese_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Chinese terms
    for word in tokens:
        if word.lower() in chinese_terms:
            chinese_word_freq[word.lower()] += 1

    return chinese_word_freq.most_common(5)

# Call the function to find Chinese-related terms in the corpus
top_chinese_terms = find_chinese_terms(corpus)

# Print the top 5 Chinese-related terms
print("*china")
for word, count in top_chinese_terms:
    print(f"{word.lower()}: {count}")

from collections import Counter
import re

def find_finnish_terms(corpus):
    finnish_terms = ["Finnish", "Finland", "Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu", "Turku", "Jyväskylä", "Kuopio", "Lahti", "Kouvola", "Pori", "Joensuu", "Lappeenranta", "Vaasa", "Hämeenlinna", "Seinäjoki", "Rovaniemi", "Mikkeli", "Kotka", "Salo", "Porvoo", "Lohja", "Hyvinkää", "Järvenpää", "Rauma", "Kokkola", "Kerava", "Kajaani", "Tuusula", "Kirkkonummi", "Seutula", "Sipoo", "Siuntio", "Karkkila", "Vihti", "Nurmijärvi", "Riihimäki", "Raseborg", "Loviisa", "Hanko", "Lohja", "Nastola", "Hollola", "Asikkala"]

    
    finnish_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Finnish terms
    for word in tokens:
        # Check for partial matches
        for term in finnish_terms:
            if term.lower() in word:
                finnish_word_freq[term.lower()] += 1

    return finnish_word_freq.most_common(5)

top_finnish_terms = find_finnish_terms(corpus)

print("*finland")
for word, count in top_finnish_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_french_terms(corpus):
    french_terms = ["French", "France", "Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille", "Rennes", "Reims", "Le Havre", "Cergy", "Saint-Étienne", "Toulon", "Angers", "Grenoble", "Dijon", "Nîmes", "Aix-en-Provence", "Saint-Quentin-en-Yvelines", "Brest", "Le Mans", "Amiens", "Tours", "Limoges", "Clermont-Ferrand", "Villeurbanne", "Besançon", "Orléans", "Metz", "Rouen", "Mulhouse", "Perpignan", "Caen", "Nancy", "Argenteuil", "Saint-Denis", "Roubaix", "Tourcoing", "Avignon", "Poitiers", "Créteil", "Nanterre", "Versailles"]
    
    french_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with French terms
    for word in tokens:
        if word.lower() in french_terms:
            french_word_freq[word.lower()] += 1

    return french_word_freq.most_common(5)

top_french_terms = find_french_terms(corpus)

print("*france")
for word, count in top_french_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_german_terms(corpus):
    german_terms = ["German", "Germany", "Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Düsseldorf", "Dortmund", "Essen", "Leipzig", "Bremen", "Dresden", "Hanover", "Nuremberg", "Duisburg", "Bochum", "Wuppertal", "Bielefeld", "Bonn", "Münster", "Karlsruhe", "Mannheim", "Augsburg", "Wiesbaden", "Gelsenkirchen", "Mönchengladbach", "Braunschweig", "Chemnitz", "Kiel", "Aachen", "Halle", "Magdeburg", "Freiburg", "Krefeld", "Lübeck", "Oberhausen", "Erfurt", "Mainz", "Rostock", "Kassel", "Hagen", "Saarbrücken", "Hamm", "Potsdam", "Leverkusen", "Oldenburg"]

    german_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with German terms
    for word in tokens:
        if word.lower() in german_terms:
            german_word_freq[word.lower()] += 1

    return german_word_freq.most_common(5)

top_german_terms = find_german_terms(corpus)

print("*germany")
for word, count in top_german_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_greek_terms(corpus):
    greek_terms = ["Greek", "Greece", "Athens", "Thessaloniki", "Patras", "Heraklion", "Larissa", "Volos", "Ioannina", "Chania", "Chalcis", "Rethymno", "Serres", "Kavala", "Drama", "Komotini", "Alexandroupoli", "Katerini", "Veria", "Trikala", "Lamia", "Kozani", "Polichni", "Karditsa", "Sykies", "Nea Ionia", "Ioannis", "Agia Paraskevi", "Palaio Faliro", "Tripoli", "Galatsi", "Agrinio", "Chios", "Mytilene", "Kalamata", "Kavala", "Volos", "Larissa", "Heraklion", "Chalkida", "Thiva", "Sparta", "Corfu", "Lamia", "Rhodes", "Karditsa", "Kastoria", "Kavala"]
    greek_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Greek terms
    for word in tokens:
        if word.lower() in greek_terms:
            greek_word_freq[word.lower()] += 1

    return greek_word_freq.most_common(5)

top_greek_terms = find_greek_terms(corpus)

print("*greece")
for word, count in top_greek_terms:
    print(f"{word.lower()}: {count}")

from collections import Counter
import re

def find_geographic_words(corpus):
    # Define a list of geographic place names in Idaho
    idaho_geographic_places = ["Caldwell", "Idaho Falls", "Pocatello", "Rupert", "Boise", "Nampa", "Emmett", "Twin Falls", "Burley", "Moscow", "Lewiston", "Mountain Home", "Blackfoot", "Post Falls", "Sandpoint", "Jerome", "Weiser", "Eagle", "Star", "Middleton", "Rathdrum", "Bonners Ferry", "St. Maries", "Spirit Lake", "Glenns Ferry", "Parma", "Kimberly", "St. Anthony", "Gooding", "McCall", "Driggs", "American Falls", "Grangeville", "Fountain", "Acequia", "Albion", "Arco", "Athol", "Bellevue", "Bloomington", "Bruneau", "Buhl", "Challis", "Clayton", "Clifton", "Cottonwood", "Council", "Crouch", "Culdesac", "Dayton", "Dover", "Downey", "Drummond", "Dubois", "Elk City", "Fairfield", "Fenn", "Fernwood", "Fort Hall", "Franklin", "Fruitland", "Garden City", "Genesee", "Grace", "Greenleaf", "Hagerman", "Hansen", "Hazelton", "Heyburn", "Holbrook", "Homedale", "Horseshoe Bend", "Huetter", "Huston", "Inkom", "Iona", "Julietta", "Kamiah", "Kendrick", "Ketchum", "Kooskia", "Kootenai", "Kuna", "Lapwai", "Lava Hot Springs", "Leadore", "Lemhi", "Letha", "Lost River", "Mackay", "Malad City", "Malta", "Marsing", "Melba", "Menan", "Mink Creek", "Montpelier", "Monteview", "Montour", "Moore", "Mountain Home AFB", "Mud Lake", "Mullan", "Murtaugh", "Newdale", "New Meadows", "New Plymouth", "Nezperce", "Notus", "Oakley", "Oldtown", "Onaway", "Orofino", "Osburn", "Paris", "Parker", "Parkline", "Paul", "Payette", "Peck", "Picabo", "Pinehurst", "Placerville", "Plummer", "Pollock", "Potlatch", "Preston", "Priest Lake", "Priest River", "Rexburg", "Richfield", "Rigby", "Rimini", "Riverside", "Rockford", "Rockland", "Sagle", "Salmon", "Shelley", "Shoshone", "Smelterville", "Soda Springs", "Spalding", "Spencer", "Stanley", "Sugar City", "Sun Valley", "Swan Valley", "Terry", "Teton", "Tetonia", "Troy", "Uhland", "Victor", "Wallace", "Wardner", "Warm River", "Weippe", "Wendell", "Weston", "White Bird", "Wilder", "Winchester", "Worley"]  

    # Initialize a Counter to tally occurrences of geographic place names
    geographic_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a geographic place name in Idaho
        if word in idaho_geographic_places:
            geographic_word_freq[word] += 1

    # Return the top 150 most common geographic place names in Idaho
    return geographic_word_freq.most_common(150)

# Call the function to find geographic words in the corpus
top_geographic_words = find_geographic_words(corpus)

# Print the top 150 geographic place names in Idaho
print("*idaho")
for word, count in top_geographic_words:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_indian_terms(corpus):
    indian_terms = ["Indian", "India", "Hindi", "New Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune", "Ahmedabad", "Surat", "Jaipur", "Kanpur", "Lucknow", "Nagpur", "Patna", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Vadodara", "Firozabad", "Ludhiana", "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot", "Varanasi", "Srinagar", "Aurangabad", "Dhanbad", "Amritsar", "Navi Mumbai", "Allahabad", "Ranchi", "Howrah", "Jabalpur", "Gwalior", "Vijayawada", "Jodhpur", "Raipur", "Kota", "Guwahati", "Chandigarh"]
    indian_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Indian terms
    for word in tokens:
        if word.lower() in indian_terms:
            indian_word_freq[word.lower()] += 1

    return indian_word_freq.most_common(5)

# Call the function to find Indian-related terms in the corpus
top_indian_terms = find_indian_terms(corpus)

# Print the top 5 Indian-related terms
print("*india")
for word, count in top_indian_terms:
    print(f"{word.lower()}: {count}")

from collections import Counter
import re

def find_irish_terms(corpus):
    irish_terms = ["Irish", "Ireland", "Dublin", "Cork", "Galway", "Limerick", "Waterford", "Drogheda", "Dundalk", "Bray", "Navan", "Kilkenny", "Ennis", "Carlow", "Tralee", "Newbridge", "Portlaoise", "Balbriggan", "Naas", "Athlone", "Mullingar", "Celbridge", "Wexford", "Letterkenny", "Sligo", "Clonmel", "Greystones", "Malahide", "Carrigaline", "Leixlip", "Lucan", "Skerries", "Tramore", "Killarney", "Arklow", "Kilcock", "Ballina", "Castlebar", "Maynooth", "Thurles", "Monaghan", "Mallow", "Portarlington", "Buncrana", "Gorey", "Tuam", "Cobh", "potato famine"]
    
    irish_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Irish terms
    for word in tokens:
        # Check for partial matches
        for term in irish_terms:
            if term.lower() in word:
                irish_word_freq[term.lower()] += 1

    return irish_word_freq.most_common(5)

top_irish_terms = find_irish_terms(corpus)

print("*ireland")
for word, count in top_irish_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_italian_terms(corpus):
    italian_terms = ["Italian", "Italy", "Rome", "Milan", "Naples", "Turin", "Palermo", "Genoa", "Bologna", "Florence", "Bari", "Catania", "Venice", "Verona", "Messina", "Padua", "Trieste", "Taranto", "Brescia", "Prato", "Reggio", "Modena", "Reggio", "Emilia", "Perugia", "Livorno", "Ravenna", "Cagliari", "Foggia", "Rimini", "Salerno", "Ferrara", "Sassari", "Latina", "Giugliano", "Monza", "Syracuse", "Bergamo", "Pescara", "Trento", "Forlì", "Vicenza", "Terni", "Bolzano", "Novara", "Piacenza", "Ancona", "Andria", "Udine"]
    italian_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Italian terms
    for word in tokens:
        if word.lower() in italian_terms:
            italian_word_freq[word.lower()] += 1

    return italian_word_freq.most_common(5)

top_italian_terms = find_italian_terms(corpus)

print("*italy")
for word, count in top_italian_terms:
    print(f"{word.lower()}: {count}")

from collections import Counter
import re

def find_japanese_terms(corpus):
    japanese_terms = ["Japanese", "Japan", "Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo", "Fukuoka", "Kobe", "Kyoto", "Kawasaki", "Saitama", "Hiroshima", "Sendai", "Kitakyushu", "Chiba", "Sakai", "Niigata", "Hamamatsu", "Okayama", "Kumamoto", "Sagamihara", "Kagoshima", "Matsumoto", "Kanazawa", "Naha", "Matsuyama", "Kōchi", "Naha", "Nagasaki", "Toyama", "Otsu", "Wakayama", "Akita", "Aomori", "Asahikawa", "Fukushima", "Fukui", "Gifu", "Hachinohe", "Hakodate", "Higashiosaka", "Himeji", "Iwaki", "Iwakuni", "Kōfu", "Kure"]
    japanese_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Japanese terms
    for word in tokens:
        if word.lower() in japanese_terms:
            japanese_word_freq[word.lower()] += 1

    return japanese_word_freq.most_common(5)

# Call the function to find Japanese-related terms in the corpus
top_japanese_terms = find_japanese_terms(corpus)

# Print the top 5 Japanese-related terms
print("*japan")
for word, count in top_japanese_terms:
    print(f"{word.lower()}: {count}")

from collections import Counter
import re

def find_mexican_terms(corpus):
    mexican_terms = ["Mexico", "Mexican", "Mexico City", "Guadalajara", "Monterrey", "Puebla", "Tijuana", "León", "Ciudad Juárez", "Chihuahua", "Cancún", "Mérida", "Aguascalientes", "Querétaro", "Toluca", "Hermosillo", "San Luis Potosí", "Culiacán", "Acapulco", "Morelia", "Saltillo", "Veracruz", "Villahermosa", "Tuxtla Gutiérrez", "Durango", "Tepic", "Colima", "Campeche", "La Paz", "Torreón", "Mazatlán", "Reynosa", "Matamoros", "Celaya", "Irapuato", "Nuevo Laredo", "Ensenada", "Coatzacoalcos", "Oaxaca", "Tlalnepantla", "Tampico", "Cuernavaca", "Zacatecas", "Uruapan", "Nogales", "Pachuca", "Cuautitlán", "Tapachula", "Delicias"]
    mexican_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Mexican terms
    for word in tokens:
        if word.lower() in [term.lower() for term in mexican_terms]:
            mexican_word_freq[word.lower()] += 1

    return mexican_word_freq.most_common(5)

# Call the function to find Mexican-related terms in the corpus
top_mexican_terms = find_mexican_terms(corpus)

# Print the top 5 Mexican-related terms
print("*mexico")
for word, count in top_mexican_terms:
    print(f"{word.lower()}: {count}")

from collections import Counter
import re

def find_norwegian_terms(corpus):
    norwegian_terms = ["Norwegian", "Norway", "Oslo", "Bergen", "Trondheim", "Stavanger", "Kristiansand", "Tromsø", "Drammen", "Fredrikstad", "Skien", "Sandnes", "Sarpsborg", "Bodø", "Ålesund", "Haugesund", "Moss", "Porsgrunn", "Arendal", "Tønsberg", "Hamar", "Ytre Enebakk", "Halden", "Larvik", "Askøy", "Kongsberg", "Harstad", "Molde", "Steinkjer", "Lillehammer", "Gjøvik", "Kristiansund", "Narvik", "Horten", "Leirvik", "Mandal", "Voss", "Ski", "Mo i Rana", "Namsos", "Lillestrøm", "Sandefjord", "Hønefoss", "Egersund", "Kongsvinger", "Raufoss", "Rjukan"]

    norwegian_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Norwegian terms
    for word in tokens:
        # Check for partial matches
        for term in norwegian_terms:
            if term.lower() in word:
                norwegian_word_freq[term.lower()] += 1

    return norwegian_word_freq.most_common(5)

top_norwegian_terms = find_norwegian_terms(corpus)

print("*norway")
for word, count in top_norwegian_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_philippine_terms(corpus):
    philippine_terms = ["Philippines", "Filipino", "Tagalog", "Manila", "Quezon City", "Davao City", "Caloocan", "Cebu City", "Zamboanga City", "Antipolo", "Pasig", "Taguig", "Cagayan de Oro", "Parañaque", "Valenzuela", "Las Piñas", "Makati", "Bacolod", "Muntinlupa", "Iloilo City", "Tarlac City", "Baguio", "Batangas City", "General Santos", "Lapu-Lapu", "Iligan", "Olongapo", "Binan", "Santa Rosa", "Tagum", "Tacloban", "Malolos", "Navotas", "Dagupan", "Toledo", "Lucena", "San Fernando", "Cabanatuan", "Ormoc", "Dasmariñas", "San Juan", "Baliuag", "Tuguegarao", "Malabon", "Mabalacat", "Cotabato City", "Puerto Princesa", "Butuan"]
    philippine_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Philippine terms
    for word in tokens:
        if word.lower() in philippine_terms:
            philippine_word_freq[word.lower()] += 1

    return philippine_word_freq.most_common(5)

# Call the function to find Philippine-related terms in the corpus
top_philippine_terms = find_philippine_terms(corpus)

# Print the top 5 Philippine-related terms
print("*philippines")
for word, count in top_philippine_terms:
    print(f"{word.lower()}: {count}")

from collections import Counter
import re

def find_polish_terms(corpus):
    polish_terms = ["Polish", "Poland", "Warsaw", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok", "Katowice", "Gdynia", "Częstochowa", "Radom", "Sosnowiec", "Toruń", "Kielce", "Rzeszów", "Gliwice", "Zabrze", "Olsztyn", "Bielsko-Biała", "Bytom", "Zielona Góra", "Rybnik", "Tarnów", "Opole", "Gorzów", "Dąbrowa", "Górnictwo", "Elbląg", "Płock", "Wałbrzych", "Chorzów", "Tychy", "Jaworzno", "Jastrzębie", "Zdrój", "Mysłowice", "Legnica", "Lubin", "Siedlce", "Inowrocław", "Piotrków", "Trybunalski", "Ostrołęka"]
    polish_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Polish terms
    for word in tokens:
        if word.lower() in polish_terms:
            polish_word_freq[word.lower()] += 1

    return polish_word_freq.most_common(5)

top_polish_terms = find_polish_terms(corpus)

print("*poland")
for word, count in top_polish_terms:
    print(f"{word.lower()}: {count}")

from collections import Counter
import re

def find_portuguese_terms(corpus):
    portuguese_terms = [
        "Portuguese", "Portugal", "Lisbon", "Porto", "Vila Nova", "Amadora", "Braga", 
        "Funchal", "Coimbra", "Setúbal", "Queluz", "Agualva-Cacém", "Aveiro", "Viseu", 
        "Amora", "Rio Tinto", "Matosinhos", "Évora", "Castelo Branco", "Guimarães", 
        "Vila Franca", "Santarém", "Vila do Conde", "Ponte de Lima", "Loures", 
        "Póvoa de Varzim", "Faro", "Sever do Vouga", "Paredes", "Penafiel", "Lagos", 
        "Odivelas", "Ovar", "Maia", "Beja", "Gondomar", "Covilhã", "Águeda", "Fafe", 
        "Almada", "Elvas", "Torres Vedras", "Loulé", "Portalegre", "Barcelos", 
        "Caldas da Rainha", "Leiria"
    ]
    
    portuguese_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Portuguese terms
    for word in tokens:
        if word.lower() in portuguese_terms:
            portuguese_word_freq[word.lower()] += 1

    return portuguese_word_freq.most_common(5)

top_portuguese_terms = find_portuguese_terms(corpus)

print("*portugal")
for word, count in top_portuguese_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_scottish_terms(corpus):
    scottish_terms = ["Scottish", "Scotland", "Edinburgh", "Glasgow", "Aberdeen", "Dundee", "Inverness", "Stirling", "Perth", "Fife", "Falkirk", "Ayr", "East Kilbride", "Livingston", "Cumbernauld", "Kilmarnock", "Greenock", "Coatbridge", "Glenrothes", "Airdrie", "Kirkcaldy", "Hamilton", "Dunfermline", "Dumfries", "Motherwell", "Paisley", "Renfrew", "Irvine", "Giffnock", "Newton Mearns", "Cambuslang", "Barrhead", "Blantyre", "Stranraer", "Bellshill", "Kirkintilloch", "Wishaw", "Nairn", "Buckie", "Portree", "Inverurie", "Alloa", "Bathgate", "Dingwall", "Elgin", "Fort William", "Hawick", "Jedburgh"]
    
    scottish_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Scottish terms
    for word in tokens:
        # Check for partial matches
        for term in scottish_terms:
            if term.lower() in word:
                scottish_word_freq[term.lower()] += 1

    return scottish_word_freq.most_common(5)

top_scottish_terms = find_scottish_terms(corpus)

print("*scotland")
for word, count in top_scottish_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_spanish_terms(corpus):
    spanish_terms = ["Spanish", "Spain", "Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza", "Málaga", "Murcia", "Palma", "Las Palmas", "Bilbao", "Alicante", "Córdoba", "Valladolid", "Vigo", "Gijón", "L'Hospitalet", "A Coruña", "Vitoria", "Granada", "Elche", "Oviedo", "Badalona", "Terrassa", "Cartagena", "Sabadell", "Jerez", "Móstoles", "Santa Cruz", "Alcalá", "Fuenlabrada", "Almería", "Leganés", "San Sebastián", "Getafe", "Burgos", "Albacete", "Santander", "Castellón", "Logroño", "Badajoz", "Huelva", "Salamanca", "Lérida", "Tarragona", "León"]

    
    spanish_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Spanish terms
    for word in tokens:
        if word.lower() in spanish_terms:
            spanish_word_freq[word.lower()] += 1

    return spanish_word_freq.most_common(5)

top_spanish_terms = find_spanish_terms(corpus)

print("*spain")
for word, count in top_spanish_terms:
    print(f"{word.capitalize()}: {count}")

from collections import Counter
import re

def find_swedish_terms(corpus):
    swedish_terms = ["Swedish", "Swede", "Swedes", "Scandinavian", "Stockholm", "Sweden", "Gothenburg", "Malmö", "Uppsala", "Linköping", "Norrköping", "Örebro", "Västerås", "Helsingborg", "Jönköping", "Umeå", "Lund", "Borås", "Sundsvall", "Gävle", "Östersund", "Eskilstuna", "Södertälje", "Halmstad", "Växjö", "Karlstad", "Trollhättan", "Örnsköldsvik", "Kalmar", "Kristianstad", "Falun", "Borlänge", "Skövde", "Karlskrona", "Visby", "Luleå", "Tumba", "Märsta", "Alingsås", "Östersund", "Vänersborg", "Täby", "Hässleholm", "Trelleborg", "Nyköping", "Piteå", "Lidingö"]

    swedish_word_freq = Counter()

    # Tokenize the corpus to handle multi-word expressions
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over tokens and check for matches with Swedish terms
    for word in tokens:
        # Check for partial matches
        for term in swedish_terms:
            if term.lower() in word:
                swedish_word_freq[term.lower()] += 1

    return swedish_word_freq.most_common(50)

top_swedish_terms = find_swedish_terms(corpus)

print("*swedish")
for word, count in top_swedish_terms:
    print(f"{word.capitalize()}: {count}")