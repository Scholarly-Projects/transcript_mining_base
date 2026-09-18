import os
import re
import string
from collections import Counter

import pandas as pd
import nltk
from nltk.corpus import stopwords

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

A_DIR = os.path.join(BASE_DIR, "A")
B_DIR = os.path.join(BASE_DIR, "B")
C_DIR = os.path.join(BASE_DIR, "C")

for folder in (A_DIR, B_DIR, C_DIR):
    os.makedirs(folder, exist_ok=True)

USE_ENGLISH_STOPWORDS = True
USE_SPANISH_STOPWORDS = False
USE_FRENCH_STOPWORDS = False
USE_PORTUGUESE_STOPWORDS = False
USE_GERMAN_STOPWORDS = False
USE_ITALIAN_STOPWORDS = False

nltk.download('stopwords', quiet=True)

_LANGUAGE_TOGGLES = {
    'english': USE_ENGLISH_STOPWORDS,
    'spanish': USE_SPANISH_STOPWORDS,
    'french': USE_FRENCH_STOPWORDS,
    'portuguese': USE_PORTUGUESE_STOPWORDS,
    'german': USE_GERMAN_STOPWORDS,
    'italian': USE_ITALIAN_STOPWORDS,
}

stop_words = set()
for _language, _enabled in _LANGUAGE_TOGGLES.items():
    if _enabled:
        stop_words |= set(stopwords.words(_language))

# Minimum word length for the general frequency scan below.
MIN_WORD_LENGTH = 5

TEXT_COLUMN = "words"

