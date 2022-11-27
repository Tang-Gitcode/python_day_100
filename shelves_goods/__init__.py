# -*- coding: utf-8 -*-
"""
@author mini-white
@date 2022年11月27日 14:22:54
@packageName 
@className __init__.py
@version 1.0.0
@describe 总系统京东商品上架
"""
import requests
from init_proxy import Proxy
from colorama import Fore


class List(object):
    page = 1

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/106.0.0.0 Safari/537.36",
            "auth-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
                          ".eyJleHAiOjE2OTU0ODAxOTYsInN1YiI6IntcInNlc3Npb25cIjogXCIyMDBkYmI2MjYyZDI3ZDZkY2E1ZDc0NjYwNTZmOTg0OVwiLCBcImFjY291bnRfaWRcIjogMTAwMCwgXCJhY2NvdW50X25hbWVcIjogXCJcXHU3NjdkXFx1NzY3ZFwiLCBcImxvZ2luX3RpbWVcIjogMTY2OTUyOTU5NiwgXCJyZWdpc3Rlcl90aW1lXCI6IDAsIFwic3VwcGxpZXJfaWRcIjogMSwgXCJnb29kc19zb3VyY2VcIjogMSwgXCJyZWZyZXNoX3Rva2VuXCI6IFwiM2IzMGE0NTI0MTNmYmRiMjdjZGI5ODM3MTBmYzE0YThcIiwgXCJleHBpcmVfdGltZVwiOiAxNjk1NDQ5NTk2fSJ9.YT3VsgPvUjCvaF8ahC5mGoGl96HLt1vLg9riKIDAmkg "
        }

    def goods_list(self):
        # 商品列表
        url = 'http://t-admin.helitong.cn/api/v1/goods/jd/list'
        data = {
            "page": self.page,
            "page_size": 100,
            "is_own": -1,
            "name": "",
            "is_stock": -1,
            "status": 3
        }
        res_list = requests.post(url=url, headers=self.headers, json=data, proxies=Proxy.get_proxy()).json()['data'][
            'items']
        # print(res_list)
        ids_list = []
        for item in res_list:
            # print(item)
            # print(ids_value)

            # if float(item['operating_margin']) > 0.00:
                # print(item)
            operating_margin = item.get('operating_margin', [])
            # print(operating_margin)
            if float(operating_margin) > 0.00:
                ids_value = item.get('goods_id', [])
                ids_list.append(ids_value)
                # print(ids_list)
        return ids_list

    def onsale(self):
        # 批量上架
        count = 0
        while count <= 50:
            url = 'http://t-admin.helitong.cn/api/v1/goods/onsale'
            data = {
                "ids": self.goods_list()
            }
            print(self.goods_list())
            try:
                res_onsale = requests.post(url=url, headers=self.headers, json=data, proxies=Proxy.get_proxy()).json()
                print(res_onsale)
                success_count = res_onsale['data']['success_count']  # 成功条数
                fail_count = res_onsale['data']['fail_count']  # 失败条数
                print(f"{Fore.GREEN}操作成功！\t成功{success_count}条，失败{fail_count}条{Fore.BLACK}")
            except Exception as e:
                print(f"error:{e}")
            finally:
                if len(self.goods_list()) < 10:
                    self.page += 1
                    count += 1
                    if count > 50:
                        print(f"{Fore.RED}提示：成功少于10条次数大于{count - 1}次，程序关闭!{Fore.BLACK}")
                        break


if __name__ == '__main__':
    t = List()
    while t.onsale():
        t.onsale()
