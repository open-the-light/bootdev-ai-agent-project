import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    messages = []

    try:
        user_prompt = sys.argv[1]
    except Exception as e:
        print("Enter your query as a command line argument please...")
        sys.exit(1)
    response = client.models.generate_content(model="gemini-2.0-flash-001",
                                              contents=user_prompt)

    usage = response.usage_metadata

    messages.append(types.Content(role="user", parts=[types.Part(text=user_prompt)]))
    print(response.text)
    print(f"Prompt tokens: {usage.prompt_token_count}\nResponse tokens: {usage.candidates_token_count}") # type: ignore


if __name__ == "__main__":
    main()
