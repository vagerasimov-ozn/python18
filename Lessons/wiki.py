import requests
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = requests.get(articleUrl)
    bs = BeautifulSoup(html.content,'html.parser')
    return bs.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('https://en.wikipedia.org/wiki/Ozone.ru')
print(len(links))
while len(links)>0:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    newArticle = 'https://en.wikipedia.org/'+ newArticle
    print(newArticle)
    print('https://en.wikipedia.org/'+ newArticle)
    links = getLinks(newArticle)
    print(links)