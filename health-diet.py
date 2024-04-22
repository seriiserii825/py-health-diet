#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

index_file = "src/index.html"

def getIndexFile():
    url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
    }
    req = requests.get(url, headers=headers)
    with open(index_file, "w") as file:
        file.write(req.text)

def readIndexFile():
    with open(index_file, "r") as file:
        content = file.read()
    soup = BeautifulSoup(content, "lxml")
    all_products_href = soup.find_all("a", class_="mzr-tc-group-item-href")
    for link in all_products_href:
        print(link)


if __name__ == "__main__":
    print("File downloaded successfully")
    readIndexFile()