TAGS = {
    "agriculture": {
        "enabled": True,
        "terms": [
            "acreage", "apiary", "apple fruit", "baler", "barn building",
            "berry", "cattle", "combine harvester", "compost", "corn maize",
            "crop", "crop rotation", "dairy", "farm field", "farmhand",
            "farming", "farming equipment", "fertilizer", "garden", "gmo",
            "grain crop", "harvest", "hay", "hoe", "homestead", "honey",
            "irrigation", "livestock", "manure", "milking", "orchard",
            "pasture", "plow", "potato", "poultry", "ranch", "rural", "seed",
            "shovel", "silage", "soybean", "sustainable", "thresher",
            "tractor", "weeding", "wheat",
        ],
    },
    "animal": {
        "enabled": False,
        "terms": [
            "badger", "bear", "beaver", "bison", "bluebird", "buck",
            "buffalo", "chicken", "chipmunk", "cougars", "coyote", "crow",
            "doe", "duck", "eagle", "ewe", "ferret", "finch", "fox", "frog",
            "gaggle", "goat", "gopher", "hawk", "hawks", "herd", "horse",
            "lamb", "lizard", "marmot", "mink", "moose", "mountain lions",
            "muskrat", "newt", "otter", "owl", "paw", "pig", "possum",
            "prairie dog", "quail", "rabbit", "raccoon", "raven", "salamander",
            "salmon", "skunk", "snake", "sparrow", "squirrel",
            "stag", "steelhead", "toad", "turkey", "weasel", "whale",
            "wolf", "wolves",
        ],
    },
    "basque": {
        "enabled": True,
        "terms": [
            "amezketa", "andoain", "astigarraga", "ataun", "azpeitia",
            "basque", "basque pelota", "beasain", "bermeo", "biarritz",
            "bilbao", "deba", "donostia", "errenteria", "euskadi", "euskara",
            "getaria", "guernica", "hernani", "hondarribia", "ibarra",
            "idiazabal", "idiazabal cheese", "iruña", "jai alai", "lazkao",
            "leaburu", "legazpi", "leintz-gatzaga", "lekeitio", "mundaka",
            "mutriku", "ondarroa", "orio", "pilota", "pintxo", "pintxos",
            "sagardo", "saint-jean-de-luz", "txakoli", "txapela", "txistorra",
            "vitoria-gasteiz", "zarautz", "zestoa", "zumaia",
        ],
    },
    "british": {
        "enabled": True,
        "terms": [
            "birmingham", "brighton", "bristol", "britain", "british",
            "cambridge", "cardiff", "cornwall", "devon", "england", "essex",
            "exeter", "hull", "leeds", "leicester", "liverpool", "london",
            "luton", "manchester", "middlesbrough", "newcastle", "northampton",
            "norwich", "nottingham", "oxford", "plymouth", "portsmouth",
            "sheffield", "southampton", "swansea", "wolverhampton",
            "yorkshire",
        ],
    },
    "canadian": {
        "enabled": True,
        "terms": [
            "brampton", "burlington", "burnaby", "calgary", "cambridge",
            "canada", "canadian", "charlottetown", "edmonton", "fredericton",
            "guelph", "halifax", "iqaluit", "kelowna", "kitchener", "manitoba",
            "markham", "mississauga", "montreal", "new brunswick",
            "niagara falls", "nova scotia", "oakville", "ontario", "ottawa",
            "quebec", "regina", "richmond", "saskatoon", "st. john's",
            "toronto", "vancouver", "vaughan", "victoria", "waterloo",
            "whitehorse", "windsor", "winnipeg", "yellowknife",
        ],
    },
    "chinese": {
        "enabled": False,
        "terms": [
            "beijing", "Bing Kong Tong", "changchun", "changsha", "china", "chinese",
            "chongqing", "dalian", "dongguan", "fuzhou", "guangzhou", "guilin",
            "guiyang", "haikou", "hangzhou", "harbin", "hefei", "hohhot",
            "hong kong", "Hop Sing", "jinan", "jining", "kashgar", "lanzhou",
            "lhasa", "macao", "macau", "nanchang", "nanjing", "nanning",
            "ningbo", "qingdao", "shanghai", "shenyang", "shenzhen",
            "shijiazhuang", "Suey Sing Tongs", "suzhou", "taipei", "taiyuan", "Tong War",
            "wuxi", "xi'an", "xiamen", "yinchuan", "zhengzhou", "ürümqi",
        ],
    },
    "cinema": {
        "enabled": True,
        "terms": [
            "actor", "actress", "animation", "antagonist", "blockbuster",
            "cameo", "camerawork", "cinema", "cinematography",
            "close-up", "closing credits", "dialogue", "documentary",
            "editing", "feature film", "film noir", "frame",
            "independent film", "long shot", "mid shot", "montage", "movie",
            "movie theater", "narrative", "opening credits", "picture show",
            "producer", "protagonist", "scene", "screenplay", "screenwriter",
            "script", "short film", "silent film", "soundtrack",
            "special effects", "storyline", "stunt", "tracking shot",
            "visual effects", "voice-over", "wide shot",
        ],
    },
    "clothing": {
        "enabled": True,
        "terms": [
            "alterations", "apparel", "apron", "boots", "cap", "clothing",
            "cotton", "denim", "department store", "fabric", "fashion",
            "flannel", "gloves", "hat", "jacket", "jeans", "outerwear",
            "outfit", "overalls", "pants", "plaid", "polyester", "retail",
            "scarf", "seamstress", "secondhand", "shoes", "shopping", "skirt",
            "sneakers", "socks", "stitching", "sweater", "t-shirt", "tailor",
            "thrift", "underwear", "uniform", "wardrobe", "workwear",
        ],
    },
    "crime": {
        "enabled": True,
        "terms": [
            "addiction", "arrest", "arson", "assault", "bribery", "burglary",
            "conviction", "corruption", "crime", "detective", "detention",
            "distribution", "domestic violence", "drugs", "embezzlement",
            "extortion", "forensics", "forgery", "fraud", "gambling", "gangs",
            "homicide", "identity theft", "illegal immigration",
            "imprisonment", "interrogation", "investigation",
            "money laundering", "murder", "officer", "parole", "plea bargain",
            "police", "possession", "probation", "prostitution",
            "racketeering", "rape", "recidivism", "rehabilitation", "robbery",
            "sentencing", "theft", "trafficking", "trial", "vandalism",
            "violence",
        ],
    },
    "culture": {
        "enabled": True,
        "terms": [
            "belonging", "celebration", "community centers", "crafts",
            "craftsmanship", "cuisine", "cultural exchange",
            "cultural identity", "cultural pride", "customs", "dialect",
            "diversity", "ethnic neighborhoods", "ethnicity", "festivals",
            "folk art", "folk dance", "folklore", "folktales", "gathering",
            "gatherings", "inclusion", "legends", "local traditions",
            "multiculturalism", "neighborhood", "oral tradition", "parades",
            "rituals", "socializing", "street fairs", "tradition",
        ],
    },
    "economic": {
        "enabled": True,
        "terms": [
            "advancement", "application", "apprenticeship", "blue-collar",
            "budgeting", "cover letter", "craftsman", "credit loan", "debt",
            "dismissal", "earnings", "employee benefits", "employment",
            "financial planning", "great depression", "hiring", "income",
            "investment", "job interview", "job search", "layoff",
            "livelihood", "loan", "manual labor", "mortgage", "paycheck",
            "pension", "profession", "promotion", "redundancy",
            "resume document", "retirement", "retrenchment", "salary",
            "salary increase", "savings", "skilled trade", "termination",
            "vocation", "wage", "white-collar",
        ],
    },
    "education": {
        "enabled": True,
        "terms": [
            "academia", "administrator", "assignment", "athletics",
            "back-to-school night", "certificate", "classroom", "counselor",
            "curriculum", "degree", "diploma", "exam", "extracurricular",
            "field trip", "financial aid", "grade", "graduation", "grant",
            "group work", "homework", "individualized education plan (iep)",
            "learning", "library", "literacy", "loan", "numeracy",
            "open house", "parent-teacher conference", "peer review",
            "principal", "prom", "report card", "research", "resource center",
            "scholarship", "school", "special education", "student", "study",
            "teacher", "test", "textbook", "tutoring", "work-study program",
        ],
    },
    "environment": {
        "enabled": True,
        "terms": [
            "air pollution", "beaches", "biodiversity", "carbon footprint",
            "climate", "climate change", "conservation", "coral reefs",
            "deforestation", "desertification", "drought", "ecology",
            "ecosystem", "ecotourism", "endangered species",
            "energy efficiency", "environmental activism",
            "environmental awareness", "environmental education",
            "environmental impact", "environmental policy",
            "environmental regulation", "flood", "forests",
            "geothermal energy", "glaciers", "global warming", "grasslands",
            "green spaces", "greenhouse gases", "habitat destruction",
            "hydropower", "lakes", "land conservation", "land degradation",
            "land use", "marine life", "mountains", "natural disaster",
            "natural resources", "nature", "ocean conservation", "oceans",
            "ozone depletion", "pollution", "recycling", "renewable energy",
            "rivers", "rural development", "sea level rise", "soil pollution",
            "solar energy", "sustainability", "sustainable development",
            "tundra", "urbanization", "waste management", "water conservation",
            "water pollution", "water scarcity", "wetlands", "wildlife",
            "wind energy",
        ],
    },
    "family": {
        "enabled": True,
        "terms": [
            "adopted child", "adoptive parent", "aunt", "boyfriend", "brother",
            "child", "child support", "cousin", "custody", "divorce",
            "domestic partner", "family dinner", "family gathering",
            "family tradition", "father", "fiance", "fiancee", "foster child",
            "foster parent", "girlfriend", "grandchild", "grandfather",
            "grandmother", "grandparent", "guardian", "husband",
            "legal guardian", "marriage", "mother", "nephew", "niece",
            "orphan", "parent", "partner", "sibling", "single parent",
            "sister", "spouse", "step-brother", "step-parent", "step-sibling",
            "step-sister", "stepchild", "uncle", "wedding", "wife",
        ],
    },
    "finnish": {
        "enabled": True,
        "terms": [
            "asikkala", "espoo", "finland", "finnish", "hanko", "helsinki",
            "hollola", "hyvinkää", "hämeenlinna", "joensuu", "jyväskylä",
            "järvenpää", "kajaani", "karkkila", "kerava", "kirkkonummi",
            "kokkola", "kotka", "kouvola", "kuopio", "lahti", "lappeenranta",
            "lohja", "loviisa", "mikkeli", "nastola", "nurmijärvi", "oulu",
            "pori", "porvoo", "raseborg", "rauma", "riihimäki", "rovaniemi",
            "salo", "seinäjoki", "seutula", "sipoo", "siuntio", "suomalainen",
            "suomi", "tampere", "turku", "tuusula", "vaasa", "vantaa", "vihti",
        ],
    },
    "food_and_drink": {
        "enabled": True,
        "terms": [
            "applesauce", "bacon", "baked beans", "beef", "beer", "biscuit",
            "bread", "butter", "buttermilk", "cake", "candy", "cheese",
            "chicken", "chocolate", "cider", "coffee", "cookies", "cornbread",
            "doughnuts", "eggs", "flapjacks", "fruit spread", "ham",
            "hardtack", "huckleberries", "ice cream", "jam", "jelly", "jerky",
            "lard", "marmalade", "milk", "molasses", "moonshine", "mush",
            "mutton", "pepper", "pickles", "pie", "pork", "rabbit", "raisins",
            "root beer", "salad", "salmon", "salt", "salt pork",
            "sarsaparilla", "sausage", "soda", "sorghum", "soup", "sourdough",
            "stew", "tea", "trout", "venison", "vinegar", "whiskey",
        ],
    },
    "french": {
        "enabled": True,
        "terms": [
            "aix-en-provence", "amiens", "angers", "argenteuil", "avignon",
            "besançon", "bordeaux", "brest", "caen", "cergy",
            "clermont-ferrand", "créteil", "dijon", "france", "french",
            "grenoble", "le havre", "le mans", "lille", "limoges", "lyon",
            "marseille", "metz", "montpellier", "mulhouse", "nanterre",
            "nantes", "nîmes", "orléans", "perpignan", "poitiers", "reims",
            "rennes", "roubaix", "rouen", "saint-denis",
            "saint-quentin-en-yvelines", "saint-étienne", "strasbourg",
            "toulon", "toulouse", "tourcoing", "versailles", "villeurbanne",
        ],
    },
    "geographic": {
        "enabled": False,
        "terms": [
            "acequia", "albion", "american falls", "arco", "athol", "bellevue",
            "blackfoot", "bloomington", "boise", "bonners ferry", "bruneau",
            "buhl", "burley", "caldwell", "challis", "clayton", "clifton",
            "cottonwood", "council, idaho", "crouch", "culdesac",
            "dayton, idaho", "dover", "downey", "driggs", "drummond", "dubois",
            "eagle, idaho", "elk city", "emmett", "fairfield", "fenn",
            "fernwood", "fort hall", "fountain, idaho", "fruitland",
            "garden city", "genesee", "glenns ferry", "gooding", "grangeville",
            "greenleaf", "hagerman", "hansen, idaho", "hazelton", "heyburn",
            "holbrook", "homedale", "horseshoe bend", "huetter",
            "huston, idaho", "idaho falls", "inkom", "iona", "jerome, idaho",
            "julietta", "kamiah", "kendrick, idaho", "ketchum", "kimberly",
            "kooskia", "kootenai", "kuna", "lapwai", "lava hot springs",
            "leadore", "lemhi", "letha", "lewiston", "lost river", "mackay",
            "malad city", "malta", "marsing", "mccall, idaho", "melba, idaho",
            "menan", "middleton", "mink creek", "monteview", "montour",
            "montpelier", "moore, idaho", "moscow", "mountain home",
            "mountain home afb", "mud lake", "mullan", "murtaugh", "nampa",
            "new meadows", "new plymouth", "newdale", "nezperce, idaho",
            "notus", "oakley", "oldtown", "onaway", "orofino", "osburn, idaho",
            "parker", "parkline", "parma", "payette", "peck", "picabo",
            "pinehurst", "placerville", "plummer", "pocatello", "pollock",
            "post falls", "potlatch", "preston", "priest lake", "priest river",
            "rathdrum", "rexburg", "richfield", "rigby", "rimini", "riverside",
            "rockford", "rockland", "rupert", "sagle", "sandpoint",
            "shelley, idaho", "shoshone", "smelterville", "soda springs",
            "spalding", "spencer", "spirit lake", "st. anthony", "st. maries",
            "stanley, idaho", "sugar city", "sun valley", "swan valley",
            "terry, idaho", "teton", "tetonia", "troy, idaho", "twin falls",
            "uhland", "victor, idaho", "wallace, idaho", "wardner",
            "warm river", "weippe", "weiser", "wendell", "weston",
            "white bird", "wilder", "winchester", "worley",
        ],
    },
    "german": {
        "enabled": False,
        "terms": [
            "aachen", "augsburg", "berlin", "bielefeld", "bochum", "bonn",
            "braunschweig", "bremen", "chemnitz", "cologne", "dortmund",
            "dresden", "duisburg", "düsseldorf", "erfurt", "essen",
            "frankfurt", "freiburg", "gelsenkirchen", "german", "germany",
            "hagen", "halle", "hamburg", "hamm", "hanover", "karlsruhe",
            "kassel", "kiel", "krefeld", "leipzig", "leverkusen", "lübeck",
            "magdeburg", "mainz", "mannheim", "munich", "mönchengladbach",
            "münster", "nuremberg", "oberhausen", "oldenburg", "potsdam",
            "rostock", "saarbrücken", "stuttgart", "wiesbaden", "wuppertal",
        ],
    },
    "greek": {
        "enabled": True,
        "terms": [
            "agia paraskevi", "agrinio", "alexandroupoli", "athens", "chalcis",
            "chalkida", "chania", "chios", "corfu", "galatsi", "greece",
            "greek", "heraklion", "ioannina", "ioannis", "kalamata",
            "karditsa", "kastoria", "katerini", "kavala", "komotini", "kozani",
            "lamia", "larissa", "mytilene", "nea ionia", "palaio faliro",
            "patras", "polichni", "rethymno", "serres", "sparta", "sykies",
            "thessaloniki", "thiva", "trikala", "tripoli", "veria", "volos",
        ],
    },
    "health": {
        "enabled": True,
        "terms": [
            "ague", "allergy", "ambulance", "amputation", "apoplexy",
            "appointment", "asthma", "bacteria", "bandage", "blood poisoning",
            "blood pressure", "body weight", "Bright's disease", "catarrh",
            "check up", "childbed fever", "cholera", "cholesterol", "clinic",
            "colic", "consumption", "cough", "croup", "diabetes", "diet plan",
            "diphtheria", "doctor", "dropsy", "dysentery", "dyspepsia",
            "emergency", "flu", "gangrene", "goiter", "headache", "healthcare",
            "hospital", "hydrophobia", "infantile paralysis", "influenza",
            "injury", "insurance", "lockjaw", "malaria", "measles", "medicine",
            "mental health", "mumps", "neurasthenia", "nurse", "pain",
            "pharmacy", "physical therapy", "pneumonia", "prescription",
            "quinsy", "rabies", "recovery", "scarlet fever", "smallpox",
            "sore throat", "Spanish flu", "spotted fever", "surgery", "TB",
            "therapy", "treatment", "tuberculosis", "typhoid fever",
            "vaccination", "vaccine", "virus", "whooping cough", "workout",
            "yellow fever",
        ],
    },
    "history": {
        "enabled": True,
        "terms": [
            "ancestors", "ancestral", "ancestral home", "ancestral knowledge",
            "ancestral land", "ancestral language", "archaeology",
            "civil rights", "colonial", "community history",
            "cultural heritage", "explorers", "family history",
            "founding fathers", "frontiersmen", "genealogy", "heritage",
            "heritage sites", "historic buildings", "historic preservation",
            "historic sites", "historical artifacts", "historical documents",
            "historical events", "historical landmarks", "historical records",
            "historical society", "labor history", "legacy", "lineage",
            "local history", "oral history", "pioneers", "revolutionary",
            "settlers", "traditional crafts", "traditions", "trailblazers",
        ],
    },
    "indigenous": {
        "enabled": False,
        "terms": [
            "atsina", "bannock", "bruneau indian", "camas prairie",
            "cayuse indian", "chelan indian", "clearwater indian",
            "coeur d'alene indian", "columbia indian", "colville indian",
            "entiat indian", "flathead", "fort hall indian", "indigenous",
            "kalispel indian", "kootenai", "lemhi", "lemhi river indian",
            "methow", "native american", "nez perce", "nez percé", "nimíipuu",
            "owyhee", "palus", "payette indian", "pend d'oreille",
            "reservation", "sahaptin", "salish", "salmon river indian",
            "sheepeater", "shoshone", "shoshone-bannock", "shoshone-paiute",
            "shoshoni", "sinkiuse-columbia", "snake river indian",
            "spokane indian", "tenino indian", "tribe", "tukudeka",
            "umatilla indian", "walla walla indian", "wenatchee indian",
            "wenatchi", "willamette valley indian", "yakama indian",
        ],
    },
    "irish": {
        "enabled": True,
        "terms": [
            "arklow", "athlone", "balbriggan", "ballina", "bray", "buncrana",
            "carlow", "carrigaline", "castlebar", "celbridge", "clonmel",
            "cobh", "drogheda", "dublin", "dundalk", "ennis", "galway",
            "gorey", "greystones", "ireland", "irish", "kilcock", "kilkenny",
            "killarney", "leixlip", "letterkenny", "limerick", "lucan",
            "malahide", "maynooth", "monaghan", "mullingar", "naas", "navan",
            "newbridge", "portarlington", "portlaoise", "potato famine",
            "skerries", "sligo", "thurles", "tralee", "tramore", "tuam",
            "waterford", "wexford",
        ],
    },
    "italian": {
        "enabled": True,
        "terms": [
            "ancona", "andria", "bari", "bergamo", "bolzano", "brescia",
            "cagliari", "catania", "emilia", "ferrara", "florence", "foggia",
            "forlì", "genoa", "giugliano", "italian", "italy", "latina",
            "livorno", "messina", "milan", "modena", "monza", "naples",
            "novara", "padua", "palermo", "perugia", "pescara", "piacenza",
            "prato", "ravenna", "reggio", "rimini", "rome", "salerno",
            "sassari", "taranto", "terni", "trento", "trieste", "turin",
            "udine", "venice", "verona", "vicenza",
        ],
    },
    "japanese": {
        "enabled": True,
        "terms": [
            "akita", "aomori", "asahikawa", "chiba", "fukui", "fukuoka",
            "fukushima", "gifu", "hachinohe", "hakodate", "hamamatsu",
            "higashiosaka", "himeji", "hiroshima", "iwaki", "iwakuni", "japan",
            "japanese", "kagoshima", "kanazawa", "kawasaki", "kitakyushu",
            "kobe", "kumamoto", "kure", "kyoto", "kōchi", "kōfu", "matsumoto",
            "matsuyama", "nagasaki", "nagoya", "naha", "niigata", "okayama",
            "osaka", "otsu", "sagamihara", "saitama", "sakai", "sapporo",
            "sendai", "tokyo", "toyama", "wakayama", "yokohama",
        ],
    },
    "LCOH Chinese": {
        "enabled": True,
        "terms": [
            "Beijing", "Bing Kong Tong", "Changchun", "Changsha", "Chengdu",
            "China", "Chinese", "Chongqing", "Dalian", "Dongguan", "Fuzhou",
            "Guangzhou", "Guilin", "Guiyang", "Haikou", "Hangzhou", "Harbin",
            "Hefei", "Hip Sing Tong", "Hohhot", "Hong Kong", "Jinan", "Jining",
            "Kashgar", "Kunming", "Lanzhou", "Lhasa", "Macao", "Macau",
            "Nanchang", "Nanjing", "Nanning", "Ningbo", "Qingdao", "Shanghai",
            "Shenyang", "Shenzhen", "Shijiazhuang", "Suzhou", "Taipei",
            "Taiyuan", "Tianjin", "Wuhan", "Wuxi", "Xi'an", "Xiamen",
            "Yinchuan", "Zhengzhou", "Ürümqi",
        ],
    },
    "LCOH Corporations": {
            "enabled": True,
            "terms": [
                "American Trust", "Anderson Bros. Bank", "Arnold & Olson",
                "Bank of Aberdeen", "Bank of Juliaetta", "Beaumont & Rust",
                "Beeler & Price", "Bennett Bros.", "Berg & Johnson",
                "Blackwell Lumber", "Boise City National Bank", "Boise Lumber",
                "Bonner County National Bank", "Brewerton C. A. & Sons",
                "Bruneau State Bank", "Buhl Bank & Trust", "Burley State Bank",
                "Caldwell Commercial Bank", "Caldwell Lumber", "Cann & Steltz",
                "Citizens National Bank of Salmon", "Citizens' Coal",
                "Clay & Murphy", "Coeur d'Alene Lumber", "Coffin Lester",
                "Coltman Lumber", "Commercial Cream",
                "Consolidated Wagon & Machine", "Cottonwood Lumber",
                "Cracker & Herbert", "Craig Mountain Lumber",
                "Crowley & Balderson", "D. L. Evans", "Dalberg P. I. & Son",
                "Deary Lumber", "Denlinger Coal & Ice", "Dernham and Kaufmann",
                "Diamond Drill Contracting", "Dryad Lumber",
                "Eagle Creek Pine Lumber", "Emory Bros.", "Exchange National Bank",
                "Farmers Mill & Lumber", "First Bank of Genesee",
                "First Bank of Troy", "Gallogly Undertaking Parlor",
                "Gallup Lumber Yard", "Gem State Lumber", "Genesee Exchange Bank",
                "Genesee Telephone", "German State Bank", "Grant Lumber",
                "Groseclose & Richardson", "Harris & Natwick", "Hawkins W. B.",
                "Henderson & Mitchell", "Hodgin's Drug", "Humbird Lumber",
                "Idaho Light & Power", "Idaho Lumber", "Idaho National Bank",
                "Idaho State & Savings Bank", "Idaho Trust & Savings Bank",
                "Iowa Lumber", "Juliaetta Hardware", "Juliaetta Mercantile",
                "Juliaetta Milling & Light", "Kamiah Lumber", "Kendrick Store",
                "Kendrick Warehouse & Milling", "Kendrick-Rochdale",
                "Lacy & Malloy", "Lapwai Lumber", "Latah County State Bank",
                "Lewiston National Bank", "Lincoln Hardware & Implement",
                "Long N. B. & Son", "Lukens & Getchell", "McGillis & Gibbs",
                "McGoldrick Lumber", "Milner-Perrine Lumber", "Milwaukee Lumber",
                "Moscow Hardware Commission", "Moscow Manufacturing",
                "Moscow State Bank", "Moscow Union Warehouse",
                "Nibley-Channel Lumber", "Niles & Needham", "North Idaho Gas",
                "Olson & Johnson", "Ostrander Lumber",
                "Pacific National Bank of Boise", "Panhandle Lumber",
                "Pioneer Bank & Trust", "Pleasant Home", "Polson Logging",
                "Potlatch Brick", "Potlatch Lumber", "Potlatch State Bank",
                "Rosauers", "Russell & Pugh Lumber",
                "Rutledge Lumber and Manufacturing", "Sewell J. M.",
                "Shattuck & Hughes", "Siegrist Milling", "Simmons & Noble",
                "Sprague E. C. & Son", "Sprague Sanitary Preserving",
                "St. Joe Boom", "Stack-Gibbs Lumber", "Standard Lumber",
                "Studebaker Bros. of Utah", "Swearingen & Wilson", "Troy Laundry",
                "Troy Lumber", "Troy Lumber & Manufacturing",
                "Twin Falls Bank & Trust", "Twin Falls Lumber",
                "Utah-Idaho Elevator", "Vandervanter Bros.", "Vollmer-Clearwater",
                "Warren & Anderson Furniture",
                "Washington, Idaho & Montana Railway", "Weiser Loan & Trust",
                "Weiser National Bank", "Weyerhaeuser Timber", "White Pine Mill",
                "White Pine Trading", "WI&M", "Winters and Godsworth",
                "Winton Lumber", "Wright-Wilkie Lumber",
            ],
    },
    "LCOH Eastern European": {
        "enabled": True,
        "terms": [
            "Bohemian", "Bohunk", "Bull Hunk", "Croat", "Czech",
            "Hungarian", "Hunk", "Hunkie", "Hunky", "Polack",
            "Rooshian", "Russian", "Ruthenian", "Serbian", "Slav", "Slavic",
            "Slavonian", "Slovack", "Slovak",
        ],
    },
    "LCOH Flora & Fauna": {
        "enabled": True,
        "terms": [
            "Appaloosa", "Badger", "Bear Den", "Beaver", "Belgian horse",
            "Bison", "Bitterroot", "Blister Rust", "Bluebird", "Buck",
            "Buffalo", "Bunchgrass", "Camas", "Cayuse", "Chicken",
            "Chipmunk", "Chokecherry", "Clydesdale", "Cougars", "Cous",
            "Coyote", "Crow", "Doe", "Duck", "Eagle", "Ewe", "Ferret", "Finch",
            "Fox", "Frog", "Gaggle", "Goat", "Gopher", "Hawk", "Hawks", "Herd",
            "Herefords", "Horse", "Huckleberry", "Kinnikinnick", "Lamb",
            "Lizard", "Marmot", "Mink", "Moose", "Morgan", "Mountain Lions",
            "Muskrat", "Newt", "Otter", "Owl", "Paw", "Percherons", "Pig",
            "Ponderosa Pine", "Possum", "Prairie Dog", "Quail",
            "Quarter Horse", "Rabbit", "Raccoon", "Raven", "Ribes",
            "Sagebrush", "Salamander", "Salmon Hatchery", "Sarvisberry",
            "Shadbush", "Shire", "Skunk", "Smudge Fire", "Snake Bite",
            "Sparrow", "Squirrel", "Stag", "Steelhead", "Syringa", "Tamarack",
            "Toad", "Turkey", "Weasel", "Whale Pod", "Wolf Pack", "Wolves",
            "Yampa",
        ],
    },
    "LCOH German": {
        "enabled": True,
        "terms": [
            "Aachen", "Augsburg", "Berlin", "Bielefeld", "Bochum", "Bonn",
            "Braunschweig", "Bremen", "Chemnitz", "Cologne", "Dortmund",
            "Dresden", "Duisburg", "Düsseldorf", "Erfurt", "Essen",
            "Frankfurt", "Freiburg", "Gelsenkirchen", "German", "Germany",
            "Hagen", "Halle", "Hamburg", "Hamm", "Hanover", "Karlsruhe",
            "Kassel", "Kiel", "Krefeld", "Leipzig", "Leverkusen", "Lübeck",
            "Magdeburg", "Mainz", "Mannheim", "Munich", "Mönchengladbach",
            "Münster", "Nuremberg", "Oberhausen", "Oldenburg", "Plautdietsch",
            "Potsdam", "Rostock", "Saarbrücken", "Stuttgart", "Wiesbaden",
            "Wuppertal",
        ],
    },
    "LCOH Indigenous": {
        "enabled": True,
        "terms": [
            "Atsina", "Bannock", "Blackfeet", "Bruneau Indian", "Burns Paiute",
            "Camas Prairie", "Cayuse Indian", "Chehalis Indian",
            "Chelan Indian", "Chinook Indian", "Clatsop", "Clearwater Indian",
            "Coast Salish", "Coeur d'Alene Indian", "Columbia Indian",
            "Colville Indian", "Coos", "Coquille", "Cowlitz", "Duwamish",
            "Entiat Indian", "Flathead", "Fort Hall Indian", "Grand Ronde",
            "Hoh", "Indigenous", "Interior Salish", "Kalispel Indian",
            "Klamath Indian", "Klickitat", "Kootenai", "Lemhi",
            "Lemhi River Indian", "Lummi", "Makah", "Methow", "Modoc",
            "Molalla", "Native American", "Nez Perce", "Nez Percé", "Nimíipuu",
            "Nisqually", "Nooksack", "Northern Paiute", "Okanagan Indian",
            "Owyhee", "Palus", "Payette Indian", "Pend d'Oreille", "Puyallup",
            "Quileute", "Quinault", "Reservation", "Sahaptin", "Salish",
            "Salmon River Indian", "Samish", "San Poil", "Sheepeater",
            "Shoshone", "Shoshone-Bannock", "Shoshone-Paiute", "Shoshoni",
            "Siletz", "Sinixt", "Sinkiuse-Columbia", "Skagit", "Skokomish",
            "Skookum", "Snake River Indian", "Snoqualmie Indian",
            "Spokane Indian", "Squaxin Island", "Stillaguamish", "Suquamish",
            "Swinomish", "Tenino Indian", "Tillamook", "Tribe", "Tribal", "Tukudeka",
            "Tulalip", "Umatilla Indian", "Umpqua", "Walla Walla Indian",
            "Wanapum", "Warm Springs Indian", "Wasco Indian",
            "Wenatchee Indian", "Wenatchi", "Western Shoshone",
            "Willamette Valley Indian", "Yakama Indian",
        ],
    },
    "LCOH Mining": {
        "enabled": True,
        "terms": [
            "Assay", "Blasting", "Coal Seam", "Conveyor Belt", "Dredging",
            "Drift Mining", "Drilling", "Environmental Impact", "Excavation",
            "Explosive Charge", "Extraction", "Extraction Rate",
            "Flotation Process", "Fracking", "Geological Survey",
            "Geotechnical Analysis", "Hard Rock Mining", "Haul Truck",
            "Heap Leaching", "Hydraulic Fracturing", "Hydrometallurgy",
            "Jigger", "Jumbo", "Longwall Mining", "Marions", "Mine Closure",
            "Mine Drainage", "Mine Reclamation", "Mine Safety",
            "Mine Ventilation", "Miner's Lamp", "Mineral Deposit", "Mining",
            "Mining Permit", "Oilers", "Open Pit", "Ore", "Ore Body",
            "Ore Grade", "Placer Mining", "Powder Men", "Processing Plant",
            "Prospecting", "Pyrometallurgy", "Quarrying", "Reclamation Bond",
            "Refining", "Rock Fragmentation", "Room and Pillar", "Roustabout",
            "Shaft Sinking", "Slope Mining", "Slurry", "Smelting",
            "Strip Mining", "Strip Ratio", "Tailings", "Tunneling",
            "Underground Mining", "Walking Boss",
        ],
    },
    "LCOH Organizations": {
        "enabled": True,
        "terms": [
            "Coxey's Army", "Coxeyites", "Daughters of Rebekah",
            "Emergency Relief Administration", "Flying squad",
            "Foster School of Healing", "Grand Army of the Republic",
            "Hayu Club", "Idaho Emergency Relief Administration", "IERA",
            "Independent Order of Odd Fellows",
            "International Workers of the World", "IOOF", "IWW", "K of P",
            "Kiwanis", "Kiwanis Club", "KKK", "Klan", "Knights of Pythias",
            "Knights of the Maccabees", "Ku Klux Klan", "Ladies Aid",
            "Ladies Auxiliary", "Ladies' Auxiliaries", "Maccabee Lodge",
            "Maccabees", "Odd Fellows", "Odd Fellows Hall", "Pioneer Club",
            "Psychiana", "QAE Club", "Rebekah Lodge", "Rebekahs",
            "Runt Club Skating Party", "Soroptimist Club", "Soroptimists",
            "WCTU", "Wobblies", "Women of the Woodcraft",
            "Women's Christian Temperance Union", "Woodman of the World",
            "Woodmen of the World",
        ],
    },
    "LCOH People": {
        "enabled": True,
        "terms": [
            "Aaron Levi", "Albert Justice", "Allison W. Laird", "Andrew Bloom",
            "Anna Webster Litle", "August Leising", "Axel Anderson", "Big Gil",
            "Big Gil Pippen", "Bill Morland", "Billy Marsh", "Broken Ass John",
            "Broomface Brooks", "Butterfly Pete", "C.B. Green", "C.G. Naugle",
            "Cecil Emmet", "Charles Bolles", "Clay Hall Brown",
            "Clifford M. Drury", "Cougar Jack", "Cryin' Gus", "Cumberford",
            "Dick Farrell", "Dirty Shirt Martin", "Doc White", "Dode Holmes",
            "Ed Allen", "Ed Hill", "Frank Tom", "Friedrich Weyerhaeuser",
            "Gene Chinaman", "George Creighton", "George McKinnon",
            "Harry Adams", "Henry Flasher", "Henry Plummer", "Herman Byers",
            "Hurdy-Gurdy Girls", "Ira Jenks", "J.P. Wahlberg",
            "Jackson Sundance", "Jacob Rosenstein", "Jake Rosenstein",
            "Joe Buck", "Joe Rivers", "Joe Wells", "John P. Vollmer",
            "Laughin' Mike", "Laughing Jim Delaney", "Lillian Cooks",
            "Lynn Henry", "M.F. Zumhof", "Malcher Anderson", "Mike Bubley",
            "Milford Welch", "Missy Lee", "Mox Herzog", "Mox-Mox",
            "Nick the Greek", "Old Codger Jack", "Old George Foss",
            "Old Gil Pippen", "Old Joe Davis", "Old John Grohl",
            "Old Sundown Jackson", "Ole Bohman",
            "Ollie Vincent", "Pack Sack Dick", "Palouser", "Pat Malone",
            "Pete Olson", "Platten Bomberg", "Powderpuff Johnny",
            "Powderpuff McDonald", "Prune Joe", "Red Watson", "Ridge Runner",
            "Robert Foster", "Rosenstein's", "Sam McKeon", "Sam Piwash",
            "Sam Samovich", "Samuel T. Red Rosie Joe", "Sells-Floto Circus",
            "Seven Jackets", "Shefflins", "Shorty Justice", "Shorty Trimble",
            "Sleigh Hall Brown", "Swan Erikson", "T.P. Jones", "Ted Collins",
            "The Big Swede", "The Nordic Queen", "Tilly Pelton", "Tom Hopkins",
            "Uncle Ben", "Walking Daily", "Warner H. Carithers",
            "Whitliff R. Smith", "Wild Davey", "William Deary",
            "William Helmer", "Wood 'em Up George",
        ],
    },
    "LCOH Places": {
        "enabled": True,
        "terms": [
            "acequia", "aggipah mountain", "ahsahka", "albion", "almota",
            "alsea", "american falls", "american ridge", "anderson",
            "andersonville prison", "angel ridge", "arco", "asotin",
            "aspendale", "athol", "bald mountain", "beals butte", "bear creek",
            "beartrack creek", "beeson meadows", "bellevue", "benewah county",
            "bergen, norway", "big bear ridge", "blackfoot", "bloomington",
            "bluestem", "boise", "bonanza", "bonners ferry", "bovard",
            "bovill", "box and goose", "bremerton", "bruneau", "buhl",
            "burley", "burnt ridge", "buzzard roost", "caldwell", "cameron",
            "camp kenjockety", "cashup davis hotel", "cavendish",
            "cedar ridge", "challis", "chatcolet lake", "chehalis", "cheney",
            "cherry butte", "christianson meadow", "clarkia", "clarkston",
            "clarksville", "clayton", "clifton", "cloquet, minnesota",
            "coeur d'alene", "collins", "colton", "corral creek", "cottonwood",
            "council, idaho", "craigmont", "cranbrook, bc", "crouch",
            "crumarine gulch", "culdesac", "cusick", "dayton, idaho", "deary",
            "dogger", "dover", "downey", "driggs", "driscoll ridge",
            "drummond", "dry ridge", "dublin", "dubois", "dworshak dam",
            "eagle, idaho", "elk city", "elk river", "ellensburg", "emida",
            "emmett", "endicott", "ephrata", "fairfield", "fairview", "fenn",
            "fernwood", "fix ridge", "fort hall", "fountain, idaho",
            "fourmile creek", "frazier", "frederickson", "fruitland",
            "gang saw", "garden city", "garfield", "genesee", "ghormley",
            "gifford", "gilt edge mine", "glenns ferry", "gooding",
            "grangeville", "greenleaf", "hagerman", "hampton", "hansen, idaho",
            "harvard", "hatter creek", "hayden", "hazelton", "helmer",
            "heyburn", "hog meadow creek", "holbrook", "homedale",
            "hood river", "hoodoo", "hoodoo mountains", "hope", "hoquiam",
            "horseshoe bend", "howell", "huetter", "huston, idaho",
            "idaho falls", "idler's rest", "inkom", "iona", "jerome, idaho",
            "juliaetta", "julietta", "kamiah", "kelly creek",
            "kendrick, idaho", "ketchum", "kibbie dome", "kimberly", "kooskia",
            "kootenai", "kuna", "laclede", "lake gamlin", "lake waha",
            "lapwai", "lapwai reservation", "larkins lake", "larkins peak",
            "lava hot springs", "leadore", "leavenworth", "leland", "lemhi",
            "letha", "lewiston", "linville", "little bear ridge",
            "lochsa river", "lolo pass, mo", "lost river", "luella mine",
            "mackay", "malad city", "malta", "marsing", "mccall, idaho",
            "mcgary butte", "melba, idaho", "melrose ridge", "menan",
            "metaline falls", "mica mountain", "mica peak", "middleton",
            "mink creek", "mizpah mine", "moeller", "monteview", "montour",
            "montpelier", "moore, idaho", "moose creek", "moscow",
            "mountain home", "mountain home afb", "mud lake", "mullan",
            "murtaugh", "muscovite mine", "nampa", "nespelem", "new meadows",
            "new plymouth", "newdale", "nezperce, idaho", "nora", "notus",
            "oakley", "okanagan", "oldtown", "omak", "onaway", "orofino",
            "osburn, idaho", "oviatt meadows", "owyhee mountains",
            "paradise ridge", "parker", "parkline", "parma", "payette",
            "payette lake", "peck", "pedicord", "pembine", "picabo",
            "pinehurst", "placerville", "plummer", "pocatello", "pollock",
            "pomeroy", "post falls", "potato hill", "potlatch", "preston",
            "priest lake", "priest river", "princeton", "pullman",
            "randall flat", "randall flat creek", "rathdrum", "reardan",
            "rexburg", "richfield", "ridenbaugh canal", "rigby", "rimini",
            "riparia", "ritzville", "riverside", "rockford", "rockland",
            "rosalia", "rosenstein store", "rupert", "sacheen lake", "sagle",
            "saint maries", "salubria", "sand mountain", "sandpoint",
            "sausalito", "scoville", "selway-bitterroot wilderness",
            "shea meadows", "shelley, idaho", "shoshone", "silverton",
            "slabtown", "smelterville", "snoqualmie falls", "soda springs",
            "sodaville", "sotin creek", "southwick", "spalding", "spangle",
            "spencer", "spirit lake", "spokane", "st. anthony", "st. maries",
            "stanley, idaho", "steptoe butte", "stites", "sugar city",
            "sun valley", "swamp creek", "swan valley", "teakean butte",
            "tensed", "terry, idaho", "teton", "tetonia", "texas ridge",
            "tomer butte", "toppenish", "troy, idaho", "twin falls", "uhland",
            "uniontown", "vassar meadows", "victor, idaho", "viola", "vollmer",
            "waha lake", "walla walla", "wallace, idaho", "wardner",
            "warm river", "weippe", "weiser", "wenatchee", "wendell",
            "west fork", "weston", "white bird", "whitmore school", "wilder",
            "wilson creek", "winchester", "woodfell", "worley", "yale",
            "yreka mining district",
        ],
    },
    "LCOH Play": {
        "enabled": True,
        "terms": [
            "Andy Over", "Basket Socials", "Bean Bake", "Bierstammtisch",
            "Bullfrog on the Bank", "Chautauquas", "Cheeky Pins", "Chesters",
            "Coasting Parties", "Darebase", "Debates", "Decoration Day",
            "Dialogues", "Do-si-do", "Drop the Handkerchief", "Fan-Tan",
            "Flinch and Muggins", "Flinch Muggins Stock Exchange Card Game",
            "Flying Dutchman", "Guess the Skull", "Gustafs Skål",
            "Gustav's Skoal", "Hambo", "Kitchen Sweats", "Kris Krinkles",
            "Leapfrog", "Literaries", "Miller Boy", "Mumblety-Peg",
            "Old Mother Pigeon", "Pie Social", "Piecake-a-Mile", "Pinochle",
            "Pom-Pom-Pull-Away", "Potlatch Days", "Pump Pump Pullway",
            "Puss in the Corner", "Pussy Wants a Corner", "Quadrilles",
            "Quilting Parties", "Reading Room", "Rinky Dinks", "Run Sheep Run",
            "Schottische", "Sells Floto Circus", "Shinny",
            "Shinny On Your Own Side", "Shivaree", "Skip to My Lou",
            "Snipe Hunting", "Spin the Platter", "Spud Hill", "Three Deep",
            "Toboggan Parties", "Vanilla Bar", "Virginia Reel", "Wink 'Em",
            "Winkum", "Winter Fox and Goose",
        ],
    },
    "LCOH Romani": {
        "enabled": True,
        "terms": [
            "Gipsy", "Gypsies", "Gypsy", "Roma", "Romani", "Romany", "Vardo",
        ],
    },
    "LCOH Rural Schools": {
        "enabled": True,
        "terms": [
            "Applequist", "Brannon", "Buckhorn School", "Elwood", "Fern Hill",
            "Liberty School", "Pleasant Hill", "Rimrock",
            "Spring Valley School", "Steele School", "Taney",
        ],
    },
    "LCOH Swedish": {
        "enabled": True,
        "terms": [
            "Alingsås", "Borlänge", "Borås", "Eskilstuna", "Falun",
            "Fattigmann", "Gothenburg", "Gävle", "Halmstad", "Helsingborg",
            "Hässleholm", "Jönköping", "Kalmar", "Karlskrona", "Karlstad",
            "Kristianstad", "Lidingö", "Linköping", "Luleå", "Lund", "Malmö",
            "Märsta", "Norrköping", "Nyköping", "Ostkaka", "Piteå",
            "Scandinavian", "Skövde", "Stockholm", "Sundsvall", "Swede",
            "Sweden", "Swedes", "Swedish", "Södertälje", "Trelleborg",
            "Trollhättan", "Täby", "Umeå", "Uppsala", "Visby", "Vänersborg",
            "Västerås", "Växjö", "Örebro", "Örnsköldsvik", "Östersund",
        ],
    },
    "LCOH Thrashing": {
        "enabled": True,
        "terms": [
            "Band Cutter", "Belt Pulley", "Binder", "Blower", "Bundle",
            "Bundle Pitcher", "Bundle Wagon", "Bundling", "Chaff",
            "Combine Harvester", "Cook Car", "Cook Shack", "Custom Thresher",
            "Feeder", "Grain Harvest", "Grain Sack", "Grain Wagon",
            "Harvest Crew", "Header Box", "Header Puncher",
            "Sack Sewer", "Self-Feeder", "Separator", "Separator Man", "Sheaf",
            "Sheaves", "Shockers", "Shocking", "Spike Pitcher",
            "Stacker", "Steam Engine", "Stook", "Straw Stack", "Thrasher",
            "Thrashing Crews", "Threshing", "Threshing Machine",
            "Threshing Run", "Traction Engine", "Water Boy", "Water Wagon",
            "Weigher", "Wheat Harvest",
        ],
    },
    "LCOH Timber": {
        "enabled": True,
        "terms": [
            "Air Drying", "Bateau", "Beam", "Board Foot", "Boom", "Boom Stick",
            "Buffer Strip", "Bullgang", "Cant Hook", "Catface", "Cat Skinner", "Chainsaw",
            "Check-Scaler", "Chipboard", "Choke-Setter", "Clear Cutting",
            "Crawler", "Crosscut", "Cruiser", "Debarking", "Deforestation",
            "Derrick Team", "Dogging", "Dray Logging", "Draymen",
            "Driving Crew", "Edgeman", "Felling", "Flume", "Flunkeying",
            "Flunkies", "Forest Conservation", "Forestry", "Go-devil", "Gyppo",
            "Gyppoed", "Gyppoing", "Hardwood", "Hectare Yield", "Highline Man",
            "Hooker", "Jammer", "Jungle", "Jungling-Up", "Kiln Drying", "Lath",
            "Log Chute", "Log Jam", "Log Scaler", "Log Yard", "Logging",
            "Logging Permit", "Lumber", "Lumber Grading", "Milling Process",
            "NACCCA",
            "North American Civilian Conservation Corps Alumni Association",
            "Peavey", "Pirating", "Plank", "Plywood", "Pond Duck", "Pulpwood",
            "Reforestation", "Rip Cut", "Rollway", "Roughlock", "Sawing",
            "Sawmill", "Selective Cutting", "Silviculture", "Skidder",
            "Softwood", "Sorting Boom", "Sorting Gaps", "Splash Dam",
            "Streamside", "Stumpage", "Sustainable Forestry", "Swamping",
            "Timber", "Timber Cruiser", "Timber Frame", "Timber Stand",
            "Timberland", "Tree Farm", "Tree Felling", "Undercutter", "Veneer",
            "Wood Grain", "Wood Preservation", "Wood Processing",
            "Wood Treatment", "Woodlot", "Woodworker",
        ],
    },
    "leisure": {
        "enabled": True,
        "terms": [
            "activity", "adventure", "barbecue", "basketball", "beach", "biking",
            "board game", "boating", "bonfire", "campfire", "camping",
            "canoeing", "card game", "cycling", "dance", "dancing", "entertainment",
            "fishing", "football", "fun", "game", "gardening", "hike", "hiking", "hobby",
            "hunting", "kayaking", "lake", "leisure", "marathon", "pastime", "photography",
            "picnic", "pool", "recreation", "relaxation", "ski", "sports",
            "swimming",
        ],
    },
    "literature": {
        "enabled": True,
        "terms": [
            "allegory", "alliteration", "author", "autobiography", "biography",
            "classic literature", "criticism", "dialogue", "draft", "editing",
            "epic poem", "epilogue", "essayist", "fable", "fiction",
            "flashback", "folktale", "foreshadowing", "free verse",
            "genre fiction", "haiku", "irony", "literary theory", "literature",
            "manuscript", "memoir", "metaphor", "mythology", "narrative",
            "nonfiction", "novel", "novella", "playwright", "plot", "poetry",
            "prologue", "prose", "publishing", "short story", "simile",
            "sonnet", "symbolism", "theme", "verse", "writer",
        ],
    },
    "manual_labor": {
        "enabled": True,
        "terms": [
            "assembly line", "blue-collar", "construction", "daily wage",
            "dismissal", "employee", "employer", "factory", "factory floor",
            "firing", "health insurance", "hiring", "hourly wage",
            "janitorial", "labor union", "laborer", "layoff", "living wage",
            "maintenance", "manual labor", "maternity leave", "minimum wage",
            "overtime", "paid time off", "paternity leave", "paycheck",
            "pension", "retirement", "salary", "service industry",
            "service worker", "sick leave", "termination", "training", "union",
            "vacation", "vocation", "wage", "warehouse", "weekly wage",
            "worker", "workplace",
        ],
    },
    "manufacturing": {
        "enabled": True,
        "terms": [
            "3d printing", "additive manufacturing", "assembly line",
            "assembly process", "automation process", "batch production",
            "casting", "cnc machining", "computer-aided design",
            "computer-aided manufacturing", "continuous improvement",
            "die casting", "equipment maintenance", "extrusion", "fabrication",
            "factory layout", "forging", "industrial engineering",
            "industrial robotics", "industrial safety", "injection molding",
            "inventory management", "just-in-time", "kaizen",
            "labor productivity", "lean manufacturing", "lean process",
            "machine calibration", "machining", "manufacturing",
            "mass production", "material handling", "molding",
            "operational efficiency", "precision engineering",
            "process optimization", "production planning",
            "production workflow", "prototyping", "quality assurance",
            "quality control", "raw materials", "sheet metal", "six sigma",
            "standardization", "supply chain", "tooling", "welding",
            "workstation",
        ],
    },
    "mexican": {
        "enabled": True,
        "terms": [
            "acapulco", "aguascalientes", "campeche", "cancún", "celaya",
            "chihuahua", "ciudad juárez", "coatzacoalcos", "colima",
            "cuautitlán", "cuernavaca", "culiacán", "delicias", "durango",
            "ensenada", "guadalajara", "hermosillo", "irapuato", "la paz",
            "león", "matamoros", "mazatlán", "mexican", "mexico",
            "mexico city", "monterrey", "morelia", "mérida", "nogales",
            "nuevo laredo", "oaxaca", "pachuca", "puebla", "querétaro",
            "reynosa", "saltillo", "san luis potosí", "tampico", "tapachula",
            "tepic", "tijuana", "tlalnepantla", "toluca", "torreón",
            "tuxtla gutiérrez", "uruapan", "veracruz", "villahermosa",
            "zacatecas",
        ],
    },
    "migration": {
        "enabled": True,
        "terms": [
            "acculturation", "asylum", "border", "border crossing",
            "citizenship", "colonization", "deportation", "diaspora",
            "dislocation", "dispersion", "displaced person", "displacement",
            "emigration", "ethnic diversity", "exile", "exodus", "expatriate",
            "fleeing", "hobo", "immigrant community", "immigration",
            "immigration reform", "integration", "journey", "melting pot",
            "migrant", "migration policy", "naturalization", "nomadism",
            "pilgrimage", "refugee", "reintegration", "relocation",
            "repatriation", "repopulation", "resettlement", "seeking refuge",
            "settler", "sojourner", "transient", "transmigrating",
            "transplantation", "visa", "voyage",
        ],
    },
    "mining": {
        "enabled": False,
        "terms": [
            "assay", "blasting", "coal seam", "conveyor belt", "dredging",
            "drift mining", "drilling", "environmental impact", "excavation",
            "explosive charge", "extraction", "extraction rate",
            "flotation process", "fracking", "geological survey",
            "geotechnical analysis", "hard rock mining", "haul truck",
            "heap leaching", "hydraulic fracturing", "hydrometallurgy",
            "longwall mining", "mine closure", "mine drainage",
            "mine reclamation", "mine safety", "mine ventilation",
            "miner's lamp", "mineral deposit", "mining", "mining permit",
            "open pit", "ore", "ore body", "ore grade", "placer mining",
            "processing plant", "prospecting", "pyrometallurgy", "quarrying",
            "reclamation bond", "refining", "rock fragmentation",
            "room and pillar", "shaft sinking", "slope mining", "slurry",
            "smelting", "strip mining", "strip ratio", "tailings", "tunneling",
            "underground mining",
        ],
    },
    "music_and_theater": {
        "enabled": True,
        "terms": [
            "accordion", "acoustics", "actor", "actress", "arpeggio",
            "autoharp", "backstage", "banjo", "bass fiddle", "blocking",
            "box office", "brass instrument", "break character",
            "breath control", "broadway", "bugle", "cadence", "chamber music",
            "character actor", "choir", "chord", "clarinet", "cold reading",
            "comedy", "composition", "concert", "concertina", "cornet",
            "costume", "counterpoint", "crescendo", "curtain call",
            "decrescendo", "drama", "dramaturgy", "dress rehearsal", "drum",
            "dulcimer", "dynamics", "ear training", "ensemble", "epilogue",
            "exit stage", "fiddle", "flute", "fourth wall", "guitar",
            "guitar technique", "harmonica", "harmony", "house lights",
            "improvisation", "ingenue", "interval", "juvenile",
            "key signature", "leading lady", "leading man", "lighting design",
            "little eva", "mandolin", "matinee", "melodeon", "melodrama",
            "melody", "method acting", "monologue", "music", "music theory",
            "musical phrasing", "notation", "off-broadway", "orchestra",
            "orchestration", "percussion", "piano", "piano technique",
            "playwright", "prologue", "pump organ", "recital", "rehearsal",
            "resonance", "rhythm", "score study", "set design",
            "sight reading", "simon legree", "soliloquy", "soloist",
            "soubrette", "sound design", "stage", "stage directions",
            "stage presence", "standing ovation", "string instrument",
            "tech rehearsal", "tempo", "theater", "timbre", "time signature",
            "trombone", "tuba", "uncle tom", "understudy", "upstage",
            "vibrato", "villain", "violin", "vocal training", "woodwind",
        ],
    },
    "norwegian": {
        "enabled": True,
        "terms": [
            "arendal", "askøy", "bergen", "bodø", "drammen", "egersund",
            "fredrikstad", "gjøvik", "halden", "hamar", "harstad", "haugesund",
            "horten", "hønefoss", "kongsberg", "kongsvinger", "kristiansand",
            "kristiansund", "larvik", "leirvik", "lillehammer", "lillestrøm",
            "mandal", "mo i rana", "molde", "namsos", "narvik", "norway",
            "norwegian", "oslo", "porsgrunn", "raufoss", "rjukan",
            "sandefjord", "sandnes", "sarpsborg", "skien", "stavanger",
            "steinkjer", "tromsø", "trondheim", "tønsberg", "ytre enebakk",
            "ålesund",
        ],
    },
    "philippine": {
        "enabled": True,
        "terms": [
            "antipolo", "bacolod", "baguio", "baliuag", "batangas city",
            "binan", "butuan", "cabanatuan", "cagayan de oro", "caloocan",
            "cebu city", "cotabato city", "dagupan", "dasmariñas",
            "davao city", "filipino", "general santos", "iligan",
            "iloilo city", "lapu-lapu", "las piñas", "lucena", "mabalacat",
            "makati", "malabon", "malolos", "manila", "muntinlupa", "navotas",
            "olongapo", "ormoc", "parañaque", "pasig", "philippines",
            "puerto princesa", "quezon city", "san fernando", "san juan",
            "santa rosa", "tacloban", "tagalog", "taguig", "tagum",
            "tarlac city", "toledo", "tuguegarao", "valenzuela",
            "zamboanga city",
        ],
    },
    "polish": {
        "enabled": True,
        "terms": [
            "białystok", "bielsko-biała", "bydgoszcz", "bytom", "chorzów",
            "częstochowa", "dąbrowa", "elbląg", "gdańsk", "gdynia", "gliwice",
            "gorzów", "górnictwo", "inowrocław", "jastrzębie", "jaworzno",
            "katowice", "kielce", "kraków", "legnica", "lubin", "lublin",
            "mysłowice", "olsztyn", "opole", "ostrołęka", "piotrków", "poland",
            "poznań", "płock", "radom", "rybnik", "rzeszów", "siedlce",
            "sosnowiec", "szczecin", "tarnów", "toruń", "trybunalski", "tychy",
            "warsaw", "wałbrzych", "wrocław", "zabrze", "zdrój",
            "zielona góra", "łódź",
        ],
    },
    "portuguese": {
        "enabled": True,
        "terms": [
            "agualva-cacém", "almada", "amadora", "amora", "aveiro",
            "barcelos", "beja", "braga", "caldas da rainha", "castelo branco",
            "coimbra", "covilhã", "elvas", "fafe", "faro", "funchal",
            "gondomar", "guimarães", "lagos", "leiria", "lisbon", "loulé",
            "loures", "maia", "matosinhos", "odivelas", "ovar", "paredes",
            "penafiel", "ponte de lima", "portalegre", "porto", "portugal",
            "portuguese", "póvoa de varzim", "queluz", "rio tinto", "santarém",
            "setúbal", "sever do vouga", "torres vedras", "vila do conde",
            "vila franca", "vila nova", "viseu", "águeda", "évora",
        ],
    },
    "religion": {
        "enabled": True,
        "terms": [
            "almsgiving", "baptism", "bar mitzvah", "bat mitzvah", "bible",
            "blessing", "ceremony", "choir", "church", "communion",
            "confession", "confirmation", "congregation", "creed", "deacon",
            "devotion", "devout", "evangelism", "faith", "fellowship", "holy",
            "hymn", "minister", "mosque", "parish", "pastor", "prayer",
            "preacher", "priest", "quran", "religious", "religious education",
            "repentance", "revival", "ritual", "sacrament", "sacred",
            "salvation", "scripture", "sermon", "spirituality",
            "sunday school", "synagogue", "temple", "torah", "worship",
            "youth group",
        ],
    },
    "reproductive_health": {
        "enabled": True,
        "terms": [
            "abortion", "adoption", "assisted reproduction", "birth control",
            "birth spacing", "cervical cap", "condom", "contraception",
            "diaphragm", "egg donation", "emergency contraception",
            "family planning", "family planning clinic", "fertility treatment",
            "implant", "in vitro fertilization", "iud", "ivf",
            "maternity leave", "menses", "menstrual health", "menstruation",
            "miscarriage", "morning-after pill", "ovarian", "ovulation",
            "parental leave", "paternity leave", "planned parenthood",
            "pregnancy", "pro-choice", "pro-life", "reproductive autonomy",
            "reproductive freedom", "reproductive health",
            "reproductive justice", "reproductive rights", "reproductivity",
            "ru-486", "sexual education", "sexual health", "sperm donation",
            "sterilization", "stillbirth", "surrogacy", "tubal ligation",
            "uterus", "vasectomy", "womb",
        ],
    },
    "scottish": {
        "enabled": True,
        "terms": [
            "aberdeen", "airdrie", "alloa", "ayr", "barrhead", "bathgate",
            "bellshill", "blantyre", "buckie", "cambuslang", "coatbridge",
            "cumbernauld", "dingwall", "dumfries", "dundee", "dunfermline",
            "east kilbride", "edinburgh", "elgin", "falkirk", "fort william",
            "giffnock", "glasgow", "glenrothes", "greenock", "hawick",
            "inverness", "inverurie", "irvine", "jedburgh", "kilmarnock",
            "kirkcaldy", "kirkintilloch", "livingston", "motherwell", "nairn",
            "newton mearns", "perth", "portree", "scotland", "scottish",
            "stirling", "stranraer", "wishaw",
        ],
    },
    "south asian": {
        "enabled": True,
        "terms": [
            "agra", "ahmedabad", "allahabad", "amritsar", "aurangabad",
            "bangalore", "bhopal", "chandigarh", "chennai", "dhanbad",
            "faridabad", "firozabad", "guwahati", "gwalior", "hindi", "Hindoo",
            "Hindustanee", "howrah", "hyderabad", "indore", "jabalpur",
            "jaipur", "jodhpur", "kanpur", "kolkata", "kota", "lucknow",
            "ludhiana", "meerut", "mumbai", "nagpur", "nashik", "navi mumbai",
            "new delhi", "patna", "pune", "raipur", "rajkot", "ranchi",
            "srinagar", "surat", "thane", "vadodara", "varanasi", "vijayawada",
            "visakhapatnam",
        ],
    },
    "spanish": {
        "enabled": True,
        "terms": [
            "a coruña", "albacete", "alcalá", "alicante", "almería", "badajoz",
            "badalona", "barcelona", "bilbao", "burgos", "cartagena",
            "castellón", "córdoba", "elche", "fuenlabrada", "getafe", "gijón",
            "granada", "huelva", "jerez", "l'hospitalet", "las palmas",
            "leganés", "león", "logroño", "lérida", "madrid", "murcia",
            "málaga", "móstoles", "oviedo", "palma", "sabadell", "salamanca",
            "san sebastián", "santa cruz", "santander", "seville", "spain",
            "tarragona", "terrassa", "valencia", "valladolid", "vigo",
            "vitoria", "zaragoza",
        ],
    },
    "swedish": {
        "enabled": False,
        "terms": [
            "alingsås", "borlänge", "borås", "eskilstuna", "falun",
            "gothenburg", "gävle", "halmstad", "helsingborg", "hässleholm",
            "jönköping", "kalmar", "karlskrona", "karlstad", "kristianstad",
            "lidingö", "linköping", "luleå", "lund", "malmö", "märsta",
            "norrköping", "nyköping", "piteå", "scandinavian", "skövde",
            "stockholm", "sundsvall", "swede", "sweden", "swedes", "swedish",
            "södertälje", "trelleborg", "trollhättan", "täby", "umeå",
            "uppsala", "visby", "vänersborg", "västerås", "växjö", "örebro",
            "örnsköldsvik", "östersund",
        ],
    },
    "technology": {
        "enabled": True,
        "terms": [
            "air conditioner", "alarm clock", "answering machine", "antenna",
            "atari", "blender", "boombox", "box fan", "browser", "cable",
            "calculator", "camera", "cassette", "cassette player", "cd player",
            "ceiling fan", "celluloid", "compact disc", "computer", "data",
            "database", "dataset", "desk fan", "dishwasher", "dryer",
            "electric fan", "fax machine", "flashlight", "hardware", "heater",
            "internet", "microwave", "modem", "network", "nintendo",
            "operating system", "oscillating fan", "pager", "playstation",
            "polaroid", "portable fan", "radio", "record player",
            "refrigerator", "remote control", "satellite", "scanner", "sega",
            "software", "spreadsheet", "tape recorder", "telephone",
            "television", "thermostat", "timepiece", "toaster", "turntable",
            "typewriter", "vacuum cleaner", "vcr", "ventilator", "vhs",
            "video cassette", "video game", "vinyl record", "walkie-talkie",
            "walkman", "washing machine", "website", "word processor",
            "wristwatch", "xbox",
        ],
    },
    "timber": {
        "enabled": False,
        "terms": [
            "air drying", "beam", "board foot", "chainsaw", "chipboard",
            "clear cutting", "crosscut", "debarking", "deforestation",
            "felling", "forest conservation", "forestry", "hardwood",
            "hectare yield", "kiln drying", "lath", "log scaler", "log yard",
            "logging", "logging permit", "lumber", "lumber grading",
            "milling process", "plank", "plywood", "pulpwood", "reforestation",
            "rip cut", "sawing", "sawmill", "selective cutting",
            "silviculture", "skidder", "softwood", "stumpage",
            "sustainable forestry", "timber", "timber frame", "timber stand",
            "timberland", "tree farm", "tree felling", "veneer", "wood grain",
            "wood preservation", "wood processing", "wood treatment",
            "woodlot", "woodworker",
        ],
    },
    "transportation": {
        "enabled": True,
        "terms": [
            "automobile", "ballast bed", "barge", "bicycle", "boxcar",
            "brakeman", "branch line", "buggy", "cable ferry", "caboose",
            "carriage", "cowcatcher", "depot", "dock", "electric train",
            "Ellis Island", "engineer", "ferry", "ferry landing", "ferryman",
            "flatcar", "freight manifest", "freight train", "gangplank",
            "grade crossing", "handcar", "horseless carriage",
            "immigrant ship", "locomotive", "main line", "Model T", "motorcar",
            "motorcycle", "narrow gauge", "ocean liner", "paddle wheel",
            "passenger manifest", "passenger train", "pier", "platform edge",
            "Pullman car", "rail bridge", "rail tunnel", "rail yard",
            "railcar", "railroad", "railroad tie", "railway", "right of way",
            "riverboat", "rolling stock", "section gang", "signal system",
            "spur line", "stagecoach", "steam locomotive", "steamer",
            "steamship", "steerage", "sternwheeler", "streetcar",
            "switch track", "tender", "timetable", "touring car",
            "track gauge", "track maintenance", "train conductor",
            "train dispatch", "train schedule", "train station", "tramway",
            "trolley", "tugboat", "water tower", "waybill", "wharf",
            "whistle stop", "trailer"
        ],
    },
    # "your_next_tag": {"enabled": True, "terms": ["term1", "term2", ...]},
}

