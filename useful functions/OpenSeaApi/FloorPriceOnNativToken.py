import requests

def get_floor_price(collection_slug: str, api_key: str):
    url = f"https://api.opensea.io/api/v2/collections/{collection_slug}/stats"
    headers = {
        "Accept": "application/json",
        "X-API-KEY": api_key
    }
    response = requests.get(url, headers=headers)
    # Проверяем, успешно ли
    if response.status_code != 200:
        print("Ошибка запроса:", response.text)
        return None
    data = response.json()
    stats = float(data["total"]["floor_price"])

    if not stats:
        print("По коллекции нет листингов")
        return None

    return stats
