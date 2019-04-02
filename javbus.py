import re
import requests
import shutil

fanhao_list = {"SSNI-338", "SSNI-295", "SSNI-315", "SSNI-179", "SSNI-272", "SSNI-402"}
headers = {'User-agent': 'Mozilla/5.0'}

def get(fanhao):
        url = "https://www.javbus.pw/%s" % fanhao
        response = requests.get(url)
        pattern = re.compile("img\s=\s'(.*?)';", re.S)
        item = re.findall(pattern,response.text)
        return item[0]

def main():
        for fanhao in fanhao_list:
                try:                
                        filename = "%s.jpg"%fanhao
                        r = requests.get(get(fanhao), stream=True, headers=headers)
                        with open(filename, 'wb') as f:
                                r.raw.decode_content = True
                                shutil.copyfileobj(r.raw, f)
                except IndexError:
                        continue

if __name__ == '__main__':
        main()
