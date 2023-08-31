import requests
from bs4 import BeautifulSoup
import time

url = ('https://cars.av.by/filter?transmission_type=1&sort=4')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

items = soup.find_all('div', class_="listing-item")
item = soup.find_all("div", class_="listing-item__params")

name = []
price = []
years = []
all = {}

while True:
    for n, i in enumerate(items, start=1):
        name_car = i.find("span", class_="link-text").text.replace('\n', '')
        name.append(name_car)

    for n, i in enumerate(items, start=1):
        value = i.find("div", class_="listing-item__price").text
        value1 = value.split("\u2009")
        value2 = value1[1].split('\xa0р.')
        total = value1[0] + value2[0]
        price.append(total)

    for n, i in enumerate(item, start=1):
        year = i.find("div").text.split('\xa0г')
        years.append(year[0])

    count = 0

    for i in name:
        piece = []
        piece.append(price[count])
        piece.append(years[count])
        all[i] = piece
        count += 1

    print(all)

    time.sleep(300)