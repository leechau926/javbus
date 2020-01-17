from bs4 import BeautifulSoup
import re
import time
import  cloudscraper

proxies = {
    'http': 'socks5://192.168.131.1:10808',
    'https': 'socks5://192.168.131.1:10808'
}

scraper = cloudscraper.create_scraper()
scrape_url = 'https://www.javlibrary.com/cn/?v=javli6tcsy'
web_data = scraper.get(scrape_url, proxies=proxies).content.decode('utf-8')
soup = BeautifulSoup(web_data, 'lxml')
# print(web_data)
img_src = soup.find(name='img', attrs={'id':'video_jacket_img'})
img_url = 'https:' + img_src['src']
print(img_url)
img_title = soup.find('title').text
print(img_title)
img_name = re.findall('^(.+?)\s', img_title)
print(img_name[0] + '.jpg')