def preprocess_text(text):
    if isinstance(text, str):
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = text.lower()
    else:
        text = ''
    return text

all_a_files = sorted(f for f in os.listdir(A_DIR) if f.lower().endswith('.csv'))
already_tagged = set(os.listdir(B_DIR))

file_names = [f for f in all_a_files if f not in already_tagged]
skipped = [f for f in all_a_files if f in already_tagged]

if skipped:
    print(f"Skipping {len(skipped)} file(s) already tagged in B/: {', '.join(skipped)}")
if not file_names:
    print("No new files to process in A/.")

file_paths = [os.path.join(A_DIR, f) for f in file_names]

# --- Load new transcripts ------------------------------------------------
dfs = {}  # file_name -> DataFrame
for file_name, file_path in zip(file_names, file_paths):
    try:
        print(f"Processing: {file_path}")
        df = pd.read_csv(file_path, encoding='utf-8', quotechar='"', escapechar='\\')
        if TEXT_COLUMN not in df.columns:
            print(f"  Skipping {file_name}: no '{TEXT_COLUMN}' column found.")
            continue
        dfs[file_name] = df
    except Exception as e:
        print(f"Error with file {file_name}: {e}")

corpus = ''
for df in dfs.values():
    words_series = df[TEXT_COLUMN].fillna('').astype(str).str.lower().str.strip()
    corpus += ' '.join(words_series) + ' '

