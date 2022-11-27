import re

import arrow
import requests
import xlsxwriter
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter

from init_proxy import Proxy


def get_current_millisecond_time() -> int:
    """
    description:  获取当前时间戳-毫秒级
    :return:      1599805496610 -> str
    """
    return int(arrow.now().timestamp() * 1000)


def get_json_value_by_key(in_json, target_key, results=[]) -> list:
    if isinstance(in_json, dict):  # 如果输入数据的格式为dict
        for key in in_json.keys():  # 循环获取key
            data = in_json[key]
            get_json_value_by_key(data, target_key, results=results)  # 回归当前key对于的value
            if key == target_key:  # 如果当前key与目标key相同就将当前key的value添加到输出列表
                results.append(data)

    elif isinstance(in_json, list) or isinstance(in_json, tuple):  # 如果输入数据格式为list或者tuple
        for data in in_json:  # 循环当前列表
            get_json_value_by_key(data, target_key, results=results)  # 回归列表的当前的元素

    return results


class Tripadvisor(object):
    def __init__(self):
        self.ids_url = 'https://www.tripadvisor.com/data/graphql/ids'

        self.headers = {
            # key必录  value貌似可以随便写
            'x-requested-by': 'TNI1625!AGYzG2CvMaqBa48OsiNxVli5YplAqfFP1zIIya7seHLClfzbxVM0531cFmaPSOI5TjRzvyytaA6ZIEHYN/oeAZEzrRRDdFY7vfoTrbTOKl4gfoOqvp/1+ptYIMeXsOTjqe4gss3hS6iUQcMeIC+f5kcV7woMbGBmn2iM3rIWgSW9',
            # 必须
            'origin': 'https://www.tripadvisor.com',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }

    def search_url(self, url: str):
        """根据url抓取信息"""
        head_name = self.get_head_name(url)
        excel_path = f"../TripAdvisor/{head_name}.xlsx"
        self.excel = ToExcel(excel_path, 'sheet')
        self.excel.write_title([
            'UserID',
            'UserCommentDate',
            'UserAddress',
            'CommentContribution',
            'CommentUsefulness',
            'OverallRating',
            'UserCheckInDate',
            'Rooms',
            'Service',
            'Cleanliness',
            'Sleep Quality',
            'Business service (e.g., internet access)',
            'Check in / front desk',
            'Location',
            'Value',
        ])
        location_id = self.resolve_location_id(url)
        self.get_comment(location_id)
        self.excel.close()
        print(excel_path)

    def search_keyword(self, keyword: str):
        """
        搜索关键字酒店列表
        :param keyword: 关键字
        :return:
        """
        url = f'https://www.tripadvisor.com/Search'
        headers = {
            'accept': 'text/html, */*',
            'accept-encoding': 'gzip, deflate, br',
            'content-type': 'Application/json; charset=utf-8',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'sec-ch-ua-platform': '"macOS"',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        }
        params = {
            'q': keyword,
            'blockRedirect': True,
            'ssrc': 'h',
            'isSingleSearch': True,
            'locationRejected': True,
            'firstEntry': False,
        }
        result = []
        try:
            res = requests.get(url=url, params=params, headers=headers)
            soup = BeautifulSoup(res.text, features='html.parser')
            title_list = soup.select('.result-title')
            for title in title_list:
                name = title.text.replace('\n', '')
                item_on_click = title.get('onclick')
                url = re.findall(r'this, \'(.*?)\', \{type:', item_on_click)[0]
                item_url = f"https://www.tripadvisor.com{url}"
                item = {
                    'name': name,
                    'url': item_url,
                    'location_id': self.resolve_location_id(item_url)
                }
                result.append(item)
                print(item)
        except Exception as e:
            print(e)
        return result

    @staticmethod
    def resolve_location_id(item_url: str = None):
        """
        解析酒店url中的location_id用户获取评论信息
        :param item_url: 酒店url  -> https://www.tripadvisor.com/Hotel_Review-g187514-d23996885-Reviews-Thompson_Madrid_a_Hyatt_brand-Madrid.html
        :return: 酒店id           -> 23996885
        """
        location_id = re.findall(r"-d(.*?)-R", item_url)[0]
        return location_id

    def get_head_name(self, url: str):
        response = requests.get(url=url, headers=self.headers, proxies=Proxy.get_proxy())
        soup = BeautifulSoup(response.text, features="lxml")

        head_name = soup.select_one('#HEADING').text
        return head_name

    def get_comment(self, location_id: str):
        """
        获取酒店评论信息
        :param location_id:
        :return:
        """
        start_timestamp = get_current_millisecond_time()

        page, limit = 0, 20
        count = 0
        comment_list = []
        session = requests.Session()
        session.mount('http://', HTTPAdapter(max_retries=3))
        session.mount('https://', HTTPAdapter(max_retries=3))
        while True:
            data = [
                {
                    "query": "ea9aad8c98a6b21ee6d510fb765a6522",
                    "variables": {
                        "locationId": location_id,
                        "offset": page * limit,
                        "filters": [
                            {
                                "axis": "LANGUAGE",
                                "selections": [
                                    "en"
                                ]
                            }
                        ],
                        "prefs": None,
                        "initialPrefs": {},
                        "limit": limit,
                        "filterCacheKey": "locationReviewFilters_7309373",
                        "prefsCacheKey": "locationReviewPrefs_7309373",
                        "needKeywords": False,
                        "keywordVariant": "location_keywords_v2_llr_order_30_en"
                    }
                },
            ]
            res = session.post(url=self.ids_url, json=data, headers=self.headers, proxies=Proxy.get_proxies(Proxy()))
            total_count = get_json_value_by_key(res.json(), 'totalCount', [])[0]
            reviews = get_json_value_by_key(res.json(), 'reviews', [])[0]
            if page * limit >= total_count:
                break
            for item_data in reviews:
                item_info = self._handle_comment_item(item_data)
                count += 1
                print(f"{count} / {total_count} : {item_info}")
                comment_list.append(item_info)
            page += 1

        end_timestamp = get_current_millisecond_time()

        consuming_time = int((end_timestamp - start_timestamp) / 1000)
        print(f"总耗时: {consuming_time} 秒")
        return comment_list

    def _handle_comment_item(self, item_data: dict):
        """
        处理评论信息提取字段
        :param item_data: 
        :return: 
        """
        """获取需求要求字段信息"""
        _user_profile = item_data.get('userProfile', {})
        # 用户名
        display_name = _user_profile.get('displayName', '')
        # 发布时间
        published_date = item_data.get('publishedDate', '')
        # 城市地区
        additional_names = _user_profile.get('hometown', {}).get('location', {}).get('additionalNames', {}).get('long', '') if _user_profile.get('hometown', {}).get('location') else ''
        # 贡献
        sum_all_ugc = _user_profile.get('contributionCounts', {}).get('sumAllUgc', '')
        # 帮助
        helpful_vote = _user_profile.get('contributionCounts', {}).get('helpfulVote', '')
        # 打分
        rating = item_data.get('rating', '')
        # 入住时间
        stay_date = item_data.get('tripInfo', {}).get('stayDate') if item_data.get('tripInfo') else ''

        # 子评分
        additional_ratings = item_data.get('additionalRatings', [])
        additional_ratings_value = {_.get('ratingLabel'): _.get('rating') for _ in additional_ratings}

        comment_info = {
            'display_name': display_name,
            'published_date': published_date,
            'additional_names': additional_names,
            'sum_all_ugc': sum_all_ugc,
            'helpful_vote': helpful_vote,
            'rating': rating,
            'stay_date': stay_date,
            'Rooms': additional_ratings_value.get('Rooms', ''),
            'Service': additional_ratings_value.get('Service', ''),
            'Cleanliness': additional_ratings_value.get('Cleanliness', ''),
            'Sleep Quality': additional_ratings_value.get('Sleep Quality', ''),
            'Business service (e.g., internet access)': additional_ratings_value.get('Business service (e.g., internet access)', ''),
            'Check in / front desk': additional_ratings_value.get('Check in / front desk', ''),
            'Location': additional_ratings_value.get('Location', ''),
            'Value': additional_ratings_value.get('Value', ''),
        }

        self.excel.write(list(comment_info.values()))
        return comment_info


