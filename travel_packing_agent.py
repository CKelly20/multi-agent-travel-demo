# Packing Agent - Gets weather context, suggests packing items

import json
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

with open("config.json") as f:
    config = json.load(f)

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
    api_key=os.getenv("AZURE_OPENAI_API_KEY", ""),
    api_version=config["azure_openai"]["api_version"],
)

DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "")
MAX_TOKENS = config["agents"]["packing"]["max_tokens"]

def get_packing_suggestions(weather_info: str) -> str:
    resp = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": "You are a travel packing assistant. Reply with 6-10 items, comma-separated."
            },
            {
                "role": "user",
                "content": f"Weather: {weather_info}\nPacking items only."
            },
        ],
        max_completion_tokens=MAX_TOKENS,
    )
    return (resp.choices[0].message.content or "").strip()

if __name__ == "__main__":
    print(get_packing_suggestions("Galway: 11°C, light rain, windy"))
