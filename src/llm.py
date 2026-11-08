import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def generate_answer(question, context):

    prompt = f"""
    Answer the question using the context provided below.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text