cleaned_corpus = preprocess_text(corpus)
filtered_words = [w for w in cleaned_corpus.split() if w not in stop_words and len(w) >= MIN_WORD_LENGTH]
word_freq = Counter(filtered_words)
top_distinctive_words = word_freq.most_common(100)

def get_tags_column_index(df):
    last_populated_idx = -1
    for idx, col in enumerate(df.columns):
        has_data = df[col].notna().any() and (df[col].astype(str).str.strip() != '').any()
        if has_data:
            last_populated_idx = idx
    return last_populated_idx + 1


def insert_tags_and_terms_columns(df, tags_series, terms_series):
    """
    Insert 'tags' then 'terms' immediately after the last populated
    column in *df* (as located by get_tags_column_index). If df already
    has two columns sitting in that slot (e.g. this file is being
    re-tagged after already having tags/terms written once), they are
    replaced rather than duplicated -- the generalized version of the
    single-column function's target_idx + 1 skip, now skipping the two
    columns we're inserting.
    """
    target_idx = get_tags_column_index(df)

    tags_col = pd.Series(tags_series.values, index=df.index, name='tags')
    terms_col = pd.Series(terms_series.values, index=df.index, name='terms')
    left = df.iloc[:, :target_idx]
    right = df.iloc[:, target_idx + 2:]
    return pd.concat([left, tags_col, terms_col, right], axis=1)

