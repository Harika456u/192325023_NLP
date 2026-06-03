def generate_plural(noun):
    # Finite-state rules for plural formation

    if noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return noun + "es"

    elif noun.endswith('y') and noun[-2].lower() not in "aeiou":
        return noun[:-1] + "ies"

    else:
        return noun + "s"

# Test nouns
nouns = ["cat", "bus", "box", "baby", "church", "book"]

print("Plural Forms:")
for noun in nouns:
    print(noun, "->", generate_plural(noun))
