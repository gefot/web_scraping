from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

def read_file(filename):
    with open(filename,'r') as f:
        data = f.read()
    return data

# filename='D:\_gfot\PyCharmProjects\web_scraping\intro-to-soup-html.html'
#
# my_data = read_file(filename)
# soup = BeautifulSoup(my_data,'lxml')
# print(soup)


url = 'http://www.euroleague.net/competition/players/showplayer?pcode=JUO&seasoncode=E2018'
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'lxml')
# soup = BeautifulSoup(data, 'html.parser')
print(soup)
# tags = soup.find_all('a')
# print(tags)
# for tag in tags:
#     print(tag)
#     print(tag.get('href'))
