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

base_url = 'https://codingbat.com'
ua = UserAgent()
header = {'user-agent':ua.chrome}
soup = get_url_data(base_url+'/python',ua,header)
# print('-------------------------\n',soup.prettify(),'\n-------------------------')


# Get names and category URLs (urls = category URLs)
all_divs = soup.find_all('div',attrs={'class':'summ'})
urls = {}
for div in all_divs:
    urls[div.a.string] = base_url+div.a['href']
print(urls)

# Get names and question URLs (urls_2 = question URLs)
for url in urls.values():
    print('\n'+url)
    inner_soup = get_url_data(url, ua, header)
    div = inner_soup.find('div',attrs={'class':'tabc'})
    urls_2 = {}
    for td in div.table.find_all('td'):
        urls_2[td.a.string] = base_url+td.a['href']
    print(urls_2)

    # Get question info
    for url_2 in urls_2.values():
        print('\n' + url_2)
        inner_soup_2 = get_url_data(url_2, ua, header)
        div = inner_soup_2.find('div',attrs={'class':'minh'})
        print(div)
        # for td in div.table.find_all('p'):
        #     print(td)
        break

    break


