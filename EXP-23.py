from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

# Download required package
nltk.download('punkt')

text = """
Natural Language Processing is a field of Artificial Intelligence.
It helps computers understand human language.
NLP is used in chatbots and machine translation.
"""

# Split into sentences
sentences = sent_tokenize(text)

# Count common words between consecutive sentences
coherence_score = 0

for i in range(len(sentences) - 1):
    words1 = set(word_tokenize(sentences[i].lower()))
    words2 = set(word_tokenize(sentences[i + 1].lower()))

    common_words = words1.intersection(words2)
    coherence_score += len(common_words)

print("Number of Sentences:", len(sentences))
print("Coherence Score:", coherence_score)

if coherence_score > 0:
    print("The text is Coherent")
else:
    print("The text is Less Coherent")
