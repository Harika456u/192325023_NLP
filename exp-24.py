# Simple Dialog Act Recognition

def identify_dialog_act(sentence):
    sentence = sentence.lower()

    if sentence.endswith("?"):
        return "Question"

    elif sentence.startswith(("hello", "hi", "hey")):
        return "Greeting"

    elif sentence.startswith(("thank", "thanks")):
        return "Thanking"

    elif sentence.startswith(("bye", "goodbye")):
        return "Closing"

    else:
        return "Statement"


# Sample conversation
conversation = [
    "Hello",
    "How are you?",
    "I am fine",
    "Thanks for your help",
    "Goodbye"
]

print("Dialog Act Recognition")
print("-" * 30)

for sentence in conversation:
    print(f"{sentence} --> {identify_dialog_act(sentence)}")
