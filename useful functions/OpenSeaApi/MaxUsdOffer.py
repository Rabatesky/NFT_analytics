import requests

# При использовании функции, желательно иметь результат исполения функции fetchTop1000Cryptos в какой-то переменной
# у меня это current_price = fetchTop1000Cryptos()
# Текущая функци работает неккоректно т.к. иногда API OpenSea возвращает некорректную ценну в Gwei писал в поддержку, пока молчат
def MaxUsdOffer(collection_slug,id):
    url = f"https://api.opensea.io/api/v2/offers/collection/{collection_slug}/nfts/{id}/best"
    headers = {
        "accept": "*/*",
        "x-api-key": OPENSEA_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        end_price = (round(int(response.json()["price"]["value"])*current_price[response.json()["price"]["currency"][1:].lower()]/1000000000000000000,5))
    else:
#Если на всей коллекции нет не единого офера или мы упали по какой-то другой причине(обработку ошибок нужно делать массово), возвращается 0
        end_price = 0
    return end_price