import requests
import json
import time
import csv

main = input()
headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://www.wildberries.ru',
    'Referer': 'https://www.wildberries.ru/catalog/0/search.aspx?&sort=popular&search=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BA%D0%B0%D1%80%D1%82%D0%B0+%D0%B4%D0%BB%D1%8F+%D0%BF%D0%BA',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-queryid': 'qid742923569170344125120240328162539',
}
ID_LIST = []
GRADE_LIST = []
PRICE_LIST = []
NAME_LIST = []
RESULT = []
x = 0
for i in range(1):
    x += 1
    params = {
        'ab_testing': 'false',
        'appType': '1',
        'curr': 'rub',
        'dest': '-1257786',
        'page': f'{x}',
        'query': f'{main}',
        'resultset': 'catalog',
        'sort': 'popular',
        'spp': '30',
        'suppressSpellcheck': 'false',
    }

    response = requests.get('https://search.wb.ru/exactmatch/ru/common/v5/search', params=params, headers=headers).json()

    time.sleep(0.5)

    name = response['data']['products']
    for i in name:
        NAME_LIST.append(i['name'])

    pric = response['data']['products']
    for i_2 in pric:
        sizes = i_2['sizes']
        for i_3 in sizes:
            price = i_3['price']['product'] / 100
            PRICE_LIST.append(f'{price}₽')

    grade = response['data']['products']
    for i_01 in grade:
        GRADE_LIST.append(i_01['reviewRating'])

    id = response['data']['products']
    for i_02 in id:
        ID_LIST.append(i_02['id'])

for name,price,assessments, id in zip(NAME_LIST,PRICE_LIST,GRADE_LIST, ID_LIST):
    RESULT.append({
        'название':name,
        'цена': price,
        'оценка': assessments,
        'артикул': id
    })

with open('i.json', 'w', encoding='utf8') as file:
    json.dump(RESULT, file, indent=4, ensure_ascii=False)