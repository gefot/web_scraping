from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import re


def get_url_data(url,ua,header):
    '''
    Returns Beautiful Soup of the requested URL
    '''
    response = requests.get(url, headers=header)
    data = response.content
    return BeautifulSoup(data, 'lxml')


def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


########################################################################################
## Get HTML site and store it at 'data'

# filename='D:\_gfot\PyCharmProjects\web_scraping\\consumer-reports.txt'
# data = read_file(filename)

ua = UserAgent()
header = {'user-agent':ua.chrome}
soup = get_url_data('https://codingbat.com/python',ua,header)

# print('-------------------------\n',soup.prettify(),'\n-------------------------')
base_url = 'https://codingbat.com'

all_divs = soup.find_all('div',attrs={'class':'summ'})
level1_urls = {}
for div in all_divs:
    level1_urls[div.a.string] = base_url+div.a['href']

print(level1_urls)

for url in level1_urls.values():
    print('\n'+url)
    inner_soup = get_url_data(url, ua, header)
    # print('-------------------------\n', soup.prettify(), '\n-------------------------')
    div = inner_soup.find('div',attrs={'class':'tabc'})
    for td in div.table.find_all('td'):
        print(td)

    break