# ============================================================
# ROW-LEVEL TAGGING (write B/)
# ============================================================

def tag_and_terms_for_row(text):
    """
    Scan a single row's text once for both the parent tags it matches
    and the specific child terms responsible for each match.

    Returns a (tags_str, terms_str) pair, each ';'-joined:
      tags_str  -- matched tag names, in TAGS iteration order.
      terms_str -- matched terms, in the order first encountered, using
                   each term's original casing as written in TAGS. A
                   term is listed once even if it occurs multiple times
                   in the row's text, or matches under more than one tag
                   (e.g. "spalding" is a term shared by both the
                   "geographic" and "LCOH Places" tags).
    """
    if not isinstance(text, str) or not text:
        return '', ''
    lowered = text.lower()
    matched_tags = []
    matched_terms = []
    seen_terms = set()
    for tag_name, tag_data in TAGS.items():
        if not tag_data.get("enabled", True):
            continue
        tag_hit = False
        for term in tag_data["terms"]:
            term_l = term.lower()
            if ' ' in term_l:
                found = term_l in lowered
            else:
                found = re.search(r'\b' + re.escape(term_l) + r'\b', lowered) is not None
            if found:
                tag_hit = True
                if term_l not in seen_terms:
                    seen_terms.add(term_l)
                    matched_terms.append(term)
        if tag_hit:
            matched_tags.append(tag_name)
    return ';'.join(matched_tags), ';'.join(matched_terms)


