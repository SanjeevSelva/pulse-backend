import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_FOOTBALL_KEY")

def get_live_fixtures():
    headers = {"x-apisports-key": API_KEY}
    response = requests.get(
        "https://v3.football.api-sports.io/fixtures?live=all",
        headers=headers
    )
    data = response.json()
    return data["response"]

if __name__ == "__main__":
    print(get_live_fixtures())