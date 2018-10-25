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
                # print(a_tag.string)
                full_url = 'http://www.euroleague.net' + url
                url_list.append(full_url)
        except:
            pass

    return url_list


def get_player_stats(soup):

    stats = []
    tr_tags = soup.find_all('tr')
    for tr_tag in tr_tags:
        print('\n\n\n\n\n')
        for td_tag in tr_tag:
            print(type(td_tag),' :',td_tag)
            # try:
            #     if td_tag.get('class') == 'PlayerGameNumberContainer':
            #         print('LALALALALA')
            # except:
            #     pass

        # print('\n\n')
        # print(tr_tag)

    return stats



########################################################################################
### Contant Variables
ua = UserAgent()
header = {'user-agent':ua.chrome}

# soup = get_url_data('http://www.euroleague.net/competition/teams/showteam?clubcode=OLY&seasoncode=E2018',ua,header)
# # print('-------------------------\n',soup.prettify(),'\n-------------------------')
# url_list = get_player_list(soup)
# print(url_list[0])


url_list = ['http://www.euroleague.net/competition/players/showplayer?pcode=007982&seasoncode=E2018']
soup = get_url_data(url_list[0],ua,header)
#print(soup.prettify())
player_stats = get_player_stats(soup)
print(player_stats)


