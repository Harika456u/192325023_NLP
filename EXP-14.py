# Subject-Verb Agreement Checker

def check_agreement(sentence):
    words = sentence.lower().split()

    if len(words) < 2:
        return "Invalid sentence"

    subject = words[0]
    verb = words[1]

    singular_subjects = ["he", "she", "it", "boy", "girl", "cat", "dog"]
    plural_subjects = ["they", "we", "boys", "girls", "cats", "dogs"]

    singular_verbs = ["runs", "eats", "plays", "jumps"]
    plural_verbs = ["run", "eat", "play", "jump"]

    if subject in singular_subjects and verb in singular_verbs:
        return "Agreement Correct"

    elif subject in plural_subjects and verb in plural_verbs:
        return "Agreement Correct"

    else:
        return "Agreement Incorrect"


# Test Sentences
sentences = [
    "He runs",
    "They run",
    "She play",
    "Dogs jumps"
]

for s in sentences:
    print(s, "->", check_agreement(s))
