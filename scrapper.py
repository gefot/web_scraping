from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import re

def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


## Get HTML site and store it at 'data'
filename='D:\_gfot\PyCharmProjects\web_scraping\\three-sisters.html'
data = read_file(filename)

# url = 'http://www.euroleague.net/competition/players/showplayer?pcode=JUO&seasoncode=E2018'
# # url = 'https://gr.linkedin.com/in/georgios-fotiadis-5a48035'
# # url = 'http://www.google.com'
# ua = UserAgent()
# header = {'user-agent':ua.chrome}
# response = requests.get(url, headers=header)
# data = response.content

## Parse HTML site
soup = BeautifulSoup(data, 'lxml')
print('-------------------------\n',soup.prettify(),'\n-------------------------')

regex = re.compile('^b$')
for tag in soup.find_all(regex):
    print(tag.string)
# print(soup.find_all(regex))

#
# head = soup.head
# title = soup.title
# meta = soup.meta
# # print(meta['charset'])
#
# body = soup.body
# print(body.contents)
# print('==========================\n')


# print(title.parent)
# p = body.p
# print("1 = ",p)
# for i,pp in enumerate(p.next_siblings):
#     print("1.",i,pp.name if pp != '\n' else 'empty sibling')
# children = [child for child in body.contents if child is not None]
# print(len(children))

# for index,child in enumerate(body.descendants):
#     print('\n---> id = ',index)
#     print(child if child != '\n' else '\\n')

# for child in body.contents:
#     print(child if child is not None else '',end='\n=====\n')
#
# for child in body.children:
#     print(child if child is not None else '',end='\n=====\n')


