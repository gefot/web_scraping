from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from selenium import webdriver
from time import sleep


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

# filename=''
# data = read_file(filename)

base_url = 'https://codingbat.com'
ua = UserAgent()
header = {'user-agent':ua.chrome}
soup = get_url_data(base_url+'/python',ua,header)
# print('-------------------------\n',soup.prettify(),'\n-------------------------')

# fd = open('instagram_data.txt','w',encoding="utf-8")
# fd.write('Scrapping https://www.instagram.com\n\n')

driver = webdriver.Chrome('D:\_gfot\chromedriver')
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
soup = BeautifulSoup(driver.page_source,'lxml')
# print(soup.prettify())

signup_button = driver.find_element_by_xpath("//span[@id='react-root']//p[@class='izU2O']/a")
signup_button.click()


## Login to Instagram account
# username_textbox = driver.find_element_by_name('username')
# username_textbox.send_keys('fotgio@hotmail.com')
# password_textbox = driver.find_element_by_name('password')
# password_textbox.send_keys('xxxxx')
# username_textbox.submit()
sleep(5)

# # Get names and category URLs (urls = category URLs)
# all_divs = soup.find_all('div',attrs={'class':'summ'})
# urls = {}
# for div in all_divs:
#     urls[div.a.string] = base_url+div.a['href']
# print(urls)
#
# # Get names and question URLs (urls_2 = question URLs)
# for key,url in urls.items():
#     print('\n'+url)
#     # fd.write('\n\n\n--------------------------------------------\n')
#     # fd.write('-> '+key)
#     inner_soup = get_url_data(url, ua, header)
#     div = inner_soup.find('div',attrs={'class':'tabc'})
#     urls_2 = {}
#     for td in div.table.find_all('td'):
#         urls_2[td.a.string] = base_url+td.a['href']
#     print(urls_2)
#
#     # Get question info
#     for key_2,url_2 in urls_2.items():
#         try:
#             print('\n' + url_2)
#             # fd.write('\n\n---> ' + key_2)
#             inner_soup_2 = get_url_data(url_2, ua, header)
#             div_2 = inner_soup_2.find('div',attrs={'class':'indent'})
#             problem_statement = div_2.table.div.string
#             print(problem_statement)
#             # fd.write('\n' + problem_statement)
#
#             statement_siblings = div_2.table.div.next_siblings
#             examples = [sibling.string for sibling in statement_siblings if sibling.string is not None]
#             print(examples)
#             for my_example in examples:
#                 # fd.write('\n'+my_example.string)
#                 print(my_example.string)
#             break
#         except:
#             pass
#
#     break

# fd.close()
driver.close()
