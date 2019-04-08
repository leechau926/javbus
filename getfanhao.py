import re
import requests
import shutil
from requests.packages.urllib3.exceptions import InsecureRequestWarning

url = "https://www.javbus.pw/"
pattern = re.compile("img\s=\s'(.*?)';", re.S)
headers = {'User-agent': 'Mozilla/5.0'}
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def getlist(filename):
    with open(filename, 'r') as q:
        namelist = []
        for line in q.readlines():
            line = line.strip("\n")
            namelist.append(line)
    return namelist

def getfanhao(fanhao):
    response = requests.get(url+fanhao, headers=headers, verify=False)
    item = re.findall(pattern, response.text)
    return item[0]

def down(link, filename):
    r = requests.get(link, stream=True, headers=headers)
    with open(filename, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
        print("%s saved!" % filename)

def main():
    for name in getlist("ssni.txt"):
        fanhao = name[0:8]
        link = getfanhao(fanhao)
        down(link, "%s.jpg"%name)

if __name__ == '__main__':
    main()
