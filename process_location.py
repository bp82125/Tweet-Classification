import re

def process_location(location):
    location = location.lower()
    location = re.sub(r'[^a-zA-Z\s]', '', location)
    location = re.sub(r'\s+', ' ', location)
    location = location.strip()

    return location
