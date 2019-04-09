import re
import requests
import shutil
import random

my_headers = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"  
]
randdom_header=random.choice(my_headers)
headers = {'User-agent': randdom_header}

def get(fanhao):
    url = "https://www.javbus.pw/%s" % fanhao
    response = requests.get(url, headers=headers)
    pattern = re.compile("img\s=\s'(.*?)';", re.S)
    item = re.findall(pattern, response.text)
    return item[0]

def main():
    fanhao = input("Please type fanhao: ")
    try: 
        filename = "%s.jpg" % fanhao
        r = requests.get(get(fanhao), stream=True, headers=headers)
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        print("%s.jpg saved!" % fanhao)
    except IndexError:
        print("%s does not exist!" % fanhao)

if __name__ == '__main__':
    main()
