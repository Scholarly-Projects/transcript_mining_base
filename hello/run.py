from header import preprocess_text, stop_words
from general import (
    agriculture,
    animals,
    clothing,
    conflict,
    crime,
    culture,
    economy,
    education,
    environment,
    family,
    food_and_drink,
    happiness,
    hardship,
    health,
    history,
    indigenous,
    labor,
    migration,
    recreation,
    religion,
    technology,
    file_paths,
    dfs
)
from geographic import (
    basque,
    britain,
    canada,
    china,
    finland,
    france,
    germany,
    greece,
    idaho,
    india,
    ireland,
    italy,
    japan,
    mexico,
    norway,
    philippines,
    poland,
    portugal,
    scotland,
    spain,
    sweden
)
from custom import (
    find_marriage_and_divorce_terms,
    find_motherhood_terms,
    find_reproductive_rights_terms
)

# Concatenate text data from all dataframes into a single corpus
corpus = concatenate_text(dfs)

# Preprocess the entire corpus
cleaned_corpus = preprocess_text(corpus)

# General section terms
general_sections = {
    "agriculture": agriculture,
    "animals": animals,
    "clothing": clothing,
    "conflict": conflict,
    "crime": crime,
    "culture": culture,
    "economy": economy,
    "education": education,
    "environment": environment,
    "family": family,
    "food_and_drink": food_and_drink,
    "happiness": happiness,
    "hardship": hardship,
    "health": health,
    "history": history,
    "indigenous": indigenous,
    "labor": labor,
    "migration": migration,
    "recreation": recreation,
    "religion": religion,
    "technology": technology
}

# Print general section terms
for section_name, section_function in general_sections.items():
    top_terms = section_function(cleaned_corpus)
    print(f"*{section_name}")
    for word, count in top_terms:
        print(f"{word.capitalize()}: {count}")

# Geographic section terms
geographic_sections = {
    "basque": basque,
    "britain": britain,
    "canada": canada,
    "china": china,
    "finland": finland,
    "france": france,
    "germany": germany,
    "greece": greece,
    "idaho": idaho,
    "india": india,
    "ireland": ireland,
    "italy": italy,
    "japan": japan,
    "mexico": mexico,
    "norway": norway,
    "philippines": philippines,
    "poland": poland,
    "portugal": portugal,
    "scotland": scotland,
    "spain": spain,
    "sweden": sweden
}

# Print geographic section terms
for section_name, section_function in geographic_sections.items():
    top_terms = section_function(cleaned_corpus)
    print(f"*{section_name}")
    for word, count in top_terms:
        print(f"{word.capitalize()}: {count}")

# Custom section terms
custom_sections = {
    "marriage_and_divorce": find_marriage_and_divorce_terms,
    "motherhood": find_motherhood_terms,
    "reproductive_rights": find_reproductive_rights_terms
}

# Print custom section terms
for section_name, section_function in custom_sections.items():
    top_terms = section_function(cleaned_corpus)
    print(f"*{section_name}")
    for word, count in top_terms:
        print(f"{word.capitalize()}: {count}")
