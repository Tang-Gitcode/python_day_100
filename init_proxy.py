import requests
import time


class Proxy(object):
    @classmethod
    def get_proxy(cls):
        # 代理池
        proxy = requests.get(
            'http://api.xiequ.cn/VAD/GetIp.aspx?act=get&uid=102338&vkey=D0A1F6AD3B21F705ED0D16C07AAA02C4&num'
            '=1&time=30&plat=0&re=0&type=0&so=1&ow=1&spl=1&addr=&db=1 ').json()
        proxy = f"{proxy['data'][0]['IP']}:{proxy['data'][0]['Port']}".strip()
        # print(f"使用的代理IP：{proxy}")
        proxies = {
            'HTTP': "http://" + proxy,
            'HTTPS': "https://" + proxy
        }
        time.sleep(5)
        return proxies


if __name__ == '__main__':
    Proxy()
