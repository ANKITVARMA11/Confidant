import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    models = openai.models.list()
    print("✅ API key is working. Models retrieved:", [m.id for m in models.data])
except Exception as e:
    print("❌ API key issue:", e)


from openai import OpenAI
client = OpenAI()

models = client.models.list()

for m in models.data:
    print(m.id)
