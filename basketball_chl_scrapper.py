from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import re

def get_url_data(url, ua, header):
    '''
    Returns Beautiful Soup of the requested URL
    '''
    response = requests.get(url, headers=header)
    data = response.content

    return BeautifulSoup(data, 'lxml')




########################################################################################
### Constant Variables
ua = UserAgent()
header = {'user-agent': ua.chrome}
global base_url
base_url = 'http://www.championsleague.basketball'

fd = open('basketball_chl_data.txt', 'w', encoding="utf-8")
fd.write('Scrapping http://www.championsleague.basketball/18-19/team/PAOK\n\n')


# Get teams names and URLs
soup = get_url_data(base_url+'/18-19/', ua, header)
# print('----------\n', soup.prettify(), '\n----------')
# teams_ul = soup.find('ul', attrs={'class': 'nav-teams nav-teams-16'})
# teams = {li.a['title']: (base_url + li.a['href']) for li in teams_ul.find_all('li') if li['class'][0] == 'item'}

teams = {'PAOK': 'http://www.championsleague.basketball/18-19/team/PAOK#|tab=roster'}
print(teams)

# Get player names and URLs for each team
for team, url in teams.items():
    print(team)
    fd.write('\n\n\n--------------------------------------------')
    fd.write('\n---> ' + team)
    fd.write('\n' + url + '\n')

    soup_2 = get_url_data(url, ua, header)
    # print('----------\n', soup_2.prettify(), '\n----------')
    # player_list = get_player_list(soup_2)
    # print(player_list)

    '''
    for player, player_url in player_list.items():
        try:
            fd.write('\n-> ' + player)
            fd.write('\n' + player_url)
            print(player, ' ', player_url)

            soup_3 = get_url_data(player_url, ua, header)
            player_stats = get_player_stats(soup_3)
            for player_stat in player_stats:
                fd.write('\n' + '\t'.join(player_stat))
        except:
            pass

'''
fd.close()
