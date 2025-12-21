import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def setup_command_line_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Gemini AI Agent Tool"
    )

    parser.add_argument("prompt", help="Prompt text (required)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")

    return parser

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = []

    parser = setup_command_line_parser()
    args = parser.parse_args()

    response = client.models.generate_content(model=args.prompt)
    print(response.text)

    if args.verbose: 
        usage = response.usage_metadata
        print(f"User prompt: {args.prompt}\nPrompt tokens: {usage.prompt_token_count}\nResponse tokens: {usage.candidates_token_count}") # type: ignore

    messages.append(types.Content(role="user", parts=[types.Part(text=args.prompt)]))


if __name__ == "__main__":
    main()