class ToExcel(object):
    def __init__(self, excel_path: str, sheet_name: str):
        self.f = xlsxwriter.Workbook(
            excel_path,
            options={
                'strings_to_urls': False,
                'default_date_format': '%Y-%m-%d %H:%M:%S'
            })
        self.ws = self.f.add_worksheet(sheet_name)
        self.count = 0

    def write_title(self, data: list):
        for index, value in enumerate(data):
            self.ws.write_string(0, index, str(value))

    def write(self, data: list):
        self.count += 1
        for index, value in enumerate(data):
            self.ws.write_string(self.count, index, str(value))

    def close(self):
        self.f.close()


if __name__ == '__main__':
    t = Tripadvisor()
    url_list = [

        'https://www.tripadvisor.com/Hotel_Review-g187309-d12821584-Reviews-BEYOND_by_Geisel-Munich_Upper_Bavaria_Bavaria.html',
        'https://www.tripadvisor.com/Hotel_Review-g187849-d2417960-Reviews-Chateau_Monfort-Milan_Lombardy.html',
        'https://www.tripadvisor.com/Hotel_Review-g186338-d23274923-Reviews-Pan_Pacific_London-London_England.html',
        'https://www.tripadvisor.com/Hotel_Review-g187147-d270546-Reviews-Hotel_Elysia-Paris_Ile_de_France.html',
        'https://www.tripadvisor.com/Hotel_Review-g188590-d232321-Reviews-Ambassade_Hotel-Amsterdam_North_Holland_Province.html',
        'https://www.tripadvisor.com/Hotel_Review-g187791-d13393444-Reviews-Singer_Palace_Hotel-Rome_Lazio.html',
        'https://www.tripadvisor.com/Hotel_Review-g187323-d230572-Reviews-Grand_Hyatt_Berlin-Berlin.html',
        'https://www.tripadvisor.com/Hotel_Review-g187497-d7142609-Reviews-Serras_Barcelona-Barcelona_Catalonia.html',
        'https://www.tripadvisor.com/Hotel_Review-g190454-d3346123-Reviews-Hotel_Sans_Souci_Wien-Vienna.html',
        'https://www.tripadvisor.com/Hotel_Review-g187514-d7309373-Reviews-The_Principal_Madrid-Madrid.html',
    ]
    for url in url_list:
        # print(url)
        t.search_url(url)
