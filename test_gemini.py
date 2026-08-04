from decouple import config
from google import genai

client = genai.Client(
    api_key=config("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model=config("GEMINI_MODEL"),
    contents="Hello what is ur name"
)

print(response.text)