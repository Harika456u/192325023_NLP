import nltk
from nltk.stem import PorterStemmer

# Create stemmer object
stemmer = PorterStemmer()

# List of words
words = ["running", "runner", "studies", "studying", "played", "playing"]

print("Morphological Analysis using Stemming:")
for word in words:
    stem = stemmer.stem(word)
    print(f"{word} --> {stem}")
