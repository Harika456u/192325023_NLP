import nltk
from nltk import word_tokenize, pos_tag
from nltk.chunk import RegexpParser

# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

# Input sentence
sentence = "The intelligent student reads a natural language processing book"

# Tokenization and POS tagging
words = word_tokenize(sentence)
tagged_words = pos_tag(words)

# Define grammar for Noun Phrase (NP)
grammar = "NP: {<DT>?<JJ>*<NN.*>+}"

# Create chunk parser
chunk_parser = RegexpParser(grammar)

# Parse sentence
tree = chunk_parser.parse(tagged_words)

print("Noun Phrases Found:")
print("-" * 30)

for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        noun_phrase = " ".join(word for word, tag in subtree.leaves())
        print("Noun Phrase:", noun_phrase)
