import nltk
from nltk.corpus import wordnet

# Download WordNet (run once)
nltk.download('wordnet')
nltk.download('omw-1.4')

# Input word
word = "bank"

# Get synsets
synsets = wordnet.synsets(word)

print("Synsets for the word:", word)
print("-" * 40)

for synset in synsets:
    print("Synset:", synset.name())
    print("Definition:", synset.definition())
    print("Examples:", synset.examples())
    print("-" * 40)
