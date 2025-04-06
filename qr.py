import os
import requests
from urllib.parse import quote

SAVE_DIR = "/path/to/dir"
os.makedirs(SAVE_DIR, exist_ok=True)

#папка со значениями куаров
codes = []

for i in range(1, 10):
    if i < 10:
        codes.append("F90" + str(i))
    else:
        codes.append("F9" + str(i))

BASE_URL = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data="

for code in codes:
    url = BASE_URL + quote(code)
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(SAVE_DIR, f"{code}.png"), "wb") as file:
            file.write(response.content)
        print(f"Сохранен: {code}.png")
    else:
        print(f"Ошибка при загрузке {code}")

