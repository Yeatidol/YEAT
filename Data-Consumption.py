import requests
import asyncio

def call_endpoint():
    asyncio.run(get_recent_boosted())  

async def get_recent_boosted():
    historical_price_endpoint = "https://api.dexscreener.com/token-boosts/latest/v1"
    try:
        response = requests.get(historical_price_endpoint)
        if response.status_code == 200:
            posts = response.json()
            print(posts)
            return posts
        else:
            print("Error", response.status_code)
            return None
    except requests.RequestException as e:
        print("Unexpected Error:", e)
        return None

# Calling the function correctly
call_endpoint()
