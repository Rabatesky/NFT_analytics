import requests

def get_max_offer(collection_slug: str, api_key: str):
    url = f"https://api.opensea.io/api/v2/offers/collection/{collection_slug}"
    headers = {
        "Accept": "application/json",
        "X-API-KEY": api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Ошибка запроса:", response.text)
        return None

    data = response.json()
    data = data["offers"]
    if not data:
        print("По коллекции нет офферов")
        return None

    price_offers = []
    for item in data:
        price_offer = float(item["price"]["value"])/int(item["protocol_data"]["parameters"]["consideration"][0]["startAmount"])/10 ** int(item["price"]["decimals"])
        price_offers.append(price_offer)

    return max(price_offers)