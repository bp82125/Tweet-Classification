import re
from nltk.tokenize import word_tokenize

def extract_hashtags(text):
    if text is None:
        return ""
    hashtags = re.findall(r'#\w+', text)
    return ' '.join(hashtags) if hashtags else ""


def split_hashtag(hashtag):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', hashtag)


def process_hashtag(hashtag):    
    text_no_hashtag = re.sub(r'#', '', hashtag)
    text_split_camel = split_hashtag(text_no_hashtag)

    tokens = word_tokenize(text_split_camel)

    return ' '.join([token.lower() for token in tokens])


def process_hashtag_string(hashtag_string):
    hashtags = hashtag_string.split()  
    
    return ' '.join([process_hashtag(tag) for tag in hashtags])
