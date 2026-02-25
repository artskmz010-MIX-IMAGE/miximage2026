from google import genai

client = genai.Client(api_key="AIzaSyAQWzs1JXLuBuqZj4Zmsvr0f1QbFoZnR3g")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)