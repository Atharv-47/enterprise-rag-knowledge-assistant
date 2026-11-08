import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def generate_answer(question, context):

    
    
    prompt = f"""
    You are an enterprise document question-answering assistant.

    STRICT INSTRUCTIONS:

    1. Answer using ONLY the information provided in the context.
    2. Do not use external knowledge or make unsupported assumptions.
    3. Cite factual statements using the source ID provided in the context.
    4. Use this exact citation format: [1], [2], etc.
    5. Use only source IDs that actually appear in the context.
    6. Place citations immediately after the statements they support.
    7. If the context does not contain enough information,
       clearly state that the information is not available.
    8. Follow the requested answer format and sentence count.

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