for file_name, df in dfs.items():
    row_results = df[TEXT_COLUMN].fillna('').astype(str).apply(tag_and_terms_for_row)
    tags_series = row_results.apply(lambda pair: pair[0])
    terms_series = row_results.apply(lambda pair: pair[1])
    tagged_df = insert_tags_and_terms_columns(df, tags_series, terms_series)
    output_path = os.path.join(B_DIR, file_name)
    tagged_df.to_csv(output_path, index=False)
    print(f"Wrote tagged file: {output_path}")

# ============================================================
# TAG TALLY (write C/)
# ============================================================

def find_tag_terms(text_corpus, terms):
    term_freq = Counter()
    lowered = text_corpus.lower()
    for term in terms:
        term_l = term.lower()
        if ' ' in term_l:
            count = len(re.findall(re.escape(term_l), lowered))
        else:
            count = len(re.findall(r'\b' + re.escape(term_l) + r'\b', lowered))
        if count:
            term_freq[term] = count
    return term_freq


all_b_files = sorted(f for f in os.listdir(B_DIR) if f.lower().endswith('.csv'))
tally_corpus = ''
for file_name in all_b_files:
    try:
        b_df = pd.read_csv(os.path.join(B_DIR, file_name), encoding='utf-8', quotechar='"', escapechar='\\')
        if TEXT_COLUMN in b_df.columns:
            words_series = b_df[TEXT_COLUMN].fillna('').astype(str).str.lower().str.strip()
            tally_corpus += ' '.join(words_series) + ' '
    except Exception as e:
        print(f"Error reading {file_name} from B/ for tally: {e}")

