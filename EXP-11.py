import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

# Define a Context-Free Grammar (CFG)
grammar = CFG.fromstring("""
S  -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog'
V -> 'chased' | 'saw'
""")

# Create Top-Down Parser
parser = RecursiveDescentParser(grammar)

# Input sentence
sentence = "the cat chased a dog".split()

# Parse the sentence
for tree in parser.parse(sentence):
    print(tree)
