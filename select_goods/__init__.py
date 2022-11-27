"""总系统接口创建商品"""
from init_proxy import Proxy
import requests
import json
import pandas as pd
import random
import os
import glob


# 初始数据
class InitialData(object):
    # 已售件数取1000-3000之间的随机数
    random_num = random.randint(1000, 3000)

    def __init__(self):
        # 请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                                    Chrome/106.0.0.0 Safari/537.36 ",
            'auth-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
                          '.eyJleHAiOjE2OTQzODEzODMsInN1YiI6IntcInNlc3Npb25cIjogXCI4ZDVlNWM0NDBjZTkwZTZmNTZlYzEyODQ1MDg2MzZkNlwiLCBcImFjY291bnRfaWRcIjogMTAwMCwgXCJhY2NvdW50X25hbWVcIjogXCJcXHU3NjdkXFx1NzY3ZFwiLCBcImxvZ2luX3RpbWVcIjogMTY2ODQzMDc4MywgXCJyZWdpc3Rlcl90aW1lXCI6IDAsIFwic3VwcGxpZXJfaWRcIjogMSwgXCJnb29kc19zb3VyY2VcIjogMSwgXCJyZWZyZXNoX3Rva2VuXCI6IFwiNWE0OGE0ZThmNDYwNWI2NGJkMGQ4MWQ2ZTM5MDI5ODZcIiwgXCJleHBpcmVfdGltZVwiOiAxNjk0MzUwNzgzfSJ9.5bXMQo6HdPZJPiIJKFfSy71cDVEvLPPxxzaJzXpq3ls '
        }

    def login(self):
        # 登录接口
        url_login = 'http://t-admin.helitong.cn/api/v1/sign/in'
        data = json.dumps({
            "account": "13530600569",
            "password": "560d4d8b173df72e813f0f1914aeb5df3240b53457000c55a1baa84fc389fa1e"
        })
        res_login = requests.post(url=url_login, headers=self.headers, data=data).text
        print(res_login)
        print('---------------------------------------------分割线-----------------------------------------------------\n')

    def category(self):
        # 分类接口
        url_category = 'http://t-admin.helitong.cn/api/v1/goods/category'
        res_category = requests.post(url=url_category, headers=self.headers).text
        print(res_category)
        print('---------------------------------------------分割线-----------------------------------------------------\n')

    def item(self):
        # 类目接口
        url_item = 'http://t-admin.helitong.cn/api/v1/goods/item'
        res_item = requests.post(url=url_item, headers=self.headers).text
        print(res_item)


# 上传图片
class Img(InitialData):  # 继承初始数据类
    def __init__(self):
        self.url = 'http://t-admin.helitong.cn/api/v1/upload/img'
        self.imgs_data_url = '../res_img/商品图'
        self.paths = glob.glob(os.path.join(self.imgs_data_url, "*.jpg"))
        super().__init__()

    def img_main(self):
        # 主图上传
        imgs = []
        for img in self.paths[0:6]:
            files = {'file': open(f'{img}', 'rb')}
            res_img = requests.post(url=self.url, headers=self.headers, files=files).json()['data']
            imgs.append(res_img)
        return imgs

    def img_detail(self):
        # 详情图上传
        imgs = []
        for img in self.paths[7:17]:
            files = {'file': open(f'{img}', 'rb')}
            res_img = requests.post(url=self.url, headers=self.headers, files=files).json()['data']
            imgs.append(res_img)
        return imgs

    def img_sku(self):
        # 规格图上传
        files = {'file': open('../res_img/商品图/000000.jpg', 'rb')}
        res_img = requests.post(url=self.url, headers=self.headers, files=files).json()['data']
        # print(res_img)
        return res_img


# 从商品表格中获取数据
class Excel(object):
    def __init__(self, brand, name, supply_price, settlement_price, sales_price, market_price):
        self.brand = brand
        self.name = name
        self.supply_price = supply_price
        self.settlement_price = settlement_price
        self.sales_price = sales_price
        self.market_price = market_price

    def excel(self, i: int):
        # 获取表格数据
        df = pd.read_excel(r'C:/Users/Administrator/Desktop/需上架商品.xlsx', sheet_name='我上传的商品')
        # 品牌
        self.brand = df.iloc[i, 1]
        # 名称
        self.name = df.iloc[i, 2]
        # 供货价
        self.supply_price = df.iloc[i, 5]
        # 结算价/集采结算价
        self.settlement_price = df.iloc[i, 6]
        # 销售价/集采价
        self.sales_price = df.iloc[i, 7]
        # 市场价
        self.market_price = df.iloc[i, 8]
        # print(brand, name, supply_price, settlement_price, sales_price, market_price)
        # return self.brand, self.name, self.supply_price, self.settlement_price, self.sales_price, self.market_price


# 创建商品
class Add(Img, Excel):  # 继承初始数据与上传图片类
    def add(self):
        # 添加商品接口
        url_add = 'http://t-admin.helitong.cn/api/v1/goods/add'
        requests_body = {
            "item_id": 376,
            "category_id": 357,
            "source": 2,  # 状态：1.自有 2.外采 3.定制
            "goods_name": f"{self.name}",
            "sales": self.random_num,
            "purchase_num": "50",
            "address": "上海",
            "unit": "",
            "goods_gallery": self.img_main(),
            "parameters": [],
            "goods_detail": self.img_detail(),
            "goods_spec": [
                {
                    "name": "规格名",
                    "id": 0,
                    "z_0": "",
                    "opt_0": "",
                    "key": "name_0",
                    "attrs": [
                        "规格值"
                    ],
                    "sel_data": [
                        {
                            "value": "one_0",
                            "label": "规格值",
                            "keys": "规格值"
                        }
                    ],
                    "imgs": [
                        self.img_sku()
                    ],
                    "val": "",
                    "valName": ""
                }
            ],
            "goods_sku": [
                {
                    "market_price": f"{self.market_price}",
                    "sale_price": f"{self.sales_price}",
                    "supply_price": f"{self.supply_price}",
                    "settle_price": f"{self.settlement_price}",
                    "purchase_price": f"{self.sales_price}",
                    "third_sku_sn": "",
                    "purchase_settle_price": f"{self.settlement_price}",
                    "fxj": 10,
                    "stock": "1000",
                    "sku": 0,
                    "zl": 0,
                    "url": self.img_sku(),
                    "img": self.img_sku(),
                    "ids": [
                        "one_0"
                    ],
                    "name": "规格值",
                    "id": 0,
                    "is_sale": 1,
                    "spec": [
                        {
                            "key": "规格名",
                            "value": "规格值"
                        }
                    ],
                    "name_0": "规格值"
                }
            ],
            "goods_after": {
                "is_exchange": 1,
                "is_return": 1,
                "is_no_reason_return": 0
            },
            "unsale_region": [],
            "brand_name": f"{self.brand}",
            "bar_code": "",
            "goods_type": 1,
            "tax_rate": 0,
            "tax_rate_code": "",
            "is_single_sale": 1,
            "ext_form_id": 0,
            "status": 2
        }
        res_add = requests.post(url=url_add, headers=self.headers, json=requests_body,
                                proxies=Proxy.get_proxy()).text
        print(res_add)
        # self.img()


if __name__ == '__main__':
    t = Add()
    for i in range(1, 46):
        t.excel(i)
        t.add()
    # t.img_main()
    # Excel()
