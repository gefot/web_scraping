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

def get_player_list(soup):
    regex = re.compile('competition/players/showplayer\?pcode=')
    a_tags = soup.find_all('a', href=True)

    url_list = []
    for a_tag in a_tags:
        try:
            # print('\n\n\n',a_tag)
            url = a_tag.get('href')
            if regex.search(url) and a_tag.get('id') == None and a_tag.string != None:
                print(a_tag.string)
                full_url = 'www.euroleague.net' + url
                print(full_url)
                url_list.append(full_url)
                print('')
        except:
            pass

    return url_list

########################################################################################
### Contant Variables
ua = UserAgent()
header = {'user-agent':ua.chrome}

### Get names and URLs for players of specific team
soup = get_url_data('http://www.euroleague.net/competition/teams/showteam?clubcode=OLY&seasoncode=E2018',ua,header)
# print('-------------------------\n',soup.prettify(),'\n-------------------------')

url_list = get_player_list(soup)
print(url_list)



