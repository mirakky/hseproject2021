import requests
from bs4 import BeautifulSoup as BS
import sqlite3

num_of_page = 2
url = 'https://vkusvill.ru/tort/?PAGEN_1='
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
        category = 'Торты на заказ'
        name = soup.select_one('h1').text
        calories = soup.find_all('li', 'DetailsList__item')

        if calories is None:
            calories_4 = 'Данных нет'
        else:
            args.append([shop, category, name.replace('\xa0', ' '), []])
            for el in calories:
                calories_2 = el.select_one('div.DetailsList__value').text
                calories_3 = el.select_one('div.DetailsList__text').text
                calories_4 = (calories_2 + ' ' + calories_3).replace('\xa0', ' ')
                args[-1][-1].append(calories_4)
            args[-1][-1] = ", ".join(args[-1][-1])
            print(args[-1])

        db = sqlite3.connect("project.db")

        cursor = db.cursor()

        cursor.executemany("""INSERT OR IGNORE INTO products VALUES (?,?,?,?)""", args)
        db.commit()
        db.close()