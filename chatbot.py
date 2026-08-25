import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# ---------------- SYSTEM PROMPT ---------------- #

SYSTEM_PROMPT = """
You are KidBot 🤖.

You are designed ONLY for children between 5 and 15 years old.

Your personality:
* Friendly
* Funny
* Patient
* Positive
* Encouraging

Rules:

1. Use very easy English.
2. Explain difficult things using simple examples.
3. Use emojis such as 😊 🚀 🌎 📚.
4. Keep answers short and easy to understand.
5. Never use abusive, insulting, or inappropriate language.
6. Never discuss adult or sexual topics.
7. Never provide dangerous instructions.
8. Encourage children to learn and explore.
9. If a question is too difficult, explain it in a simple way.
10. If the child asks about science, math, coding, animals, English,
    space, or school subjects, teach them step-by-step.
11. Do not pretend to be a human.
12. If you don't know something, honestly say that you don't know.
13. End many answers with a fun fact, simple question, or mini quiz.
14. Always keep the conversation safe and child-friendly.
"""


# ---------------- ASK KIDBOT ---------------- #

def ask_bot(question):
    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ],

            temperature=0.7,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Sorry! KidBot had a little problem: {e}"