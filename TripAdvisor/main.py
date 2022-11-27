#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2022/11/14 23:07
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : search.py
# @Software    : PyCharm
# @Description :
import re
import requests
from bs4 import BeautifulSoup
import json
import uuid


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


class TripadvisorService(object):

    def __init__(self):
        self.base_url = 'https://www.tripadvisor.com'
        self.headers = {
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
        self.session = requests.session()

    def search(self, name: str):
        url = f'{self.base_url}/Search'
        params = {
            'q': name,
            'blockRedirect': True,
            'ssrc': 'a',
            'isSingleSearch': True,
            'locationRejected': True,
            'firstEntry': False,
        }
        res = requests.get(url=url, params=params, headers=self.headers)
        print(res.text)
        soup = BeautifulSoup(res.text, features='lxml')
        search_result = soup.select_one('div[class="search-results-list"][data-widget-type="TOP_RESULT"]')
        url_item = search_result.select_one('div[class="ui_columns is-mobile result-content-columns"]')
        print(url_item.get('onclick'))
        item_on_click = url_item.get('onclick')
        url = re.findall(r'this, \'(.*?)\', \{type:', item_on_click)[0]
        print(url)
        # self.item_page(url)

    def item_page(self, url_path):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'macOS',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',

        }
        url = f"{self.base_url}{url_path}"
        url = 'https://www.tripadvisor.com/Hotel_Review-g187514-d7309373-Reviews-The_Principal_Madrid-Madrid.html'
        res = requests.get(url=url, headers=headers)
        # print(res.text)
        soup = BeautifulSoup(res.text, features='lxml')
        scripts = soup.select('script')
        for script in scripts:
            if '__WEB_CONTEXT__' in script.text:
                # print(script)
                json_data = re.findall(r"urqlCache\":(.*?),\"redux\"", script.text)[0]
                # print('=' * 200)
                data = json.loads(json_data)
                for ural_id, urql_value in data.items():
                    if 'cachedFilters' in str(urql_value):
                        comment_data = json.loads(urql_value.get('data'))
                        print(comment_data)
                        comment_list = comment_data.get('locations', [])[0].get('reviewListPage', {}).get('reviews', [])
                        comment_result_list = [self.handle_comment_item(item) for item in comment_list]
                        print(comment_result_list)

    def comment(self, locationId: int = 12821584):
        url = 'https://www.tripadvisor.com/data/graphql/ids'
        headers = {
            # 必须
            'x-requested-by': '1TNI1625!AGYzG2CvMaqBa48OsiNxVli5YplAqfFP1zIIya7seHLClfzbxVM0531cFmaPSOI5TjRzvyytaA6ZIEHYN/oeAZEzrRRDdFY7vfoTrbTOKl4gfoOqvp/1+ptYIMeXsOTjqe4gss3hS6iUQcMeIC+f5kcV7woMbGBmn2iM3rIWgSW9',
            # 必须
            'origin': 'https://www.tripadvisor.com',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        data = [
            # {
            #     "query": "0eb3cf00f96dd65239a88a6e12769ae1",
            #     "variables": {
            #         "interaction": {
            #             "productInteraction": {
            #                 "interaction_type": "CLICK",
            #                 "site": {
            #                     "site_name": "ta",
            #                     "site_business_unit": "Hotels",
            #                     "site_domain": "www.tripadvisor.com"
            #                 },
            #                 "pageview": {
            #                     "pageview_request_uid": "fca49486-64f0-426d-9a90-d3ac64a2b50d",
            #                     "pageview_attributes": {
            #                         "location_id": 7309373,
            #                         "geo_id": 187514,
            #                         "servlet_name": "Hotel_Review"
            #                     }
            #                 },
            #                 "user": {
            #                     "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            #                     "site_persistent_user_uid": "web380a.222.128.44.3.18476036C65",
            #                     "unique_user_identifiers": {
            #                         "session_id": "6B9DD414A1D74F1B99D88DF0060E6D8A"
            #                     }
            #                 },
            #                 "search": {},
            #                 "item_group": {
            #                     "item_group_collection_key": "fca49486-64f0-426d-9a90-d3ac64a2b50d"
            #                 },
            #                 "item": {
            #                     "product_type": "Hotels",
            #                     "item_id_type": "ta-location-id",
            #                     "item_id": 7309373,
            #                     "item_attributes": {
            #                         "element_type": "number",
            #                         "action_name": "REVIEW_NAV",
            #                         "page_number": 2,
            #                         "offset": 10,
            #                         "limit": 10
            #                     }
            #                 }
            #             }
            #         }
            #     }
            # },
            {
                "query": "ea9aad8c98a6b21ee6d510fb765a6522",
                "variables": {
                    "locationId": locationId,
                    "offset": 0,
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
                    "limit": 10,
                    "filterCacheKey": "locationReviewFilters_7309373",
                    "prefsCacheKey": "locationReviewPrefs_7309373",
                    "needKeywords": False,
                    "keywordVariant": "location_keywords_v2_llr_order_30_en"
                }
            },
            # {
            #     "query": "b050e7606f36c30459a65090ee6df9cf",
            #     "variables": {
            #         "0": "{",
            #         "1": "}",
            #         "placementKey": "INTERSTITIAL",
            #         "limit": 50,
            #         "uid": "fca49486-64f0-426d-9a90-d3ac64a2b50d",
            #         "sessionId": "6B9DD414A1D74F1B99D88DF0060E6D8A",
            #         "currency": "HKD",
            #         "sectionTypes": [
            #             "Mixer_ArticlesHeroStoriesHighlightSection",
            #             "Mixer_ArticlesMosaicSection",
            #             "Mixer_FeaturedStoriesSection",
            #             "Mixer_Shelf",
            #             "Mixer_EditorialFeatureSection",
            #             "Mixer_FullImageFeatureCardSection",
            #             "Mixer_InsetImageFeatureCardSection",
            #             "Mixer_AdPlaceholderSection",
            #             "Mixer_CategorySearchesSection",
            #             "Mixer_FactSheetSection",
            #             "Mixer_PromotionalBannerSection",
            #             "Mixer_TravelersChoiceSection",
            #             "Mixer_InteractiveMapSection",
            #             "Mixer_ArticlesKeepExploringSection",
            #             "Mixer_InterstitialSection"
            #         ],
            #         "sectionContentTypes": [
            #             "Mixer_DescriptionAndCarousel",
            #             "Mixer_FlexGrid",
            #             "Mixer_ImageAndCarousel",
            #             "Mixer_MediumCarousel",
            #             "Mixer_NarrowCarousel",
            #             "Mixer_PlusCarousel",
            #             "Mixer_TravelerSpotlightCarousel",
            #             "Mixer_WideCarousel",
            #             "Mixer_ProminentFlexList"
            #         ],
            #         "cardTypes": [
            #             "Mixer_PoiVerticalStandardCard",
            #             "Mixer_PoiVerticalMerchandisingCard",
            #             "Mixer_PoiVerticalDescriptionCard",
            #             "Mixer_PoiVerticalNameWithButtonCard",
            #             "Mixer_GeoVerticalMinimalCard",
            #             "Mixer_TripVerticalContributorCard",
            #             "Mixer_VrGeoVerticalMinimalCard",
            #             "Mixer_GeoImageBackgroundCard",
            #             "Mixer_CustomImageBackgroundCard",
            #             "Mixer_AttractionTaxonomyImageBackgroundCard",
            #             "Mixer_LinkPostEditorialCard",
            #             "Mixer_TripEditorialCard",
            #             "Mixer_VideoEditorialCard",
            #             "Mixer_ForumCard",
            #             "Mixer_UgcEditorialFeatureLinkPostCard",
            #             "Mixer_UgcEditorialFeatureTripCard",
            #             "Mixer_ReviewVerticalContributorCard",
            #             "Mixer_CustomVerticalMinimalCard",
            #             "Mixer_AttractionFlexCard",
            #             "Mixer_GeoVerticalNameWithButtonCard"
            #         ],
            #         "route": {
            #             "page": "Hotel_Review",
            #             "params": {
            #                 "detailId": 7309373,
            #                 "geoId": 187514,
            #                 "offset": "r10"
            #             }
            #         }
            #     }
            # },
            # {
            #     "query": "dd297ef79164a42dba1997b10f33d055",
            #     "variables": {
            #         "locationId": 7309373,
            #         "application": "HOTEL_DETAIL",
            #         "currencyCode": "HKD",
            #         "pricingMode": "BASE_RATE",
            #         "sessionId": "6B9DD414A1D74F1B99D88DF0060E6D8A",
            #         "pageviewUid": "fca49486-64f0-426d-9a90-d3ac64a2b50d",
            #         "travelInfo": {
            #             "adults": 2,
            #             "rooms": 1,
            #             "checkInDate": "2022-11-27",
            #             "checkOutDate": "2022-11-28",
            #             "childAgesPerRoom": [],
            #             "usedDefaultDates": True
            #         },
            #         "requestNumber": 1,
            #         "filters": None,
            #         "route": {
            #             "page": "Hotel_Review",
            #             "params": {
            #                 "detailId": 7309373,
            #                 "geoId": 187514,
            #                 "offset": "r10"
            #             }
            #         }
            #     }
            # }
        ]
        res = self.session.post(url=url, json=data, headers=headers)
        print(res.text)

    def handle_comment_item(self, comment_item_data: dict):
        """获取需求要求字段信息"""
        _user_profile = comment_item_data.get('userProfile', {})
        # 用户名
        displayName = _user_profile.get('displayName')
        # 发布时间
        publishedDate = comment_item_data.get('publishedDate')
        # 城市地区
        additionalNames = _user_profile.get('hometown', {}).get('location', {}).get('additionalNames', {}).get('long') if _user_profile.get('hometown', {}).get('location') else None
        # 贡献
        sumAllUgc = _user_profile.get('contributionCounts', {}).get('sumAllUgc')
        # 帮助
        helpfulVote = _user_profile.get('contributionCounts', {}).get('helpfulVote')
        # 打分
        rating = comment_item_data.get('rating')
        # 入住时间
        stayDate = comment_item_data.get('tripInfo', {}).get('stayDate')

        # 子评分
        additionalRatings = comment_item_data.get('additionalRatings', [])
        additionalRatingsValue = {_.get('ratingLabel'): _.get('rating') for _ in additionalRatings}

        item_info = {
            'username': displayName,
            'publishedDate': publishedDate,
            'additionalNames': additionalNames,
            'sumAllUgc': sumAllUgc,
            'helpfulVote': helpfulVote,
            'rating': rating,
            'stayDate': stayDate,
            'additionalRatingsValue': additionalRatingsValue,
        }
        print(item_info)
        return item_info


if __name__ == '__main__':
    t = TripadvisorService()
    t.search('The Princip3232al Madrid6')
    # t.item_page('/Hotel_Review-g187514-d7309373-Reviews-The_Principal_Madrid-Madrid.html')
    # t.comment()
