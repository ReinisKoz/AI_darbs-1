# app.py
import os
from dotenv import load_dotenv
from utils import summarize_text, generate_keywords, generate_quiz

load_dotenv()  # load .env vars

def main():
    print("=== AI Console App ===")

    file_path = input("Enter path to .txt file: ").strip()

    if not os.path.exists(file_path):
        print("❌ File not found.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    print("\n✨ Generating summary...")
    summary = summarize_text(text)
    print("\n--- SUMMARY ---")
    print(summary)

    print("\n🔑 Generating keywords...")
    kw_count = int(input("How many keywords to generate? (default 5): ") or 5)
    keywords = generate_keywords(text, kw_count)
    print("\n--- KEYWORDS ---")
    for k in keywords:
        print("•", k)

    print("\n🧠 Generating quiz...")
    q_count = int(input("How many quiz questions? (default 5): ") or 5)
    quiz = generate_quiz(text, q_count)

    print("\n--- QUIZ ---")
    print(quiz)

    print("\n✅ Done!")

if __name__ == "__main__":
    main()
