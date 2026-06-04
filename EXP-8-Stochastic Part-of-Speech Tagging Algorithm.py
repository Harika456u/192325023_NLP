# Simple Stochastic POS Tagger

# Probabilistic dictionary of words and their possible POS tags
pos_probabilities = {
    "book": {"NN": 0.7, "VB": 0.3},
    "flies": {"NNS": 0.4, "VBZ": 0.6},
    "time": {"NN": 0.8, "VB": 0.2},
    "quickly": {"RB": 1.0},
    "the": {"DT": 1.0}
}

sentence = "the book flies quickly"
words = sentence.split()

print("Word\tPOS Tag")
print("-" * 20)

for word in words:
    if word in pos_probabilities:
        # Choose tag with highest probability
        tag = max(pos_probabilities[word],
                  key=pos_probabilities[word].get)
        print(f"{word}\t{tag}")
    else:
        print(f"{word}\tUNK")
