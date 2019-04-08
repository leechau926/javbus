import requests
import re
import random

url = "https://www.torrentkitty.tv/search/"
#keyword = input("Please input keyword: ")
my_headers = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"	
]
randdom_header=random.choice(my_headers)
headers = {'User-agent': randdom_header}
pattern = re.compile('<td class="name">(.*?)</td>.*?<td class="date">(.*?)</td>.*?Detail</a><a\shref="(.*?)"\stitle', re.S)

def max_page(response_text):
    page_pattern = re.compile('<a\shref="\d{1,3}">(\d{1,3})</a><a\shref="2"', re.S)
    pages = re.findall(page_pattern, response_text)
    max_page = int(pages[0])
    return max_page

def main():
    keyword = input("Please input keyword: ")
    print('========%s========' % keyword)
    maxpage = max_page(requests.get(url+keyword, headers=headers).text)
    print('max page is ', maxpage)
    for num in range(1,maxpage+1):
        response = requests.get(url+keyword+"/"+str(num), headers=headers)
        items = re.findall(pattern, response.text)
        for item in items:
            with open('output.txt', 'a', encoding='utf-8') as op:
                op.write("%s,%s,%s\n" % (item[0], item[1], item[2][0:60]))
        print('page %d saved!' % num)

if __name__ == '__main__':
    main()
