import requests


Endpoint = "https://pro-api.coingecko.com/api/v3/"
trends = "https://api.coingecko.com/api/v3/search/trending"

Breakdown = []

crytrends = requests.get(trends)
coins = crytrends.json()["coins"]

for i in coins:
    symbol = i['item']['symbol']
    Name = i['item']['name']
    id = i['item']['id']
    paras = {
            "ids":id,
            "vs_currencies": "usd",
            "include_market_cap": "true",
        }
    Money = requests.get(url = "https://api.coingecko.com/api/v3/simple/price", params=paras)
    price = Money.json()[id]["usd"]
    Breakdown.append(f"{Name}:${price}")

print(f"This is the Price of the top 7 Cryptocurrency : {Breakdown}")

