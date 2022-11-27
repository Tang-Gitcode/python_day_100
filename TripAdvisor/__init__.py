import requests
import json
import os
from jsonsearch import JsonSearch
from init_proxy import Proxy


# 代理池
# proxy = requests.get('http://api.xiequ.cn/VAD/GetIp.aspx?act=get&uid=102338&vkey=D0A1F6AD3B21F705ED0D16C07AAA02C4&num'
#                      '=1&time=30&plat=0&re=0&type=0&so=1&ow=1&spl=1&addr=&db=1 ').json()
# proxy = f"{proxy['data'][0]['IP']}:{proxy['data'][0]['Port']}".strip()
# print(f"使用的代理IP：{proxy}")
# proxies = {
#     'HTTP': "http://" + proxy,
#     'HTTPS': "https://" + proxy
# }

# os.environ['NO_PROXY'] = 'https://www.tripadvisor.com/data/graphql/ids'
url = "https://www.tripadvisor.com/data/graphql/ids"

headers = {
    # 'authority': 'www.tripadvisor.com',
    # 'method': 'POST',
    # 'path': '/data/graphql/ids',
    # 'scheme':'https',
    # 'accept': '*/*',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language':'zh-CN,zh;q=0.9',
    # 'content-length': '1239',
    'content-type': 'application/json',
    # 'Connection': 'keep-alive',
    # 'cookie': 'TADCID=ShS1Tl0Y7HMTJD81ABQCFdpBzzOuRA-9xvCxaMyI13GKSRrI8Yk-cd_Fxrx3XpNA2S3HukTLTF5q2xa0FiKQaM06bZVT-j7uBLE; TAUnique=%1%enc%3AnTJ1BUTsWrLY%2BUrucLaXzcVTRYJ4kZeDqfHbYYO4nyVQcF0be502LA%3D%3D; TASSK=enc%3AAOfrkbHy%2B6Z5jCb%2Fv2XvsyT7kdTUMdGr3qv9hQjJAVYFYCW7kjCaEYk7bG5MVPsHs%2FeheNlbwDs%2BjvxQyAeGwWf2dub2RXr5cqhUemcUUHs1xiVj759f7OOZE42HtSEBVg%3D%3D; ServerPool=B; BEPIN=%1%18478afd80e%3Bweb303a.a.tripadvisor.com%3A30023%3B; TATravelInfo=V2*AY.2022*AM.11*AD.27*DY.2022*DM.11*DD.28*A.2*MG.-1*HP.2*FL.3*DSM.1668472100995*RS.1; TATrkConsent=eyJvdXQiOiIiLCJpbiI6IkFMTCJ9; _pbjs_userid_consent_data=3524755945110770; _li_dcdm_c=.tripadvisor.com; _lc2_fpi=b140173de591--01ghwb0pcpz8f6cvaktrhrsaj8; __gads=ID=4b93ee832e54c876:T=1668472136:S=ALNI_MbhyerTACojy2wSFcftwqOspoPaNg; _lr_sampling_rate=100; _lr_env_src_ats=false; pbjs_li_nonid=%7B%7D; TART=%1%enc%3AAnsPIPVK9zn21HM8CmQGkloZfIZR90x0N%2FLg6TMb6RNzOgCED0DNDhDU3T2VDs32VvCd%2Bd238yc%3D; PMC=V2*MS.69*MD.20221114*LD.20221115; __gpi=UID=00000b7c1d6297d1:T=1668472136:RT=1668499298:S=ALNI_MYThn_7BSxRrkRXimDXGxY8Z__XkA; bm_sz=282073517DE4499BC5506712A60A29B8~YAAQ3NbdWPfdRnSEAQAA/gl/ehFlBUiKF/ARcSqh0aeKeUBfbhbA85c8FCyVieqpqVPzKrViryiahkTajcpoqkfilYJ8C6ocN75I33AyiFIIgn/eh1f3EM6eTNpLCNOhpTrggHcTcolyP3ieH7Xu1Aoo4cSc317/KZq0GjaEhBtGVyGEg95yRzAj91QCBua/ospp+KpwMNy+94V5BJ1Pm1J1pp+wwKn2YhG/RlBzdhKE4OH5Z/ckAbRgfi5pUmEMBztvk+IreaaoCJK8ca7DQWJyfBk43ZsdPi8eBIATT1caKIJYe0HXxMzKUPTryaLxoO1NEnuGkj8M829MLuQMAg==~3553075~4534597; PAC=AJ7Znbh_k90CWvZElUNwxg0JKqXloMfGUfcgCUYibcG-MO7RsnjERu4Lvpgy-7fZLYAY4df4l18ek-XJWU2IGjuR32SnOzWI-sd9FZYyKGDxsJo_Yf3Ti5YHUoiZR2tj0FbKlK3ja6tex_c0u51RAg19QrocTkOpWiK9vaU91S_BXXtb2vQZqZtbDE9j21X9-8shbNIpvRoovYn7jv9zlg7FT3OWxJjUZsd61ybMKyes; _lr_retry_request=true; __vt=rSEeQaU3h9W_hFMeABQCIf6-ytF7QiW7ovfhqc-AvSFqtA_hU2iqRJqdx7arY_MNH-Rfls0d02sUI16diQvyut2EGnSlWn5WwUMQCDtPRXU7W7-krSiF_b_At2zC2610WAn7FdqrdiSglxAOhzCRmTAe34k; ak_bmsc=696D8130469D027FF194E942C5845266~000000000000000000000000000000~YAAQ37x3aIFmbl6EAQAAIM4/exEJhDKd/kgN0q2Ze6ybJSEl8wt5pcEHyGTTLmU4HmcJQ3H49DhkUAB68kqkkHdY1SDSi7QIfR8hn6M1wMi5kJ4+vKvRKhyKujKMeV1s67JPCddGHlhBu3XRkJNVFCtb6brtcXoSv9SQZjH0UotEjsnbtrXKQTwqdeEObxI+fUtiVkBjmern+qUDozMDbpj0P2MxUQKIG20tArNJkTDktJvaK22jfJYmNITaG9wCbYbCoTRxzUNqQOXfxJQ4onGUmnRDbknbw8uzhkLdRlUDyHQtj0KMu0xsQ1j/zp7co552EMCtexz34kzI+eU/3t1ByLOaIru2k0Q2wwFHbrdGXj72vY1MuYf8j18N/AbncnKT24+pj8XlC1mrHa34; TASID=EA8F8E1F8B334DE08C46D9BDE3CC78C1; SRT=%1%enc%3AAnsPIPVK9zn21HM8CmQGkloZfIZR90x0N%2FLg6TMb6RNzOgCED0DNDhDU3T2VDs32VvCd%2Bd238yc%3D; TAReturnTo=%1%%2FHotel_Review-g187514-d7309373-Reviews-or10-The_Principal_Madrid-Madrid.html; roybatty=TNI1625!AKMm6ovj44Lzi%2FzEX1M1MxXJYL3VxVUtREPd2vmx1gQGi5ulI%2B2nM%2FsWwtzysj4469i%2FaQaJaHJs8y4TZChO90xtP3q93cpInNiNRTS9UKfJ%2FJTdxKmYUoacz44GSUnRUhigs254MknRkeNgJ9Ce90VVzn6%2FSW9jafuLG9p7G3dM%2C1; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Nov+15+2022+20%3A26%3A40+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=5b710653-69f2-49de-82d0-8aaaade56c2c&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; TASession=V2ID.EA8F8E1F8B334DE08C46D9BDE3CC78C1*SQ.36*LS.PageMoniker*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.en*FA.1*DF.0*TRA.false*LD.7309373*EAU._; TAUD=LA-1668472125932-1*RDD-1-2022_11_15*HDD-1-2022_11_27.2022_11_28.1*LD-43072614-2022.11.27.2022.11.28*LG-43072616-2.1.F.; _abck=0D117B804C800CC026FCF1DBBFACE1D7~0~YAAQ37x3aChubl6EAQAAlAJCewjog4BLTmzI+/C1tP+bkY43PSoyuFAlfc8VbwT9LsZQw93FJV9g8CLzbtYlBWDURmW5xBzWTr/F0XtgdqAjJTInTPMxRBJwSXhKCNSr9KR8KlmcZ8Aqqk1p6Lh4GLiMu+mpkT75cGiqVL2armtxjwJPUIxEqwHLANCTGk1rCvV8udv8igIZmK+o1PCFBvdE3tXzv9ZEyw9q1Ocg4mIGgAW6e0h3hgCrR8lTfJhHeowHrIDZUq9320RfUIOleFnEng8oUrpzN5NZ5HEE7OtncyB/7QD+yS8UmnvuinNvnlbBI20oWRWNRP8hU+TdbQXbsVhmMaSq0qC1Qo3ufY/G3U9obhx9CMyeMAJJQ77hjCwi~-1~-1~-1; bm_sv=CC8F9B7BD8371CBD200DE5F1358C63A7~YAAQ37x3aClubl6EAQAAlAJCexH7dJ7askgieUJYJ25/IBf65RQbQ+4dte6in5buNTN8iXepZiupef6Cl9SvG9AuI3VFFx5EqMYi+scvlu+p4TY2SOzR595o3KtLGAyPTC2oe1l3i/EmVzV0XBkDgZOEMG8tKDqiLZ5usmdLbRPdkqMBP+eYth/fYa9F0WrDn7+Au7xcvWHiEAUeJVN8Nn4d1/WIX7MEUx+yNcuwYcFoAf6UHSI1ps4Fu51gcP8VuktHVEP/~1',
    'origin': 'https://www.tripadvisor.com',
    # 'referer':'https://www.tripadvisor.com/Hotel_Review-g187514-d7309373-Reviews-or10-The_Principal_Madrid-Madrid.html',
    # 'sec-ch-ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    # 'sec-ch-ua-mobile':'?0',
    # 'sec-ch-ua-platform':"Windows",
    # 'sec-fetch-dest':'empty',
    # 'sec-fetch-mode':'cors',
    # 'sec-fetch-site':'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 '
                  'Safari/537.36',
    'x-requested-by': 'TNI1625!AMX7oPRdS40ZvJkAwABwXyYjI2gs1h103JA6iNl/IDU7Wi3ebxHLG8oEj7+qLKFJhtt1v/wAmwrlBVS7QEDWkRejBIac03bNcyTJC06fKxnwNESDyW7f0bSO8+wvWl0Z2RD4QcIMp17vzENwrWz1iXNP9/NppqxZ5uxlDUgEcm2+'
}

