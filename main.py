from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
import argparse


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
GOOGLE_GENAI_USE_VERTEXAI=False

#arg parser
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=messages
)
if (args.verbose):
    print("User prompt: " + args.user_prompt)
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

print("Response: \n" + response.text)