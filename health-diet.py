#!/usr/bin/python3
import requests

index_file = "index.html"

def getIndexFile():
    url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
    }
    req = requests.get(url, headers=headers)
    with open(index_file, "w") as file:
        file.write(req.text)

# getIndexFile()

