import requests
#Функция возвращает json с указанием floor цены в нативном токене и в долларе, а как же показывает на каком маркетплейсе такая цена
def get_floor(contract_address,chain):
    url = f"https://deep-index.moralis.io/api/v2.2/nft/{contract_address}/floor-price"
    headers = {
        "X-API-Key": MORALIS_KEY,
        "accept": "application/json"
    }
    params = {
        "chain": chain
    }
    
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200:
        data = resp.json()
    else:
        print("Error:", resp.status_code, resp.text)
    return data