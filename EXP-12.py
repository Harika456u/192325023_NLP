import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

# Define CFG Grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog'
V -> 'chased' | 'saw'
""")

# Create Earley Parser
parser = EarleyChartParser(grammar)

# Input sentence
sentence = "the cat chased a dog".split()

# Parse sentence
for tree in parser.parse(sentence):
    print(tree)
