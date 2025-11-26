import requests
import json
import os
from time import sleep
#функция выгружает всю метадату и все png из хранилища ipfs в указанную вами папк
#внутри папки будет создано две внутринние папки images и metadata 
def get_collection_ipfs(BASE_URI,START_TOKEN_ID,END_TOKEN_ID,SAVE_FOLDER="collection"):

    os.makedirs(SAVE_FOLDER, exist_ok=True)
    os.makedirs(os.path.join(SAVE_FOLDER, "images"), exist_ok=True)
    os.makedirs(os.path.join(SAVE_FOLDER, "metadata"), exist_ok=True)
    # Преобразование ipfs:// в https
    def ipfs_to_http(url):
        if url.startswith("ipfs://"):
            return url.replace("ipfs://", "https://ipfs.io/ipfs/")
        return url

    for token_id in range(START_TOKEN_ID, END_TOKEN_ID + 1):
        try:
            token_url = ipfs_to_http(f"{BASE_URI}{token_id}")
            r = requests.get(token_url)
            if r.status_code != 200:
                print(f"[{token_id}] JSON не найден: {token_url}")
                continue
    
            data = r.json()
            #Получаем метадату
            with open(os.path.join(SAVE_FOLDER, "metadata", f"{token_id}.json"), "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            #Получаем png
            image_url = ipfs_to_http(data.get("image", ""))
            if image_url:
                img_data = requests.get(image_url).content
                img_name = f"{os.path.basename(image_url)}"
                with open(os.path.join(SAVE_FOLDER, "images", img_name), "wb") as f:
                    f.write(img_data)
    
            print(f"[{token_id}] Успешно скачано")
    
        except Exception as e:
            print(f"[{token_id}] Ошибка: {e}")