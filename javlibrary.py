# get bestrated
from bs4 import BeautifulSoup
import re
import time

file = open('bestrated.html', 'r', encoding='utf-8')

soup = BeautifulSoup(file.read(), 'lxml')

t_title = soup.find('title').text
print(t_title)

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

pattern = re.compile('vid_javli')
t_list = soup.find_all(name='div', attrs={'id':pattern})
# print(t_list)
for item in t_list:
	name = item.a['title']
	address = item.a['href'].replace('.', '')
	link = 'http://www.javlibrary.com/cn' + address
	print('name: ' + name)
	print('link: ' + link)
	print('******************************')
