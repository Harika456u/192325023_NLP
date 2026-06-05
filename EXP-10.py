# Transformation-Based POS Tagging

# Initial tagging (all words tagged as NN)
sentence = "The cat is running quickly"

words = sentence.split()
tags = [(word, "NN") for word in words]

print("Initial Tags:")
print(tags)

# Transformation Rules
for i in range(len(tags)):
    word, tag = tags[i]

    # Rule 1: Words ending with 'ing' -> VBG
    if word.endswith("ing"):
        tags[i] = (word, "VBG")

    # Rule 2: Words ending with 'ly' -> RB
    elif word.endswith("ly"):
        tags[i] = (word, "RB")

    # Rule 3: Articles -> DT
    elif word.lower() in ["a", "an", "the"]:
        tags[i] = (word, "DT")

    # Rule 4: Forms of 'be' -> VB
    elif word.lower() in ["is", "am", "are", "was", "were"]:
        tags[i] = (word, "VB")

print("\nAfter Applying Transformation Rules:")
for word, tag in tags:
    print(word, "->", tag)
