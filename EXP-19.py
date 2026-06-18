import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

# Download required resources
nltk.download('punkt')
nltk.download('wordnet')

# Sentence containing an ambiguous word
sentence = "I went to the bank to deposit money"

# Tokenize sentence
tokens = word_tokenize(sentence)

# Find the correct sense of the word "bank"
sense = lesk(tokens, 'bank')

print("Sentence:", sentence)
print("\nWord Sense:", sense)
print("Definition:", sense.definition())
