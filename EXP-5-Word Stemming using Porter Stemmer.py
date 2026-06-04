import nltk
from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# List of words
words = ["running", "studies", "playing", "connected",
         "happiness", "fishing", "walked"]

print("Word Stemming using Porter Stemmer:")
for word in words:
    stem_word = ps.stem(word)
    print(word, "->", stem_word)
