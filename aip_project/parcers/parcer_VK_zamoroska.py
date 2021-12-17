import requests
from bs4 import BeautifulSoup as BS
import sqlite3

num_of_page = 20
url = 'https://vkusvill.ru/goods/zamorozhennye-produkty/?PAGEN_1='
base_url = 'https://vkusvill.ru'

for i in range(1, num_of_page + 1):
    response = requests.get(url + str(i))
    html = response.text
    soup = BS(html, 'html.parser')

    container = soup.select_one('div.ProductCards__list')
    products = container.select('div.ProductCards__item')

    urls = []
    for product in products:
        link = product.select_one('div.ProductCard__content a')['href']
        urls.append(base_url + link)

    args = []
    for link in urls:
        response = requests.get(link)
        html = response.text
        soup = BS(html, 'html.parser')
        shop = 'ВкусВилл'
        category = 'Замороженные продукты'
        name = soup.select_one('h1').text
        energy = soup.select_one('div.DetailsList__value')
        if energy is None:
            pass
        else:
            energy = soup.select_one('div.DetailsList__value').text
            args.append((shop, category, name.replace('\xa0', ' '), energy))
            for ar in args:
                print(ar)

        db = sqlite3.connect("project.db")

        cursor = db.cursor()

        cursor.executemany("""INSERT OR IGNORE INTO products VALUES (?,?,?,?)""", args)
        db.commit()
        db.close()