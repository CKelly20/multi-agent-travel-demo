# Weather Agent - Extracts location, calls weather API

import json
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

with open("config.json") as f:
    config = json.load(f)

API_KEY = os.getenv("WEATHERAPI_KEY")
WEATHER_URL = config["weather_api"]["base_url"]

def get_weather(location: str, date: str) -> str:
    if not API_KEY:
        return "Weather API key missing"

    # make sure date input
    try:
        nice_date = datetime.strptime(date, "%Y-%m-%d").strftime("%B %d")
    except ValueError:
        return "Date format must be YYYY-MM-DD (e.g., 2026-02-10)"

    r = requests.get(
        WEATHER_URL,
        params={"key": API_KEY, "q": location}
    )
    data = r.json()

    if "error" in data:
        return data["error"]["message"]

    temp = data["current"]["temp_c"]
    desc = data["current"]["condition"]["text"]

    return f"{location} on {nice_date}: {temp}\u00b0C, {desc}"

if __name__ == "__main__":
    print(get_weather("Galway", "2026-02-10"))
