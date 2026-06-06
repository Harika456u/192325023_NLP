import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define CFG Grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog'
V -> 'chased' | 'saw'
""")

# Create Parser
parser = ChartParser(grammar)

# Input Sentence
sentence = "the cat chased a dog".split()

# Generate Parse Tree
for tree in parser.parse(sentence):
    print("Parse Tree:")
    print(tree)

    # Display tree graphically
    tree.pretty_print()