payload = json.dumps(
    [
        {
            "query": "ea9aad8c98a6b21ee6d510fb765a6522",
            "variables": {
                "locationId": 7309373,
                "offset": 10,
                "filters": [],
                "prefs": None,
                "initialPrefs": {},
                "limit": 10,
                "filterCacheKey": None,
                "prefsCacheKey": "locationReviewPrefs_7309373",
                "needKeywords": False,
                "keywordVariant": "location_keywords_v2_llr_order_30_en"
            }
        }
    ]
)


response = requests.post(url=url, headers=headers, data=payload, proxies=Proxy.get_proxies(Proxy())).text
reviews = json.loads(response)
# print(reviews)
reviews_data=reviews[0]
reviews_data_info=reviews_data
print(reviews_data_info)
# for item_data in response:
#     item_info=item_data['data']['locations'][0]
#     print(item_info)
#     display_name=item_info.get('displayName',{})
#     print(display_name)
# res_data:dict=response.get('data',[])
# res_dict={}
# res_dict_name:dict=res_dict.get('displayName',{})
# res_dict_name=res_dict.get('locations', {})
# print(res_dict_name)
#     # res_dict_name=res_dict.get('displayName')
#     # print(res_dict_name)
#     jsondata = JsonSearch(object=res, mode='j')
#     #获取姓名
#     res_name=jsondata.search_all_value(key='displayName')
#     #地址
#     res_long=jsondata.search_all_value.get('long',{})
#     print(res_name)
#     print(res_long)

