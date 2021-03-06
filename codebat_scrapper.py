from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def get_url_data(url, ua, header):
    response = requests.get(url, headers=header)
    data = response.content
    return BeautifulSoup(data, 'lxml')


def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


########################################################################################
# Get HTML site and store it at 'data'

# filename=''
# data = read_file(filename)

base_url = 'https://codingbat.com'
ua = UserAgent()
header = {'user-agent':ua.chrome}
soup = get_url_data(base_url+'/python', ua, header)
# print('-------------------------\n',soup.prettify(),'\n-------------------------')

fd = open('codebat_data.txt', 'w', encoding="utf-8")
fd.write('Scrapping https://codingbat.com/python\n\n')

# Get names and category URLs (urls = category URLs)
all_divs = soup.find_all('div', attrs={'class': 'summ'})
urls = {}
for div in all_divs:
    urls[div.a.string] = base_url+div.a['href']
print(urls)

# Get names and question URLs (urls_2 = question URLs)
for key, url in urls.items():
    print('\n'+url)
    fd.write('\n\n\n--------------------------------------------\n')
    fd.write('-> '+key)
    inner_soup = get_url_data(url, ua, header)
    div = inner_soup.find('div',attrs={'class':'tabc'})
    urls_2 = {}
    for td in div.table.find_all('td'):
        urls_2[td.a.string] = base_url+td.a['href']
    print(urls_2)

    # Get question info
    for key_2, url_2 in urls_2.items():
        try:
            print('\n' + url_2)
            fd.write('\n\n---> ' + key_2)
            inner_soup_2 = get_url_data(url_2, ua, header)
            div_2 = inner_soup_2.find('div',attrs={'class':'indent'})
            problem_statement = div_2.table.div.string
            print(problem_statement)
            fd.write('\n' + problem_statement)

            statement_siblings = div_2.table.div.next_siblings
            examples = [sibling.string for sibling in statement_siblings if sibling.string is not None]
            print(examples)
            for my_example in examples:
                fd.write('\n'+my_example.string)
                print(my_example.string)
        except:
            pass


fd.close()
