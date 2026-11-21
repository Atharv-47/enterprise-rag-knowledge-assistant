import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def generate_answer(question, context):

    
    
    prompt = f"""
    You are an enterprise document question-answering assistant.

    STRICT INSTRUCTIONS:

    1. Answer using ONLY the information provided in the context.
    2. Do not use external knowledge or make unsupported assumptions.
    3. Before answering, determine whether the context contains
    sufficient information to answer the question.
    4. If the context is related to the question but does not
    contain the required answer, abstain.
    5. If the answer is unavailable, respond exactly:
    "I couldn't find sufficient information in the uploaded documents."
    6. Cite factual statements using the source ID provided in the context.
    7. Use this exact citation format: [1], [2], etc.
    8. Use only source IDs that actually appear in the context.
    9. Place citations immediately after the statements they support.
    10. Follow the requested answer format and sentence count
        whenever the answer is available.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """



    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )
        return response.text

    except errors.ServerError:
        return "Gemini is temporarily unavailable. Please try again later."

    except errors.APIError as e:
        return f"Gemini API error: {e}"