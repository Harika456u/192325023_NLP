import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define a Probabilistic Context-Free Grammar
grammar = PCFG.fromstring("""
S -> NP VP [1.0]

NP -> Det N [0.6]
NP -> 'John' [0.4]

VP -> V NP [1.0]

Det -> 'the' [0.5]
Det -> 'a' [0.5]

N -> 'cat' [0.5]
N -> 'dog' [0.5]

V -> 'chased' [0.6]
V -> 'saw' [0.4]
""")

# Create Viterbi Parser
parser = ViterbiParser(grammar)

# Input sentence
sentence = "John saw the dog".split()

# Parse sentence
for tree in parser.parse(sentence):
    print(tree)
    print("Probability =", tree.prob())