tally_rows = []
for tag_name, tag_data in TAGS.items():
    if not tag_data.get("enabled", True):
        continue
    term_counts = find_tag_terms(tally_corpus, tag_data["terms"])
    for term, count in term_counts.items():
        tally_rows.append({'tag': tag_name, 'term': term, 'count': count})

tally_rows.sort(key=lambda r: (r['tag'].lower(), -r['count']))

tally_df = pd.DataFrame(tally_rows, columns=['tag', 'term', 'count'])
tally_output_path = os.path.join(C_DIR, 'tag_tally.csv')
tally_df.to_csv(tally_output_path, index=False)
print(f"\nWrote combined tag tally: {tally_output_path}")

current_tag = None
for row in tally_rows:
    if row['tag'] != current_tag:
        current_tag = row['tag']
        print(f"\n## {current_tag}")
    print(f"{row['term']}: {row['count']}")

# ============================================================
# PER-FILE TAG + TERM TALLY (write C/)
# ============================================================

file_tally_lines = []
for file_name in all_b_files:
    file_stem = os.path.splitext(file_name)[0]

    file_tag_rows = []
    try:
        b_df = pd.read_csv(os.path.join(B_DIR, file_name), encoding='utf-8', quotechar='"', escapechar='\\')
        if TEXT_COLUMN in b_df.columns:
            file_words_series = b_df[TEXT_COLUMN].fillna('').astype(str).str.lower().str.strip()
            file_corpus = ' '.join(file_words_series) + ' '
            for tag_name, tag_data in TAGS.items():
                if not tag_data.get("enabled", True):
                    continue
                term_counts = find_tag_terms(file_corpus, tag_data["terms"])
                if term_counts:
                    file_tag_rows.append((tag_name, sum(term_counts.values()), term_counts))
    except Exception as e:
        print(f"Error reading {file_name} from B/ for per-file tally: {e}")

    file_tag_rows.sort(key=lambda r: r[0].lower())

    file_tally_lines.append(file_stem)
    file_tally_lines.append('')
    for tag_name, tag_total, term_counts in file_tag_rows:
        file_tally_lines.append(f"{tag_name}: {tag_total}")
        for term, count in sorted(term_counts.items(), key=lambda kv: -kv[1]):
            file_tally_lines.append(f"{term}: {count}")
    file_tally_lines.append('')

file_tally_output_path = os.path.join(C_DIR, 'tag_tally_by_file.csv')
with open(file_tally_output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(file_tally_lines).rstrip('\n') + '\n')

print(f"\nWrote per-file tag/term tally: {file_tally_output_path}")