from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import re

def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


## Get HTML site and store it at 'data'
filename='D:\_gfot\PyCharmProjects\web_scraping\\consumer-reports.txt'
data = read_file(filename)

# # url = 'http://www.euroleague.net/competition/players/showplayer?pcode=JUO&seasoncode=E2018'
# # url = 'https://gr.linkedin.com/in/georgios-fotiadis-5a48035'
# # url = 'http://www.google.com'
# url = 'https://www.consumerreports.org/cro/a-to-z-index/products/index.htm'
# ua = UserAgent()
# header = {'user-agent':ua.chrome}
# response = requests.get(url, headers=header)
# data = response.content

## Parse HTML site
soup = BeautifulSoup(data, 'lxml')
# print('-------------------------\n',soup.prettify(),'\n-------------------------')


all_divs = soup.find_all('div',attrs={'class':'entry-letter'})
print(all_divs)
products = {div.div.a.span.string.strip():div.div.a['href'] for div in all_divs}
# for div in all_divs:
#     products[div.div.a.span.string.strip()] = div.div.a['href']

print(products)
# products = [div.div.a.span.string.strip() for div in all_divs]
# all_divs =
# # products = [re.sub('^ ','',prod) for prod in products]
# print(products)