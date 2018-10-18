from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


# Get HTML site and store it at 'data'
# filename='D:\_gfot\PyCharmProjects\web_scraping\intro-to-soup-html.html'
# data = read_file(filename)

# url = 'http://www.euroleague.net/competition/players/showplayer?pcode=JUO&seasoncode=E2018'
# url = 'https://gr.linkedin.com/in/georgios-fotiadis-5a48035'
url = 'http://www.google.com'
ua = UserAgent()
header = {'user-agent':ua.chrome}
response = requests.get(url, headers=header)
data = response.content


# Parse HTML site
soup = BeautifulSoup(data, 'lxml')
# print(soup.prettify())
meta = soup.meta
print(meta)


# tags = soup.find_all('a')
# print(tags)
# for tag in tags:
#     print(tag)
#     print(tag.get('href'))
