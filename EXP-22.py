# Simple Reference Resolution Program

text = [
    "John went to the market.",
    "He bought some fruits.",
    "He returned home."
]

# Assume 'He' refers to the last mentioned person
last_person = None

for sentence in text:
    words = sentence.split()

    if words[0] not in ["He", "She", "They"]:
        last_person = words[0]

    resolved_sentence = sentence

    if words[0] in ["He", "She", "They"] and last_person:
        resolved_sentence = sentence.replace(words[0], last_person)

    print("Original :", sentence)
    print("Resolved :", resolved_sentence)
    print()
