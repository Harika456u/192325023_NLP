from transformers import pipeline

# Load translation pipeline
translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

# English text
text = "Natural Language Processing is an exciting field of Artificial Intelligence."

# Translate
result = translator(text)

print("English Text:")
print(text)

print("\nFrench Translation:")
print(result[0]['translation_text'])
