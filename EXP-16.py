import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Sundar Pichai is the CEO of Google and lives in California."

# Process text
doc = nlp(text)

print("Named Entities:")
print("-" * 30)

for ent in doc.ents:
    print(f"{ent.text} --> {ent.label_}")
