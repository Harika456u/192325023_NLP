from openai import OpenAI

# Initialize client with your API key
client = OpenAI(
    api_key="YOUR_API_KEY"
)

# Input prompt
prompt = "Explain Natural Language Processing in simple words."

# Generate text
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print("Generated Text:\n")
print(response.output_text)
