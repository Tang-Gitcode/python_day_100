import requests
from bs4 import BeautifulSoup

url = 'https://cdn-v3.honghusaas.com/driver/static-res/1012/ag/2022-11-02/093cab1c325519e4fa45002cd5ea95dc.html'
header = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) \
                   Chrome/106.0.0.0 Mobile Safari/537.36 '
}
res = requests.get(url=url, headers=header).content.decode('utf-8')

soup = BeautifulSoup(res, 'lxml')
# print(soup)
soup_div = soup.find_all('div')
soup_text = soup.div.get_text()
# print(soup_text)
soup_text_count = soup_text.count('麦田来了')
print(f'包含关键词“麦田来了”的个数:{soup_text_count}\n')
soup_text_list = soup_text.split('\n')
for i in soup_text_list:
    if '麦田来了' in i:
        print(i)


