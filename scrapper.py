from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent':ua.chrome}

url = "http://www.google.com"
url_response = requests.get(url,headers=header)
print(url_response.status_code)
print(url_response.text,'\n\n\n')
#print(url_response.headers)

for key,value in url_response.headers.items():
    print(key, ' --> ',value)
#data = url_response.text
#data_tagged = BeautifulSoup(data,'html.parser')
#data_list = data_tagged.find_all()
#for tag in data_tagged:
#    print(tag)

'''
url = "http://cisco.com/"
response = requests.get(url)
data = response.text
#print(data)
soup = BeautifulSoup(data, 'html.parser')
#print(soup)
tags = soup.find_all('a')
#print(tags)
for tag in tags:
    print(tag)
#    print(tag.get('href'))
'''
