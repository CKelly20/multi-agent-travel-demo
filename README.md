# Travel Assistant Demo

A multi-agent travel assistant that uses an LLM-powered orchestrator to route user requests to specialised agents:

- **Weather Agent** - Fetches current weather for a destination using the WeatherAPI.
- **Packing Agent** - Suggests packing items based on weather conditions using Azure OpenAI.
- **Orchestrator** - Classifies user intent, extracts destination and date, and routes to the appropriate agent(s). When both agents are needed, it composes a single response from their outputs.

## Prerequisites

- Python 3.10+
- An Azure OpenAI resource with a deployed chat model
- A WeatherAPI key from [weatherapi.com](https://www.weatherapi.com/)

## Setup

1. Clone the repository:

```
git clone <repo-url>
cd travel-assistant-demo
```

2. Run the setup script to create a virtual environment and install dependencies:

```
setup.bat
```

Or do it manually:

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. Copy the sample environment file and fill in your API keys:

```
copy .env.sample .env
```

Edit `.env` with your actual values. See `.env.sample` for the required variables.

## Configuration

`config.json` contains non-secret configuration such as API versions, the weather API base URL, and token limits for each agent. Adjust these as needed.

## Running the Demo

```
python demo.py
```

This runs four test scenarios covering weather-only requests, packing-only requests, combined trip advice, and natural language variations.
