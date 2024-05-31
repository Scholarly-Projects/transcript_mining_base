from collections import Counter
import re

def find_marriage_and_divorce_terms(corpus):
    marriage_and_divorce_terms = ["marriage", "wedding", "bride", "groom", "engagement", "fiance", "fiancee", "spouse", "husband", "wife", "vows", "ceremony", "reception", "anniversary", "honeymoon", "divorce", "separation", "alimony", "custody", "prenup", "ring", "proposal", "love", "commitment", "partnership", "union", "betrothal", "elopement", "matrimony", "nuptials", "celebration", "toast", "bridesmaid", "groomsman", "officiant", "invitation", "registry", "bridal", "shower", "bachelor", "bachelorette", "dowry", "veil", "tuxedo", "bouquet", "aisle", "altar", "honeymoon", "settlement"]

    # Initialize a counter for marriage and divorce-related terms
    marriage_and_divorce_word_freq = Counter()

    # Tokenize the corpus
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a marriage or divorce-related term
        if word in marriage_and_divorce_terms:
            marriage_and_divorce_word_freq[word] += 1

    # Return the top 50 most common marriage and divorce-related terms
    return marriage_and_divorce_word_freq.most_common(50)

def find_motherhood_terms(corpus):
    motherhood_terms = ["mother", "mom", "mum", "mommy", "mummy", "maternal", "motherhood", "pregnancy", "birth", "newborn", "baby", "infant", "toddler", "parenting", "nurture", "care", "breastfeeding", "childbirth", "maternity", "postpartum", "labor", "delivery", "child", "family", "nanny", "midwife", "doula", "contractions", "prenatal", "obstetrician", "gynecologist", "nursery", "pacifier", "crib", "diaper", "stroller", "carriage", "playpen", "bottle", "formula", "lullaby", "nanny", "babysitter", "swaddle", "onesie", "highchair", "milk", "pediatrician", "growth"]

    # Initialize a counter for motherhood-related terms
    motherhood_word_freq = Counter()

    # Tokenize the corpus
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a motherhood-related term
        if word in motherhood_terms:
            motherhood_word_freq[word] += 1

    # Return the top 50 most common motherhood-related terms
    return motherhood_word_freq.most_common(50)

def find_reproductive_rights_terms(corpus):
    reproductive_rights_terms = ["abortion", "contraception", "birth control", "family planning", "reproductive health", "fertility", "sterilization", "IVF", "in vitro fertilization", "pregnancy", "miscarriage", "stillbirth", "menstruation", "menstrual health", "period", "ovulation", "ovarian", "uterus", "womb", "fertility treatment", "assisted reproduction", "egg donation", "sperm donation", "surrogacy", "adoption", "parental leave", "maternity leave", "paternity leave", "reproductive rights", "reproductive justice", "sexual health", "sexual education", "family planning clinic", "Planned Parenthood", "morning-after pill", "RU-486", "emergency contraception", "IUD", "implant", "tubal ligation", "vasectomy", "condom", "diaphragm", "cervical cap", "birth spacing", "reproductive freedom", "pro-choice", "pro-life", "reproductive autonomy"]

    # Initialize a counter for reproductive rights-related terms
    reproductive_rights_word_freq = Counter()

    # Tokenize the corpus
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Iterate over each token in the corpus
    for word in tokens:
        # Check if the token is a reproductive rights-related term
        if word in reproductive_rights_terms:
            reproductive_rights_word_freq[word] += 1

    # Return the top 50 most common reproductive rights-related terms
    return reproductive_rights_word_freq.most_common(50)
