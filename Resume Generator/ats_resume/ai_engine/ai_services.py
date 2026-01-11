import os
import openai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_ai_suggestions(resume_text, job_description):
    """
    Gives simple ATS improvement suggestions
    """

    prompt = f"""
    Suggest ways to improve this resume for ATS.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Give 5 short bullet points.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )

    return response.choices[0].message.content
