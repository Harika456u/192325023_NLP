import random
from collections import defaultdict

# Training text
text = "I love natural language processing and I love machine learning"

# Tokenize text
words = text.split()

# Build Bigram Model
bigram_model = defaultdict(list)

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    bigram_model[current_word].append(next_word)

# Generate text
current_word = random.choice(words)
generated_text = [current_word]

for _ in range(10):
    if current_word in bigram_model:
        next_word = random.choice(bigram_model[current_word])
        generated_text.append(next_word)
        current_word = next_word
    else:
        break

print("Generated Text:")
print(" ".join(generated_text))
