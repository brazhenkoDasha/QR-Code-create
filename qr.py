import os
import requests
from urllib.parse import quote

SAVE_DIRS = {
    "class8": "/home/darya/Documents/qr/qr_codes_class8/519",
    "class9": "/home/darya/Documents/qr/qr_codes_class9/519",
    "class7": "/home/darya/Documents/qr/qr_codes_class7/519",
    "class10": "/home/darya/Documents/qr/qr_codes_class10/519",
    "class11": "/home/darya/Documents/qr/qr_codes_class11/519"
}

for path in SAVE_DIRS.values():
    os.makedirs(path, exist_ok=True)

codes = []

for i in range(1, 20):
    if i < 10:
        codes.append(("W0" + str(i), "class7"))
    else:
        codes.append(("W" + str(i), "class7"))

for i in range(1, 25):
    if i < 10:
        codes.append(("W80" + str(i), "class8"))
    else:
        codes.append(("W8" + str(i), "class8"))

for i in range(1, 30):
    if i < 10:
        codes.append(("W90" + str(i), "class9"))
    else:
        codes.append(("W9" + str(i), "class9"))

for i in range(1, 29):
    if i < 10:
        codes.append(("W100" + str(i), "class10"))
    else:
        codes.append(("W10" + str(i), "class10"))

for i in range(1, 22):
    if i < 10:
        codes.append(("W110" + str(i), "class11"))
    else:
        codes.append(("W11" + str(i), "class11"))


BASE_URL = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data="

for code, class_key in codes:
    url = BASE_URL + quote(code)
    response = requests.get(url)
    if response.status_code == 200:
        save_path = os.path.join(SAVE_DIRS[class_key], f"{code}.png")
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"Сохранен: {code}.png в {SAVE_DIRS[class_key]}")
    else:
        print(f"Ошибка при загрузке {code}")

