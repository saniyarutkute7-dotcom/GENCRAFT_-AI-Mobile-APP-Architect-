import streamlit as st
from groq import Groq


def get_groq_client():
    """Create and return the Groq client."""
    return Groq(api_key=st.secrets["GROQ_API_KEY"])


def generate_response(
    prompt,
    model="openai/gpt-oss-20b",
    temperature=0.7,
    max_tokens=1024,
    system_prompt=None
):
    """
    Send a prompt to Groq and return the AI response.
    """

    try:
        client = get_groq_client()

        messages = []

        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })

        messages.append({
            "role": "user",
            "content": prompt
        })

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_completion_tokens=max_tokens
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Groq API Error: {str(e)}"
    