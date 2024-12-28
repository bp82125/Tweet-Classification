import json
import re
import string
from nltk.tokenize import word_tokenize

from lemmatize import lemmatize_word

with open('abbreviations.json', 'r') as f:
    contractions = json.load(f)


def expand_contractions(text):
    for contraction, full_form in contractions.items():
        text = re.sub(r'\b' + re.escape(contraction) + r'\b', full_form, text)

    return text


def process_text(text):
    text = text.lower()
    
    text = expand_contractions(text)
    
    text = re.sub(r'@\w+', '', text)
    
    text = re.sub(r'http[s]?://\S+', '', text)
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    
    text = re.sub(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', text)
   
    tokens = word_tokenize(text)

    processed_text = ' '.join([lemmatize_word(token) for token in tokens])

    processed_text = re.sub(r'\s+', ' ', processed_text).strip()
    return processed_text
