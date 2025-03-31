import re
import spacy
import nltk
from nltk.corpus import stopwords

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Load stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_query(query):
    """
    Clean and normalize the query text.
    """
    # Lowercase the text
    query = query.lower()

    # Remove special characters, punctuation, and extra whitespace
    query = re.sub(r'[^a-zA-Z0-9\s]', '', query)
    query = re.sub(r'\s+', ' ', query).strip()

    # Remove stopwords
    tokens = query.split()
    filtered_tokens = [word for word in tokens if word not in stop_words]

    return ' '.join(filtered_tokens)

def extract_entities(query):
    """
    Extract business-related entities using spaCy.
    """
    doc = nlp(query)
    entities = {
        "ORG": [],
        "GPE": [],
        "PRODUCT": [],
        "PERSON": [],
        "MONEY": [],
        "DATE": []
    }

    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)

    return entities

def detect_query_type(query):
    """
    Detect if the query is simple or multi-step.
    """
    multi_step_keywords = ["and", "also", "then", "followed by", "after"]
    
    # Check if query contains multi-step indicators
    if any(keyword in query for keyword in multi_step_keywords):
        return "multi-step"
    
    return "simple"
