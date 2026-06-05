import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger


nltk.download('punkt')


patterns = [
    (r'.*ing$', 'VBG'),    # Verb ending with ing
    (r'.*ed$', 'VBD'),     # Verb ending with ed
    (r'.*es$', 'VBZ'),     # Verb ending with es
    (r'.*ly$', 'RB'),      # Adverb
    (r'.*ous$', 'JJ'),     # Adjective
    (r'.*ness$', 'NN'),    # Noun
    (r'.*ment$', 'NN'),    # Noun
    (r'.*', 'NN')          # Default tag
]

# Create rule-based tagger
tagger = RegexpTagger(patterns)

# Input sentence
sentence = "The boy is playing happily and finished his assignment"

# Tokenize
words = word_tokenize(sentence)

# Tag words
tagged = tagger.tag(words)

print("Word\tPOS Tag")
print("-" * 20)

for word, tag in tagged:
    print(f"{word}\t{tag}")
