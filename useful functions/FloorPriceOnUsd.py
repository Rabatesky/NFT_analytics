import requests

def FloorPriceOnUsd(collection_slug):
    #example
    #collection_slug = 'gs-on-ape'
    #При использовании функции, желательно иметь результат исполения функции fetchTop1000Cryptos в какой-то переменной
    #у меня это current_price = fetchTop1000Cryptos()
    url = f"https://api.opensea.io/api/v2/collections/{collection_slug}/stats"
    headers = {
        "accept": "*/*",
        "x-api-key": OPENSEA_KEY,
    }
    r = requests.get(url, headers=headers)
    if r.status_code == 200 and r.json()["total"]["floor_price_symbol"] != '':
        flor_price_nativ = float(r.json()["total"]["floor_price"])
        native_symbol = r.json()["total"]["floor_price_symbol"].lower()
        price_nativ = current_price[native_symbol]
        return round(flor_price_nativ*float(price_nativ),2)
    else:
        return 0