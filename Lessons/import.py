#Путь к сайту http://www.combook.ru/catalog/32/
import requests
from bs4 import BeautifulSoup
import re
import os

# URL = input('Введите URL, который хотите спарсить: \n')
URL = 'http://www.combook.ru/catalog/32/'
# name_folder = input('Введите название папки: \n')
name_folder = '32'
try:
    os.mkdir(name_folder)
except IsADirectoryError:
    pass
page = requests.get(URL.strip())

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

results = soup.find_all('img', src = re.compile('\/\w+\/\d+\/\w+\.jpg'))
print(results)

print(type(results))
print(len(results))

# for i in range(len(results)):
#     link = results[i]['src']
#     print(link)
#     img_data = requests.get('http://www.combook.ru/'+link)
#     with open(name_folder+ '/'+str(i) + '.jpg', 'wb') as handler:
#         handler.write(img_data.content)