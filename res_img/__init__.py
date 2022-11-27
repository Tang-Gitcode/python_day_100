import requests
import os
import re
from init_proxy import Proxy

# def get_images_from_baidu(keyword, page_num, save_dir):
#     header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                             'Chrome/78.0.3904.108 Safari/537.36'}
#     # 请求的 url
#     url = 'https://image.baidu.com/search/acjson?'
#     n = 0
#     for pn in range(0, 30 * page_num, 30):
#         # 请求参数
#         param = {'tn': 'resultjson_com',
#                  # 'logid': '7603311155072595725',
#                  'ipn': 'rj',
#                  'ct': 201326592,
#                  'is': '',
#                  'fp': 'result',
#                  'queryWord': keyword,
#                  'cl': 2,
#                  'lm': -1,
#                  'ie': 'utf-8',
#                  'oe': 'utf-8',
#                  'adpicid': '',
#                  'st': -1,
#                  'z': '',
#                  'ic': '',
#                  'hd': '',
#                  'latest': '',
#                  'copyright': '',
#                  'word': keyword,
#                  's': '',
#                  'se': '',
#                  'tab': '',
#                  'width': '',
#                  'height': '',
#                  'face': 0,
#                  'istype': 2,
#                  'qc': '',
#                  'nc': '1',
#                  'fr': '',
#                  'expermode': '',
#                  'force': '',
#                  'cg': '',    # 这个参数没公开，但是不可少
#                  'pn': pn,    # 显示：30-60-90
#                  'rn': '30',  # 每页显示 30 条
#                  'gsm': '1e',
#                  '1618827096642': ''
#                  }
#         request = requests.get(url=url, headers=header, params=param)
#         if request.status_code == 200:
#             print('Request success.')
#         request.encoding = 'utf-8'
#         # 正则方式提取图片链接
#         html = request.text
#         image_url_list = re.findall('"thumbURL":"(.*?)",', html, re.S)
#         print(image_url_list)
#
#         if not os.path.exists(save_dir):
#             os.makedirs(save_dir)
#
#         for image_url in image_url_list:
#             image_data = requests.get(url=image_url, headers=header).content
#             with open(os.path.join(save_dir, f'{n:06d}.jpg'), 'wb') as fp:
#                 fp.write(image_data)
#             n = n + 1
#             fp.close()
#
#
# if __name__ == '__main__':
#     keyword = '商品图'
#     save_dir = keyword
#     page_num = 2
#     get_images_from_baidu(keyword, page_num, save_dir)
#     print('爬取完成')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36 '
}
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10846172375391154848&ipn=rj&ct=201326592&is=&fp' \
      '=result&fr=&word=%E5%95%86%E5%93%81%E5%9B%BE&queryWord=%E5%95%86%E5%93%81%E5%9B%BE&cl=2&lm=-1&ie=utf-8&oe=utf' \
      '-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode' \
      '=&nojc=&isAsync=&pn=30&rn=30&gsm=1e&1669474056038= '
res = requests.get(url, headers=headers, proxies=Proxy.get_proxy()).text
res_img = re.findall('"thumbURL":"(.*?)"', res, re.S)
n = 1
os.makedirs('商品图1')
for img in res_img:
    imgs = requests.get(url=img, headers=headers, proxies=Proxy.get_proxy()).content
    with open(os.path.join('商品图1', f'{n:06d}.png'), 'wb')as pd:
        pd.write(imgs)
        print(f"写入第{n}个图片成功！")
        n += 1
    # print(res_img)
    # pd.close()
