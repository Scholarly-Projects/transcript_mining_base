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
            "harvest", "tractor", "acreage", "crop", "livestock",
            "farm field", "barn building", "ranch", "garden", "orchard",
            "dairy", "cattle", "poultry", "farming equipment", "fertilizer",
            "seed", "irrigation", "plow", "farmhand", "hoe", "shovel",
            "milking", "hay", "silage", "compost", "weeding", "crop rotation",
            "organic", "gmo", "sustainable", "farming", "rural", "homestead",
            "grain crop", "wheat", "corn maize", "soybean", "potato",
            "apple fruit", "berry", "honey", "apiary", "pasture",
            "combine harvester", "trailer", "baler", "thresher",
        ],
    },
    "animal": {
        "enabled": False,
        "terms": [
            "moose", "ewe", "horse", "salmon hatchery", "goat", "pig",
            "chicken", "turkey", "duck", "quail", "rabbit", "squirrel",
            "herd", "stag", "buck", "doe", "paw", "bear den", "cougars",
            "coyote", "wolves", "fox", "mountain lions", "raccoon", "skunk",
            "badger", "possum", "weasel", "ferret", "mink", "otter", "beaver",
            "muskrat", "marmot", "gopher", "prairie dog", "chipmunk", "bison",
            "buffalo", "lizard", "snake bite", "frog", "toad", "newt",
            "salamander", "owl", "hawk", "eagle", "raven", "crow", "sparrow",
            "finch", "bluebird", "lamb", "wolf pack", "whale pod", "gaggle",
            "hawks", "steelhead",
        ],
    },
    "clothing": {
        "enabled": True,
        "terms": [
            "clothing", "fashion", "apparel", "outfit", "wardrobe", "jeans",
            "t-shirt", "sweater", "jacket", "skirt", "pants", "shoes",
            "boots", "sneakers", "hat", "cap", "scarf", "gloves", "socks",
            "underwear", "outerwear", "workwear", "uniform", "overalls",
            "apron", "denim", "flannel", "plaid", "cotton", "polyester",
            "fabric", "stitching", "seamstress", "tailor", "alterations",
            "thrift", "secondhand", "shopping", "retail", "department store",
        ],
    },
    "crime": {
        "enabled": True,
        "terms": [
            "crime", "violence", "theft", "robbery", "burglary", "assault",
            "homicide", "murder", "rape", "domestic violence", "gangs",
            "drugs", "trafficking", "possession", "distribution", "addiction",
            "prostitution", "gambling", "corruption", "bribery", "fraud",
            "embezzlement", "extortion", "racketeering", "money laundering",
            "forgery", "identity theft", "vandalism", "arson",
            "illegal immigration", "detention", "arrest", "interrogation",
            "trial", "plea bargain", "conviction", "sentencing",
            "imprisonment", "probation", "parole", "rehabilitation",
            "recidivism", "police", "detective", "officer", "investigation",
            "forensics",
        ],
    },
    "culture": {
        "enabled": True,
        "terms": [
            "tradition", "folklore", "customs", "rituals", "celebration",
            "cuisine", "festivals", "dialect", "belonging", "neighborhood",
            "gathering", "gatherings", "socializing", "folktales", "legends",
            "crafts", "craftsmanship", "oral tradition", "ethnicity",
            "diversity", "inclusion", "community centers", "street fairs",
            "parades", "local traditions",
            "folk dance", "folk art", "cultural exchange",
            "cultural identity", "cultural pride", "multiculturalism",
            "ethnic neighborhoods",
        ],
    },
    "economic": {
        "enabled": True,
        "terms": [
            "great depression", "employment", "wage", "salary", "income",
            "paycheck", "earnings", "livelihood", "vocation", "profession",
            "skilled trade", "skill", "craftsman", "manual labor",
            "blue-collar", "white-collar", "layoff", "dismissal",
            "termination", "retrenchment", "redundancy", "job search",
            "job interview", "resume document", "cover letter", "application",
            "hiring", "apprenticeship", "promotion", "advancement",
            "salary increase", "employee benefits", "pension", "retirement",
            "savings", "investment", "budgeting", "financial planning",
            "debt", "credit loan", "loan", "mortgage",
        ],
    },
    "education": {
        "enabled": True,
        "terms": [
            "school", "classroom", "teacher", "student", "learning",
            "literacy", "numeracy", "curriculum", "assignment", "homework",
            "exam", "test", "grade", "report card", "diploma", "degree",
            "certificate", "academia", "scholarship", "transcript",
            "textbook", "library", "study", "research", "group work",
            "peer review", "tutoring", "principal", "administrator",
            "counselor", "resource center", "special education",
            "individualized education plan (iep)", "field trip",
            "extracurricular", "athletics", "club",
            "parent-teacher conference", "back-to-school night", "open house",
            "graduation", "prom", "financial aid", "grant", "loan",
            "work-study program",
        ],
    },
    "environment": {
        "enabled": True,
        "terms": [
            "nature", "ecology", "ecosystem", "biodiversity",
            "conservation", "sustainability", "climate", "climate change",
            "global warming", "pollution", "air pollution", "water pollution",
            "soil pollution", "deforestation", "habitat destruction",
            "waste management", "recycling", "renewable energy",
            "solar energy", "wind energy", "hydropower", "geothermal energy",
            "carbon footprint", "greenhouse gases", "ozone depletion",
            "wildlife", "endangered species", "natural resources",
            "land conservation", "water conservation", "energy efficiency",
            "environmental impact", "environmental policy",
            "environmental regulation", "environmental awareness",
            "environmental education", "environmental activism",
            "sustainable development", "urbanization", "rural development",
            "land use", "land degradation", "desertification",
            "ocean conservation", "marine life", "coral reefs",
            "sea level rise", "water scarcity", "drought", "flood",
            "natural disaster", "ecotourism", "green spaces", "parks",
            "forests", "wetlands", "mountains", "rivers", "lakes", "oceans",
            "beaches", "glaciers", "tundra", "grasslands",
        ],
    },
    "family": {
        "enabled": True,
        "terms": [
            "parent", "mother", "father", "child", "sibling", "brother",
            "sister", "grandparent", "grandfather", "grandmother",
            "grandchild", "cousin", "aunt", "uncle", "nephew", "niece",
            "step-parent", "step-sibling", "step-brother", "step-sister",
            "stepchild", "spouse", "husband", "wife", "partner", "boyfriend",
            "girlfriend", "fiance", "fiancee", "domestic partner", "marriage",
            "wedding", "divorce", "single parent", "orphan",
            "adoptive parent", "adopted child", "foster parent",
            "foster child", "guardian", "legal guardian", "custody",
            "child support", "family gathering", "family dinner",
            "family tradition",
        ],
    },
    "food_and_drink": {
            "enabled": True,
            "terms": [
                "beef", "pork", "chicken", "milk", "bread", "butter", "eggs",
                "cheese", "pie", "biscuit", "coffee", "tea", "beer", "whiskey",
                "soda", "soup", "stew", "salad", "salt", "pepper", "lard",
                "marmalade", "cider", "vinegar", "bacon", "sausage", "jerky",
                "pickles", "fruit spread", "cake", "cookies", "doughnuts",
                "ice cream", "candy", "chocolate", "raisins", "ham", "mutton",
                "venison", "elk", "salmon", "trout", "rabbit", "salt pork",
                "sourdough", "cornbread", "flapjacks", "hardtack", "mush",
                "molasses", "sorghum", "jam", "jelly", "applesauce", "baked beans",
                "buttermilk", "sarsaparilla", "root beer", "moonshine",
                "huckleberries",
            ],
        },
    "health": {
        "enabled": True,
        "terms": [
            "doctor", "nurse", "hospital", "clinic", "medicine",
            "prescription", "insurance", "appointment", "check up",
            "emergency", "pharmacy", "surgery", "ambulance", "patient",
            "care", "treatment", "therapy", "recovery", "vaccine",
            "vaccination", "flu", "cold", "fever", "cough", "sore throat",
            "headache", "pain", "injury", "wound", "bandage", "cast",
            "physical therapy", "mental health", "diet plan", "workout",
            "body weight", "blood pressure", "cholesterol", "diabetes",
            "asthma", "allergy", "immunity", "virus", "bacteria",
            "healthcare",
        ],
    },
    "history": {
        "enabled": True,
        "terms": [
            "ancestors", "traditions", "lineage", "legacy", "ancestral",
            "heritage", "oral history", "ancestral home", "ancestral land",
            "pioneers", "settlers", "frontiersmen", "colonial",
            "revolutionary", "founding fathers", "historic sites",
            "historical landmarks", "ancestral knowledge",
            "historic preservation", "historical records", "local history",
            "family history", "explorers", "trailblazers",
            "historical events", "heritage sites", "cultural heritage",
            "community history", "historical artifacts", "historical society",
            "genealogy", "civil rights", "labor history",
            "historical documents", "archaeology", "historic buildings",
            "traditional crafts", "ancestral language",
        ],
    },
    "cinema": {
        "enabled": True,
        "terms": [
            "cinema", "film", "movie", "screenplay", "script", "producer",
            "cinematography", "editing", "soundtrack", "score", "dialogue",
            "actor", "actress", "cast", "crew", "scene", "shot", "frame",
            "close-up", "long shot", "mid shot", "wide shot", "tracking shot",
            "montage", "climax", "plot", "storyline", "narrative",
            "character", "antagonist", "protagonist", "screenwriter",
            "camerawork", "film noir", "blockbuster", "independent film",
            "silent film", "documentary", "mockumentary", "animation",
            "feature film", "short film", "opening credits",
            "closing credits", "cameo", "stunt", "special effects",
            "visual effects", "voice-over",
        ],
    },
    "literature": {
        "enabled": True,
        "terms": [
            "literature", "novel", "poetry", "prose", "fiction", "nonfiction",
            "narrative", "plot", "theme", "character", "dialogue", "metaphor",
            "simile", "alliteration", "allegory", "symbolism", "irony",
            "foreshadowing", "flashback", "epilogue", "prologue",
            "manuscript", "draft", "editing", "publishing", "author",
            "writer", "playwright", "essayist", "verse", "sonnet", "haiku",
            "epic poem", "free verse", "short story", "novella", "fable",
            "mythology", "folktale", "biography", "autobiography", "memoir",
            "criticism", "literary theory", "genre fiction",
            "classic literature",
        ],
    },
    "theater": {
        "enabled": True,
        "terms": [
            "theater", "drama", "comedy", "melodrama", "monologue", "stage",
            "backstage", "front stage", "playwright", "script", "blocking",
            "dramaturgy", "actor", "actress", "cast", "ensemble",
            "understudy", "set design", "prop", "costume", "lighting design",
            "sound design", "curtain call", "matinee", "broadway",
            "off-broadway", "box office", "standing ovation", "fourth wall",
            "break character", "dress rehearsal", "cold reading", "soliloquy",
            "prologue", "epilogue", "improvisation", "method acting",
            "stage directions", "tech rehearsal", "house lights",
            "exit stage", "upstage",
        ],
    },
    "music": {
        "enabled": True,
        "terms": [
            "music", "melody", "harmony", "rhythm", "tempo", "dynamics",
            "notation", "composition", "improvisation", "orchestration",
            "counterpoint", "cadence", "crescendo", "decrescendo", "timbre",
            "chord", "key signature", "time signature", "interval",
            "arpeggio", "sight reading", "ear training", "music theory",
            "conducting", "score study", "vibrato", "resonance", "acoustics",
            "concert", "recital", "rehearsal", "ensemble", "soloist", "choir",
            "orchestra", "chamber music", "woodwind", "brass instrument",
            "string instrument", "percussion", "piano technique",
            "guitar technique", "vocal training", "breath control",
            "stage presence", "musical phrasing",
        ],
    },
    "indigenous": {
        "enabled": False,
        "terms": [
            "shoshone", "tribe", "reservation", "native american",
            "indigenous", "bannock", "nez perce", "coeur d'alene indian",
            "kootenai", "salish", "spokane indian", "shoshone-bannock",
            "fort hall indian", "lemhi", "shoshone-paiute", "shoshoni",
            "tukudeka", "sheepeater", "camas prairie", "nimíipuu", "sahaptin",
            "atsina", "kalispel indian", "pend d'oreille", "yakama indian",
            "flathead", "wenatchi", "methow", "entiat indian",
            "chelan indian", "sinkiuse-columbia", "wenatchee indian", "palus",
            "cayuse indian", "umatilla indian", "tenino indian",
            "walla walla indian", "nez percé", "colville indian",
            "columbia indian", "willamette valley indian",
            "clearwater indian", "salmon river indian", "payette indian",
            "bruneau indian", "owyhee", "snake river indian",
            "lemhi river indian",
        ],
    },
    "mining": {
        "enabled": False,
        "terms": [
            "mining", "ore", "extraction", "prospecting", "drilling",
            "blasting", "excavation", "fracking", "hydraulic fracturing",
            "tunneling", "shaft sinking", "open pit", "underground mining",
            "strip mining", "quarrying", "mineral deposit", "ore body",
            "tailings", "mine reclamation", "smelting", "refining",
            "flotation process", "heap leaching", "hydrometallurgy",
            "pyrometallurgy", "drift mining", "slope mining",
            "room and pillar", "longwall mining", "hard rock mining",
            "placer mining", "dredging", "coal seam", "geological survey",
            "assay", "mine ventilation", "mine safety", "explosive charge",
            "miner's lamp", "haul truck", "conveyor belt", "ore grade",
            "rock fragmentation", "mining permit", "extraction rate",
            "strip ratio", "reclamation bond", "processing plant", "slurry",
            "geotechnical analysis", "mine closure", "environmental impact",
            "mine drainage",
        ],
    },
    "timber": {
        "enabled": False,
        "terms": [
            "timber", "lumber", "logging", "forestry", "sawing", "felling",
            "deforestation", "reforestation", "sawmill", "plywood",
            "hardwood", "softwood", "board foot", "timberland", "woodlot",
            "log yard", "milling process", "kiln drying", "air drying",
            "wood grain", "lumber grading", "plank", "beam", "log scaler",
            "chainsaw", "skidder", "debarking", "pulpwood", "chipboard",
            "veneer", "crosscut", "rip cut", "lath", "timber frame",
            "wood treatment", "sustainable forestry", "clear cutting",
            "selective cutting", "silviculture", "tree farm", "stumpage",
            "hectare yield", "logging permit", "timber stand", "tree felling",
            "woodworker", "wood processing", "forest conservation",
            "wood preservation",
        ],
    },
    "manufacturing": {
        "enabled": True,
        "terms": [
            "manufacturing", "fabrication", "assembly line", "machining",
            "casting", "forging", "molding", "cnc machining",
            "lean manufacturing", "quality control", "process optimization",
            "supply chain", "raw materials", "industrial robotics",
            "prototyping", "batch production", "mass production",
            "just-in-time", "six sigma", "kaizen", "additive manufacturing",
            "3d printing", "tooling", "precision engineering",
            "injection molding", "extrusion", "welding", "sheet metal",
            "die casting", "material handling", "assembly process",
            "industrial safety", "factory layout", "workstation",
            "operational efficiency", "machine calibration",
            "inventory management", "continuous improvement",
            "computer-aided design", "computer-aided manufacturing",
            "automation process", "labor productivity", "quality assurance",
            "standardization", "lean process", "production planning",
            "equipment maintenance", "industrial engineering",
            "production workflow",
        ],
    },
    "transportation": {
        "enabled": True,
        "terms": [
            "railroad", "railway", "locomotive", "freight train",
            "passenger train", "high-speed rail", "commuter rail",
            "light rail", "subway system", "monorail", "streetcar", "tramway",
            "track gauge", "railcar", "diesel engine", "electric train",
            "steam locomotive", "bullet train", "rail yard", "train station",
            "rail bridge", "grade crossing", "switch track", "rolling stock",
            "signal system", "train dispatch", "rail tunnel",
            "track maintenance", "level crossing", "railroad tie",
            "ballast bed", "freight corridor", "passenger corridor",
            "intermodal terminal", "container transport", "right of way",
            "rail infrastructure", "train conductor", "brakeman", "engineer",
            "freight manifest", "waybill", "cargo handling", "rail logistics",
            "timetable", "train schedule", "platform edge", "railway safety",
            "commuter pass", "transit hub",
        ],
    },
    "manual_labor": {
        "enabled": True,
        "terms": [
            "factory", "labor union", "union", "worker", "laborer",
            "employee", "employer", "vocation", "wage", "salary", "paycheck",
            "hourly wage", "daily wage", "weekly wage", "overtime",
            "minimum wage", "living wage", "health insurance", "healthcare",
            "retirement", "pension", "sick leave", "vacation",
            "maternity leave", "paternity leave", "paid time off", "layoff",
            "dismissal", "termination", "hiring", "firing", "training",
            "manual labor", "blue-collar", "workplace", "factory floor",
            "assembly line", "warehouse", "construction", "maintenance",
            "janitorial", "service industry", "service worker",
        ],
    },
    "migration": {
        "enabled": True,
        "terms": [
            "immigration", "emigration", "refugee", "asylum",
            "naturalization", "resettlement", "integration", "exile",
            "citizenship", "border", "visa", "deportation", "fleeing",
            "repatriation", "exodus", "transplantation", "dispersion",
            "nomadism", "migrant", "transient", "displacement",
            "colonization", "settler", "journey", "voyage", "pilgrimage",
            "relocation", "repopulation", "expatriate", "sojourner",
            "transmigrating", "seeking refuge", "dislocation",
            "displaced person", "reintegration", "acculturation", "diaspora",
            "melting pot", "ethnic diversity", "immigrant community",
            "border crossing", "migration policy", "immigration reform",
        ],
    },
    "leisure": {
        "enabled": True,
        "terms": [
            "ski", "leisure", "recreation", "entertainment", "activity",
            "hobby", "pastime", "sports", "game", "fun", "relaxation",
            "adventure", "picnic", "barbecue", "camp", "hike",
            "trail", "fishing", "hunting", "camping", "bonfire", "campfire",
            "swimming", "pool", "beach", "lake", "boating", "canoeing",
            "kayaking", "biking", "cycling", "walking", "running", "hiking",
            "gardening", "photography", "board game", "card game", "dance",
        ],
    },
    "religion": {
        "enabled": True,
        "terms": [
            "religious", "church", "temple", "mosque", "synagogue", "prayer", "worship",
            "faith", "creed", "spirituality", "religious", "devotion",
            "ritual", "ceremony", "sacred", "holy", "blessing", "preacher",
            "minister", "priest", "pastor", "deacon", "congregation",
            "parish", "fellowship", "almsgiving", "devout", "evangelism",
            "revival", "sermon", "bible", "scripture", "quran", "torah",
            "hymn", "choir", "religious education", "sunday school",
            "youth group", "confirmation", "bar mitzvah", "bat mitzvah",
            "sacrament", "communion", "baptism", "confession", "repentance",
            "salvation",
        ],
    },
    "technology": {
        "enabled": True,
        "terms": [
            "electric fan", "oscillating fan", "desk fan", "box fan",
            "ceiling fan", "portable fan", "ventilator", "computer", "pc",
            "software", "hardware", "data", "database", "network", "internet",
            "website", "browser", "operating system", "dataset",
            "word processor", "spreadsheet", "modem", "printer", "scanner",
            "fax machine", "vhs", "cassette", "walkman", "tape recorder",
            "cd player", "compact disc", "video game", "atari", "nintendo",
            "sega", "playstation", "xbox", "calculator",
            "typewriter", "telephone", "answering machine", "pager",
            "television", "vcr", "remote control", "antenna", "cable",
            "satellite", "video cassette", "walkie-talkie", "radio",
            "cassette player", "boombox", "turntable", "vinyl record",
            "record player", "camera", "polaroid", "celluloid", "flashlight",
            "timepiece", "wristwatch", "microwave", "toaster", "blender",
            "vacuum cleaner", "dishwasher", "washing machine", "dryer",
            "refrigerator", "air conditioner", "heater", "thermostat",
            "alarm clock",
        ],
    },
    "basque": {
        "enabled": True,
        "terms": [
            "basque", "euskadi", "euskara", "donostia",
            "bilbao", "vitoria-gasteiz", "iruña", "hondarribia", "zarautz",
            "getaria", "biarritz", "bayonne", "saint-jean-de-luz", "guernica",
            "bermeo", "mutriku", "ondarroa", "mundaka", "lekeitio", "orio",
            "deba", "zumaia", "lazkao", "azpeitia", "zestoa", "hernani",
            "amezketa", "andoain", "astigarraga", "ataun", "beasain",
            "errenteria", "ibarra", "idiazabal", "leaburu", "legazpi",
            "leintz-gatzaga", "txakoli", "sagardo", "pintxo", "pintxos",
            "pilota", "basque pelota", "jai alai", "txapela", "txistorra",
            "idiazabal cheese",
        ],
    },
    "british": {
        "enabled": True,
        "terms": [
            "british", "britain", "london", "manchester", "birmingham",
            "liverpool", "leeds", "bristol", "sheffield", "newcastle",
            "cardiff", "nottingham", "southampton", "leicester", "brighton",
            "portsmouth", "plymouth", "derby", "hull", "middlesbrough",
            "northampton", "luton", "wolverhampton", "norwich", "swansea",
            "oxford", "cambridge", "exeter", "yorkshire", "cornwall", "essex",
            "surrey", "devon", "england",
        ],
    },
    "canadian": {
        "enabled": True,
        "terms": [
            "canada", "canadian", "toronto", "montreal", "vancouver",
            "calgary", "edmonton", "ottawa", "winnipeg", "quebec", "victoria",
            "halifax", "regina", "saskatoon", "st. john's", "kitchener",
            "burnaby", "windsor", "richmond", "burlington", "surrey",
            "mississauga", "markham", "brampton", "vaughan", "oakville",
            "niagara falls", "waterloo", "guelph", "cambridge", "kelowna",
            "fredericton", "charlottetown", "whitehorse", "yellowknife",
            "iqaluit", "ontario", "nova scotia", "new brunswick", "manitoba",
        ],
    },
    "chinese": {
        "enabled": False,
        "terms": [
            "chinese", "china", "beijing", "shanghai", "guangzhou",
            "shenzhen", "tianjin", "chongqing", "hangzhou", "nanjing",
            "chengdu", "wuhan", "xi'an", "suzhou", "dalian", "qingdao",
            "shenyang", "xiamen", "changsha", "zhengzhou", "dongguan", "wuxi",
            "changchun", "ningbo", "kunming", "nanchang", "hefei", "taiyuan",
            "jinan", "guiyang", "fuzhou", "harbin", "hohhot", "ürümqi",
            "lanzhou", "yinchuan", "lhasa", "nanning", "haikou", "macau",
            "hong kong", "taipei", "macao", "guilin", "kashgar",
            "shijiazhuang", "jining",
        ],
    },
    "finnish": {
        "enabled": True,
        "terms": [
            "finnish", "suomalainen", "finland", "suomi", "helsinki", "espoo",
            "tampere", "vantaa", "oulu", "turku", "jyväskylä", "kuopio",
            "lahti", "kouvola", "pori", "joensuu", "lappeenranta", "vaasa",
            "hämeenlinna", "seinäjoki", "rovaniemi", "mikkeli", "kotka",
            "salo", "porvoo", "lohja", "hyvinkää", "järvenpää", "rauma",
            "kokkola", "kerava", "kajaani", "tuusula", "kirkkonummi",
            "seutula", "sipoo", "siuntio", "karkkila", "vihti", "nurmijärvi",
            "riihimäki", "raseborg", "loviisa", "hanko", "nastola", "hollola",
            "asikkala",
        ],
    },
    "french": {
        "enabled": True,
        "terms": [
            "french", "france", "marseille", "lyon", "toulouse", "nantes",
            "strasbourg", "montpellier", "bordeaux", "lille", "rennes",
            "reims", "le havre", "cergy", "saint-étienne", "toulon", "angers",
            "grenoble", "dijon", "nîmes", "aix-en-provence",
            "saint-quentin-en-yvelines", "brest", "le mans", "amiens",
            "limoges", "clermont-ferrand", "villeurbanne", "besançon",
            "orléans", "metz", "rouen", "mulhouse", "perpignan", "caen",
            "argenteuil", "saint-denis", "roubaix", "tourcoing", "avignon",
            "poitiers", "créteil", "nanterre", "versailles",
        ],
    },
    "german": {
        "enabled": False,
        "terms": [
            "german", "germany", "berlin", "hamburg", "munich", "cologne",
            "frankfurt", "stuttgart", "düsseldorf", "dortmund", "essen",
            "leipzig", "bremen", "dresden", "hanover", "nuremberg",
            "duisburg", "bochum", "wuppertal", "bielefeld", "bonn", "münster",
            "karlsruhe", "mannheim", "augsburg", "wiesbaden", "gelsenkirchen",
            "mönchengladbach", "braunschweig", "chemnitz", "kiel", "aachen",
            "halle", "magdeburg", "freiburg", "krefeld", "lübeck",
            "oberhausen", "erfurt", "mainz", "rostock", "kassel", "hagen",
            "saarbrücken", "hamm", "potsdam", "leverkusen", "oldenburg",
        ],
    },
    "greek": {
        "enabled": True,
        "terms": [
            "greek", "greece", "athens", "thessaloniki", "patras",
            "heraklion", "larissa", "volos", "ioannina", "chania", "chalcis",
            "rethymno", "serres", "kavala", "komotini", "alexandroupoli",
            "katerini", "veria", "trikala", "lamia", "kozani", "polichni",
            "karditsa", "sykies", "nea ionia", "ioannis", "agia paraskevi",
            "palaio faliro", "tripoli", "galatsi", "agrinio", "chios",
            "mytilene", "kalamata", "chalkida", "thiva", "sparta", "corfu",
            "kastoria",
        ],
    },
    "geographic": {
        "enabled": False,
        "terms": [
            "caldwell", "idaho falls", "pocatello", "rupert", "boise",
            "nampa", "emmett", "twin falls", "burley", "moscow", "lewiston",
            "mountain home", "blackfoot", "post falls", "sandpoint",
            "jerome, idaho", "weiser", "eagle, idaho", "middleton",
            "rathdrum", "bonners ferry", "st. maries", "spirit lake",
            "glenns ferry", "parma", "kimberly", "st. anthony", "gooding",
            "mccall, idaho", "driggs", "american falls", "grangeville",
            "fountain, idaho", "acequia", "albion", "arco", "athol",
            "bellevue", "bloomington", "bruneau", "buhl", "challis",
            "clayton", "clifton", "cottonwood", "council, idaho", "crouch",
            "culdesac", "dayton, idaho", "dover", "downey", "drummond",
            "dubois", "elk city", "fairfield", "fenn", "fernwood",
            "fort hall", "fruitland", "garden city", "genesee", "greenleaf",
            "hagerman", "hansen, idaho", "hazelton", "heyburn", "holbrook",
            "homedale", "horseshoe bend", "huetter", "huston, idaho", "inkom",
            "iona", "julietta", "kamiah", "kendrick, idaho", "ketchum",
            "kooskia", "kootenai", "kuna", "lapwai", "lava hot springs",
            "leadore", "lemhi", "letha", "lost river", "mackay", "malad city",
            "malta", "marsing", "melba, idaho", "menan", "mink creek",
            "montpelier", "monteview", "montour", "moore, idaho",
            "mountain home afb", "mud lake", "mullan", "murtaugh", "newdale",
            "new meadows", "new plymouth", "nezperce, idaho", "notus",
            "oakley", "oldtown", "onaway", "orofino", "osburn, idaho",
            "parker", "parkline", "payette", "peck", "picabo", "pinehurst",
            "placerville", "plummer", "pollock", "potlatch", "preston",
            "priest lake", "priest river", "rexburg", "richfield", "rigby",
            "rimini", "riverside", "rockford", "rockland", "sagle",
            "shelley, idaho", "shoshone", "smelterville", "soda springs",
            "spalding", "spencer", "stanley, idaho", "sugar city",
            "sun valley", "swan valley", "terry, idaho", "teton", "tetonia",
            "troy, idaho", "uhland", "victor, idaho", "wallace, idaho",
            "wardner", "warm river", "weippe", "wendell", "weston",
            "white bird", "wilder", "winchester", "worley",
        ],
    },
    "south asian": {
        "enabled": True,
        "terms": [
            "indian", "india", "hindi", "Hindustanee", "Hindoo", "new delhi", "mumbai", "bangalore",
            "chennai", "kolkata", "hyderabad", "pune", "ahmedabad", "surat",
            "jaipur", "kanpur", "lucknow", "nagpur", "patna", "indore",
            "thane", "bhopal", "visakhapatnam", "vadodara", "firozabad",
            "ludhiana", "agra", "nashik", "faridabad", "meerut", "rajkot",
            "varanasi", "srinagar", "aurangabad", "dhanbad", "amritsar",
            "navi mumbai", "allahabad", "ranchi", "howrah", "jabalpur",
            "gwalior", "vijayawada", "jodhpur", "raipur", "kota", "guwahati",
            "chandigarh",
        ],
    },
    "irish": {
        "enabled": True,
        "terms": [
            "irish", "ireland", "dublin", "galway", "limerick", "waterford",
            "drogheda", "dundalk", "bray", "navan", "kilkenny", "ennis",
            "carlow", "tralee", "newbridge", "portlaoise", "balbriggan",
            "naas", "athlone", "mullingar", "celbridge", "wexford",
            "letterkenny", "sligo", "clonmel", "greystones", "malahide",
            "carrigaline", "leixlip", "lucan", "skerries", "tramore",
            "killarney", "arklow", "kilcock", "ballina", "castlebar",
            "maynooth", "thurles", "monaghan", "mallow", "portarlington",
            "buncrana", "gorey", "tuam", "cobh", "potato famine",
        ],
    },
    "italian": {
        "enabled": True,
        "terms": [
            "italian", "italy", "rome", "milan", "naples", "turin", "palermo",
            "genoa", "bologna", "florence", "bari", "catania", "venice",
            "verona", "messina", "padua", "trieste", "taranto", "brescia",
            "prato", "reggio", "modena", "emilia", "perugia", "livorno",
            "ravenna", "cagliari", "foggia", "rimini", "salerno", "ferrara",
            "sassari", "latina", "giugliano", "monza", "syracuse", "bergamo",
            "pescara", "trento", "forlì", "vicenza", "terni", "bolzano",
            "novara", "piacenza", "ancona", "andria", "udine",
        ],
    },
    "japanese": {
        "enabled": True,
        "terms": [
            "japanese", "japan", "tokyo", "yokohama", "osaka", "nagoya",
            "sapporo", "fukuoka", "kobe", "kyoto", "kawasaki", "saitama",
            "hiroshima", "sendai", "kitakyushu", "chiba", "sakai", "niigata",
            "hamamatsu", "okayama", "kumamoto", "sagamihara", "kagoshima",
            "matsumoto", "kanazawa", "naha", "matsuyama", "kōchi", "nagasaki",
            "toyama", "otsu", "wakayama", "akita", "aomori", "asahikawa",
            "fukushima", "fukui", "gifu", "hachinohe", "hakodate",
            "higashiosaka", "himeji", "iwaki", "iwakuni", "kōfu", "kure",
        ],
    },
    "mexican": {
        "enabled": True,
        "terms": [
            "mexico", "mexican", "mexico city", "guadalajara", "monterrey",
            "puebla", "tijuana", "león", "ciudad juárez", "chihuahua",
            "cancún", "mérida", "aguascalientes", "querétaro", "toluca",
            "hermosillo", "san luis potosí", "culiacán", "acapulco",
            "morelia", "saltillo", "veracruz", "villahermosa",
            "tuxtla gutiérrez", "durango", "tepic", "colima", "campeche",
            "la paz", "torreón", "mazatlán", "reynosa", "matamoros", "celaya",
            "irapuato", "nuevo laredo", "ensenada", "coatzacoalcos", "oaxaca",
            "tlalnepantla", "tampico", "cuernavaca", "zacatecas", "uruapan",
            "nogales", "pachuca", "cuautitlán", "tapachula", "delicias",
        ],
    },
    "norwegian": {
        "enabled": True,
        "terms": [
            "norwegian", "norway", "oslo", "bergen", "trondheim", "stavanger",
            "kristiansand", "tromsø", "drammen", "fredrikstad", "skien",
            "sandnes", "sarpsborg", "bodø", "ålesund", "haugesund",
            "porsgrunn", "arendal", "tønsberg", "hamar", "ytre enebakk",
            "halden", "larvik", "askøy", "kongsberg", "harstad", "molde",
            "steinkjer", "lillehammer", "gjøvik", "kristiansund", "narvik",
            "horten", "leirvik", "mandal", "voss", "mo i rana", "namsos",
            "lillestrøm", "sandefjord", "hønefoss", "egersund", "kongsvinger",
            "raufoss", "rjukan",
        ],
    },
    "philippine": {
        "enabled": True,
        "terms": [
            "philippines", "filipino", "tagalog", "manila", "quezon city",
            "davao city", "caloocan", "cebu city", "zamboanga city",
            "antipolo", "pasig", "taguig", "cagayan de oro", "parañaque",
            "valenzuela", "las piñas", "makati", "bacolod", "muntinlupa",
            "iloilo city", "tarlac city", "baguio", "batangas city",
            "general santos", "lapu-lapu", "iligan", "olongapo", "binan",
            "santa rosa", "tagum", "tacloban", "malolos", "navotas",
            "dagupan", "toledo", "lucena", "san fernando", "cabanatuan",
            "ormoc", "dasmariñas", "san juan", "baliuag", "tuguegarao",
            "malabon", "mabalacat", "cotabato city", "puerto princesa",
            "butuan",
        ],
    },
    "polish": {
        "enabled": True,
        "terms": [
            "poland", "warsaw", "kraków", "łódź", "wrocław", "poznań",
            "gdańsk", "szczecin", "bydgoszcz", "lublin", "białystok",
            "katowice", "gdynia", "częstochowa", "radom", "sosnowiec",
            "toruń", "kielce", "rzeszów", "gliwice", "zabrze", "olsztyn",
            "bielsko-biała", "bytom", "zielona góra", "rybnik", "tarnów",
            "opole", "gorzów", "dąbrowa", "górnictwo", "elbląg", "płock",
            "wałbrzych", "chorzów", "tychy", "jaworzno", "jastrzębie",
            "zdrój", "mysłowice", "legnica", "lubin", "siedlce", "inowrocław",
            "piotrków", "trybunalski", "ostrołęka",
        ],
    },
    "portuguese": {
        "enabled": True,
        "terms": [
            "portuguese", "portugal", "lisbon", "porto", "vila nova",
            "amadora", "braga", "funchal", "coimbra", "setúbal", "queluz",
            "agualva-cacém", "aveiro", "viseu", "amora", "rio tinto",
            "matosinhos", "évora", "castelo branco", "guimarães",
            "vila franca", "santarém", "vila do conde", "ponte de lima",
            "loures", "póvoa de varzim", "faro", "sever do vouga", "paredes",
            "penafiel", "lagos", "odivelas", "ovar", "maia", "beja",
            "gondomar", "covilhã", "águeda", "fafe", "almada", "elvas",
            "torres vedras", "loulé", "portalegre", "barcelos",
            "caldas da rainha", "leiria",
        ],
    },
    "scottish": {
        "enabled": True,
        "terms": [
            "scottish", "scotland", "edinburgh", "glasgow", "aberdeen",
            "dundee", "inverness", "stirling", "perth", "fife", "falkirk",
            "ayr", "east kilbride", "livingston", "cumbernauld", "kilmarnock",
            "greenock", "coatbridge", "glenrothes", "airdrie", "kirkcaldy",
            "dunfermline", "dumfries", "motherwell", "paisley", "renfrew",
            "irvine", "giffnock", "newton mearns", "cambuslang", "barrhead",
            "blantyre", "stranraer", "bellshill", "kirkintilloch", "wishaw",
            "nairn", "buckie", "portree", "inverurie", "alloa", "bathgate",
            "dingwall", "elgin", "fort william", "hawick", "jedburgh",
        ],
    },
    "spanish": {
        "enabled": True,
        "terms": [
            "spanish", "spain", "madrid", "barcelona", "valencia", "seville",
            "zaragoza", "málaga", "murcia", "palma", "las palmas", "bilbao",
            "alicante", "córdoba", "valladolid", "vigo", "gijón",
            "l'hospitalet", "a coruña", "vitoria", "granada", "elche",
            "oviedo", "badalona", "terrassa", "cartagena", "sabadell",
            "jerez", "móstoles", "santa cruz", "alcalá", "fuenlabrada",
            "almería", "leganés", "san sebastián", "getafe", "burgos",
            "albacete", "santander", "castellón", "logroño", "badajoz",
            "huelva", "salamanca", "lérida", "tarragona", "león",
        ],
    },
    "swedish": {
        "enabled": False,
        "terms": [
            "swedish", "swede", "swedes", "scandinavian", "stockholm",
            "sweden", "gothenburg", "malmö", "uppsala", "linköping",
            "norrköping", "örebro", "västerås", "helsingborg", "jönköping",
            "umeå", "lund", "borås", "sundsvall", "gävle", "östersund",
            "eskilstuna", "södertälje", "halmstad", "växjö", "karlstad",
            "trollhättan", "örnsköldsvik", "kalmar", "kristianstad", "falun",
            "borlänge", "skövde", "karlskrona", "visby", "luleå", "märsta",
            "alingsås", "vänersborg", "täby", "hässleholm", "trelleborg",
            "nyköping", "piteå", "lidingö",
        ],
    },
    "reproductive_health": {
        "enabled": True,
        "terms": [
            "abortion", "contraception", "birth control", "family planning",
            "reproductive health", "reproductivity", "sterilization", "ivf",
            "in vitro fertilization", "pregnancy", "miscarriage",
            "stillbirth", "menstruation", "menstrual health", "menses",
            "ovulation", "ovarian", "uterus", "womb", "fertility treatment",
            "assisted reproduction", "egg donation", "sperm donation",
            "surrogacy", "adoption", "parental leave", "maternity leave",
            "paternity leave", "reproductive rights", "reproductive justice",
            "sexual health", "sexual education", "family planning clinic",
            "planned parenthood", "morning-after pill", "ru-486",
            "emergency contraception", "iud", "implant", "tubal ligation",
            "vasectomy", "condom", "diaphragm", "cervical cap",
            "birth spacing", "reproductive freedom", "pro-choice", "pro-life",
            "reproductive autonomy",
        ],
    },
    "LCOH Corporations": {
        "enabled": True,
        "terms": [
            "Dernham and Kaufmann", "Hodgin's Drug Store",
            "Humbird Lumber Company", "McGoldrick Lumber Company",
            "Olson & Johnson", "Pleasant Home", "Gallup Lumber Yard",
            "Polson Logging Company", "Rosauers",
            "Rutledge Lumber and Manufacturing Company",
            "Troy Lumber Company", "Weyerhaeuser Timber Company", "WI&M",
            "Washington, Idaho & Montana Railway", "Winters and Godsworth",
            "Winton Lumber Company", "White Pine Mill",
        ],
    },
    "LCOH Flora & Fauna": {
            "enabled": True,
            "terms": [
                "Appaloosa", "Badger", "Bear Den", "Beaver", "Belgian horse", "Bison",
                "Bitterroot", "Blister Rust", "Bluebird", "Buck", "Buffalo",
                "Bunchgrass", "Camas", "Catface", "Cayuse", "Chicken", "Chipmunk",
                "Chokecherry", "Clydesdale", "Cougars", "Cous", "Coyote", "Crow",
                "Doe", "Duck", "Eagle", "Ewe", "Ferret", "Finch", "Fox", "Frog",
                "Gaggle", "Goat", "Gopher", "Hawk", "Hawks", "Herd", "Herefords",
                "Horse", "Huckleberry", "Kinnikinnick", "Lamb", "Lizard", "Marmot",
                "Mink", "Moose", "Morgan", "Mountain Lions", "Muskrat", "Newt",
                "Otter", "Owl", "Paw", "Percherons", "Pig", "Ponderosa Pine",
                "Possum", "Prairie Dog", "Quail", "Quarter Horse", "Rabbit",
                "Raccoon", "Raven", "Ribes", "Sagebrush", "Salamander",
                "Salmon Hatchery", "Sarvisberry", "Shadbush", "Shire", "Skunk",
                "Smudge Fire", "Snake Bite", "Sparrow", "Squirrel", "Stag",
                "Steelhead", "Syringa", "Tamarack", "Toad", "Turkey", "Weasel",
                "Whale Pod", "Wolf Pack", "Wolves", "Yampa",
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
    "LCOH Eastern European": {
        "enabled": True,
        "terms": [
            "Austrian", "Bohemian", "Bohunk", "Bull Hunk", "Croat", "Czech",
            "Hungarian", "Hunk", "Hunkie", "Hunky", "Polack", "Pole", "Polish",
            "Rooshian", "Russian", "Ruthenian", "Serbian", "Slav", "Slavic",
            "Slavonian", "Slovack", "Slovak",
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
            "Swinomish", "Tenino Indian", "Tillamook", "Tribe", "Tukudeka",
            "Tulalip", "Umatilla Indian", "Umpqua", "Walla Walla Indian",
            "Wanapum", "Warm Springs Indian", "Wasco Indian",
            "Wenatchee Indian", "Wenatchi", "Western Shoshone",
            "Willamette Valley Indian", "Yakama Indian",
        ],
    },
    "LCOH Romani": {
        "enabled": True,
        "terms": [
            "Gipsy", "Gypsies", "Gypsy", "Roma", "Romani", "Romany", "Vardo",
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
    "LCOH Thrashing": {
            "enabled": True,
            "terms": [
                "Band Cutter", "Belt Pulley", "Binder", "Blower", "Bundle",
                "Bundle Pitcher", "Bundle Wagon", "Bundling", "Chaff",
                "Combine Harvester", "Cook Car", "Cook Shack", "Custom Thresher",
                "Engineer", "Feeder", "Fireman", "Grain Harvest", "Grain Sack",
                "Grain Wagon", "Harvest Crew", "Header", "Header Box",
                "Header Puncher", "Sack Sewer", "Self-Feeder", "Separator",
                "Separator Man", "Sheaf", "Sheaves", "Shock", "Shockers",
                "Shocking", "Spike Pitcher", "Stacker", "Steam Engine", "Stook",
                "Straw Stack", "Thrasher", "Thrashing Crews", "Threshing",
                "Threshing Machine", "Threshing Run", "Traction Engine", "Twine",
                "Water Boy", "Water Wagon", "Weigher", "Wheat Harvest",
            ],
    },
    "LCOH Timber": {
        "enabled": True,
        "terms": [
            "Jungle", "Jungling-Up", "Air Drying", "Bateau", "Beam", "Board Foot", "Boom", "Boom Stick",
            "Buffer Strip", "Bullgang", "Cant Hook", "Cat Skinner", "Chainsaw",
            "Check-Scaler", "Chipboard", "Choke-Setter", "Clear Cutting",
            "Crawler", "Crosscut", "Cruiser", "Debarking", "Deforestation",
            "Derrick Team", "Dogging", "Dray Logging", "Draymen",
            "Driving Crew", "Edgeman", "Felling", "Flume", "Flunkeying",
            "Flunkies", "Flying squad", "Forest Conservation", "Forestry",
            "Go-devil", "Gyppoing", "Hardwood", "Hectare Yield",
            "Highline Man", "Hooker", "Jammer", "Kiln Drying", "Lath",
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
    "LCOH Organizations": {
            "enabled": True,
            "terms": [
                "Coxey's Army", "Coxeyites", "Daughters of Rebekah",
                "Emergency Relief Administration", "Foster School of Healing",
                "GAR", "Grand Army of the Republic", "Hayu Club",
                "Idaho Emergency Relief Administration", "IERA",
                "Independent Order of Odd Fellows", "Odd Fellows", "IOOF", "K of P", "Kiwanis",
                "Kiwanis Club", "KKK", "Klan", "Knights of Pythias",
                "Knights of the Maccabees", "Ku Klux Klan", "Ladies Aid",
                "Ladies Auxiliary", "Ladies' Auxiliaries", "Maccabee Lodge",
                "Maccabees", "Odd Fellows Hall", "Pioneer Club", "Psychiana",
                "QAE Club", "Rebekah Lodge", "Rebekahs", "Runt Club Skating Party",
                "Soroptimist Club", "Soroptimists", "WCTU",
                "Women of the Woodcraft", "Women's Christian Temperance Union",
                "Woodman of the World", "Woodmen of the World", "WOW",
            ],
        },
    "LCOH People": {
        "enabled": True,
        "terms": [
            "Harry Adams", "Ed Allen", "Axel Anderson", "The Big Swede",
            "Malcher Anderson", "Uncle Ben", "Andrew Bloom", "Ole Bohman",
            "Ollie Bowman", "Charles Bolles", "Platten Bomberg",
            "Broomface Brooks", "Clay Hall Brown", "Sleigh Hall Brown",
            "Mike Bubley", "Joe Buck", "Herman Byers", "Warner H. Carithers",
            "Gene Chinaman", "Ted Collins", "Lillian Cooks",
            "The Nordic Queen", "George Creighton", "Cumberford",
            "Walking Daily", "Old Joe Davis", "William Deary",
            "Clifford M. Drury", "Cecil Emmet", "Swan Erikson",
            "Laughing Jim Delaney", "Pack Sack Dick", "Dick Farrell",
            "Henry Flasher", "Old George Foss", "Robert Foster",
            "Wood 'em Up George", "Hurdy-Gurdy Girls", "C.B. Green",
            "Old John Grohl", "Cryin' Gus", "William Helmer", "Lynn Henry",
            "Mox Herzog", "Ed Hill", "Dode Holmes", "Tom Hopkins",
            "Allison W. Laird", "Missy Lee", "August Leising", "Aaron Levi",
            "Anna Webster Litle", "Old Codger Jack", "Cougar Jack",
            "Ira Jenks", "Samuel T. Red Rosie Joe", "T.P. Jones",
            "Broken Ass John", "Albert Justice", "Shorty Justice", "Palouser",
            "Tilly Pelton", "Butterfly Pete", "Old Gil Pippen", "Big Gil",
            "Sam Piwash", "Old Sundown Jackson", "Powderpuff Johnny",
            "Seven Jackets", "Prune Joe", "Pat Malone", "Billy Marsh",
            "Dirty Shirt Martin", "Powderpuff McDonald", "Sam McKeon",
            "George McKinnon", "Laughin' Mike", "Bill Morland",
            "Ridge Runner", "Mox-Mox", "C.G. Naugle", "Nick the Greek",
            "Rosenstein's", "Jake Rosenstein", "Henry Plummer", "Pete Olson",
            "Big Gil Pippen", "Joe Rivers", "Jacob Rosenstein",
            "Sam Samovich", "Sells-Floto Circus", "Shefflins", "Shivaree",
            "Whitliff R. Smith", "Jackson Sundance", "Frank Tom",
            "Shorty Trimble", "Ollie Vincent", "John P. Vollmer",
            "J.P. Wahlberg", "Red Watson", "Joe Wells", "Milford Welch",
            "Wild Davey", "Friedrich Weyerhaeuser", "Doc White",
            "M.F. Zumhof",
        ],
    },
   "LCOH Places": {
        "enabled": True,
        "terms": [
            "caldwell", "idaho falls", "pocatello", "rupert", "boise",
            "nampa", "emmett", "twin falls", "burley", "moscow", "lewiston",
            "mountain home", "blackfoot", "post falls", "sandpoint",
            "jerome, idaho", "weiser", "eagle, idaho", "middleton",
            "rathdrum", "bonners ferry", "st. maries", "spirit lake",
            "glenns ferry", "parma", "kimberly", "st. anthony", "gooding",
            "mccall, idaho", "driggs", "american falls", "grangeville",
            "fountain, idaho", "acequia", "albion", "arco", "athol",
            "bellevue", "bloomington", "bruneau", "buhl", "challis",
            "clayton", "clifton", "cottonwood", "council, idaho", "crouch",
            "culdesac", "dayton, idaho", "dover", "downey", "drummond",
            "dubois", "elk city", "fairfield", "fenn", "fernwood",
            "fort hall", "fruitland", "garden city", "genesee", "greenleaf",
            "hagerman", "hansen, idaho", "hazelton", "heyburn", "holbrook",
            "homedale", "horseshoe bend", "huetter", "huston, idaho", "inkom",
            "iona", "julietta", "kamiah", "kendrick, idaho", "ketchum",
            "kooskia", "kootenai", "kuna", "lapwai", "lava hot springs",
            "leadore", "lemhi", "letha", "lost river", "mackay", "malad city",
            "malta", "marsing", "melba, idaho", "menan", "mink creek",
            "montpelier", "monteview", "montour", "moore, idaho",
            "mountain home afb", "mud lake", "mullan", "murtaugh", "newdale",
            "new meadows", "new plymouth", "nezperce, idaho", "notus",
            "oakley", "oldtown", "onaway", "orofino", "osburn, idaho",
            "parker", "parkline", "payette", "peck", "picabo", "pinehurst",
            "placerville", "plummer", "pollock", "potlatch", "preston",
            "priest lake", "priest river", "rexburg", "richfield", "rigby",
            "rimini", "riverside", "rockford", "rockland", "sagle",
            "shelley, idaho", "shoshone", "smelterville", "soda springs",
            "spalding", "spencer", "stanley, idaho", "sugar city",
            "sun valley", "swan valley", "terry, idaho", "teton", "tetonia",
            "troy, idaho", "uhland", "victor, idaho", "wallace, idaho",
            "wardner", "warm river", "weippe", "wendell", "weston",
            "white bird", "wilder", "winchester", "worley",
            "agatha", "aggipah mountain", "almota", "alsea",
            "american ridge", "anderson", "angel ridge", "andersonville prison",
            "arrow", "asotin", "ahsahka", "aspendale", "bald mountain",
            "beals butte", "bear creek", "beartrack creek", "beeson meadows",
            "benewah county", "bergen, norway", "big bear ridge", "bluestem",
            "bonanza", "bovard", "bovill", "box and goose", "burnt ridge",
            "buzzard roost", "bremerton", "cameron", "camp kenjockety",
            "cashup davis hotel", "cavendish", "cedar ridge", "chatcolet lake",
            "chehalis", "cheney", "cherry butte", "christianson meadow",
            "clarkia", "clarkston", "clarksville", "cloquet, minnesota",
            "collins", "colton", "coeur d'alene", "corral creek", "craigmont",
            "cranbrook, bc", "crumarine gulch", "cusick", "deary", "dogger",
            "driscoll ridge", "dry ridge", "dublin", "dworshak dam", "ellensburg",
            "elk river", "emida", "endicott", "ephrata", "fairview",
            "fix ridge", "fourmile creek", "frazier", "frederickson",
            "gang saw", "garfield", "ghormley park", "gifford", "gilt edge mine",
            "hampton", "harvard", "hatter creek", "heyburn park", "hayden",
            "helmer", "hog meadow creek", "hope", "hoodoo", "hoodoo mountains",
            "hood river", "hoquiam", "howell", "idler's rest", "joel",
            "juliaetta", "kelly creek", "kibbie dome", "laclede", "lake gamlin",
            "lake waha", "lapwai reservation", "larkins peak", "larkins lake",
            "leavenworth", "leland", "linville", "little bear ridge",
            "lochsa river", "lolo pass, mo", "luella mine", "mcgary butte",
            "melrose ridge", "metaline falls", "mica mountain", "mica peak",
            "mizpah mine", "moeller", "moose creek", "muscovite mine",
            "nespelem", "nora", "okanagan", "omak", "oviatt meadows",
            "owyhee mountains", "paradise ridge", "payette lake", "pedicord hotel",
            "pembine", "pomeroy", "potato hill", "princeton", "pullman",
            "randall flat", "randall flat creek", "reardan", "ridenbaugh canal",
            "riparia", "ritzville", "rosalia", "rosenstein store",
            "saint maries", "sacheen lake", "salubria", "sand mountain",
            "sausalito", "scoville", "selway-bitterroot wilderness",
            "shea meadows", "silverton", "slabtown", "snoqualmie falls",
            "sodaville", "sotin creek", "spangle", "southwick",
            "spokane", "steptoe butte", "stites", "swamp creek",
            "teakean butte", "tensed", "texas ridge", "tomer butte",
            "toppenish", "uniontown", "vassar meadows", "viola",
            "vollmer", "waha lake", "walla walla", "wenatchee",
            "west fork", "whitmore school", "wilson creek", "woodfell", "yale",
            "yreka mining district",
        ],
    },
    "LCOH Play": {
        "enabled": True,
        "terms": [
            "Andy Over", "Basket Socials", "Bean Bake", "Bierstammtisch",
            "Black Man", "Bullfrog on the Bank", "Chautauquas", "Chesters",
            "Cheeky Pins", "Coasting Parties", "Darebase", "Debates",
            "Decoration Day", "Dialogues", "Do-si-do",
            "Drop the Handkerchief", "Fan-Tan",
            "Flinch Muggins Stock Exchange Card Game", "Flinch and Muggins",
            "Flying Dutchman", "Guess the Skull", "Gustav's Skoal",
            "Gustafs Skål", "Hambo", "Kitchen Sweats", "Kris Krinkles",
            "Leapfrog", "Literaries", "Miller Boy", "Mumblety-Peg",
            "Old Mother Pigeon", "Pie Social", "Piecake-a-Mile", "Pinochle",
            "Post Office", "Potlatch Days", "Pump Pump Pullway",
            "Pom-Pom-Pull-Away", "Pussy Wants a Corner", "Puss in the Corner",
            "Quadrilles", "Quilting Parties", "Reading Room", "Rinky Dinks",
            "Run Sheep Run", "Schottische", "Sells Floto Circus", "Shinny",
            "Shinny On Your Own Side", "Shivaree", "Skip to My Lou",
            "Snipe Hunting", "Spin the Platter", "Spud Hill", "Three Deep",
            "Toboggan Parties", "Vanilla Bar", "Virginia Reel", "Winkum",
            "Wink 'Em", "Winter Fox and Goose",
        ],
    },
    "LCOH Rural Schools": {
        "enabled": True,
        "terms": [
            "Applequist", "Brannon", "Buckhorn", "Elwood", "Fern Hill",
            "Liberty", "Pleasant Hill", "Rimrock", "Spring Valley", "Steele",
            "Taney",
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