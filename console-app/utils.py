# utils.py
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def summarize_text(text: str) -> str:
    """Generate a summary using OpenAI."""
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Summarize the following text:\n{text}"}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()


def generate_keywords(text: str, count: int = 5) -> list[str]:
    """Generate keywords using OpenAI."""
    prompt = (
        f"Extract {count} important keywords from the following text. "
        "Return only a clean bullet list:\n\n{text}"
    )
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    keywords = response.choices[0].message.content.strip().split("\n")
    # Clean bullets
    keywords = [k.replace("-", "").strip() for k in keywords if k.strip()]
    return keywords[:count]


def generate_quiz(text: str, count: int = 5) -> str:
    """Generate quiz questions using OpenAI."""
    prompt = (
        f"Create {count} quiz questions based on this text. "
        "Each question should have 4 options and show the correct answer at the end.\n\n{text}"
    )
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()
