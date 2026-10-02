from pathlib import Path
import textstat
import spacy

nlp = spacy.load("en_core_web_sm")

PACKAGE_DIR = Path(__file__).resolve().parent

def open_file(PACKAGE_DIR, file_path):
    complete_file_path = PACKAGE_DIR / file_path
    with open(complete_file_path, "r", encoding="utf-8") as f:
        return f.read()

file = open_file(PACKAGE_DIR, "data/sample-data-sherlock.txt")

print (textstat.coleman_liau_index(file))

doc = nlp(file)
content_tokens = [
    token.lemma_.lower()
    for token in doc
    if not token.is_punct and not token.is_space and not token.is_stop and not token.like_num
]

print (content_tokens)