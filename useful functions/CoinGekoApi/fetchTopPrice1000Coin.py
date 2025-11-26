import requests
#функция возвращает словать из 1000 первых криптовалют по капитализации, что бы получить цену конкретной, нужно обратиться по символу монеты, напримем по ['ape']
def fetchTop1000Cryptos(vs_currency="usd"):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    all_tokens = []

    for page in range(1, 5):
        params = {
            "vs_currency": vs_currency,
            "order": "market_cap_desc",
            "per_page": 250,
            "page": page
        }
        headers = {
            "x-cg-api-key": COIN_GEKO_KEY
        }

        resp = requests.get(url, params=params, headers=headers)

        data = resp.json()
        if isinstance(data, list):
            all_tokens.extend(data)
        else:
            print(f"Unexpected response on page {page}: {data}")

    return {item["symbol"].lower(): item["current_price"] for item in all_tokens}
