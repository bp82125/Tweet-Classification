from nltk.corpus import wordnet as wn, words as nltk_words, stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
english_words = set(nltk_words.words())


def load_custom_words(file_path):
    try:
        with open(file_path, 'r') as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        print(f"File {file_path} not found. Returning an empty set.")
        return set()


rejected_words = load_custom_words('rejected_words.txt')
accepted_words = load_custom_words('accepted_words.txt')


def is_english_word(word):
    if isinstance(word, str) and word.isalpha() and len(word) > 1:
        return word.lower() in english_words
    return False


def is_stop_words(word):
    return word in stop_words


def is_accepted_word(word):
    return word in accepted_words


def is_rejected_word(word):
    return word in rejected_words


def lemmatize_word(word):
    if len(word) == 1:
        return ""

    for pos in [wn.VERB, wn.ADJ, wn.ADV, wn.NOUN]:
        lemmatized_token = lemmatizer.lemmatize(word, pos=pos)

        if is_accepted_word(lemmatized_token):
            return lemmatized_token

        if is_english_word(lemmatized_token) and not is_stop_words(lemmatized_token) and not is_rejected_word(lemmatized_token):
            return lemmatized_token

    if is_english_word(word) and not is_stop_words(word) and not is_rejected_word(word):
        return word

    return ""
