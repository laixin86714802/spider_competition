# -*- coding: utf-8 -*-

import scrapy
from scrapy import FormRequest
from spider_execute.items import SpiderUserItem

import requests
import json
import time
import traceback
import random
import base64

class BilibiliSpider(scrapy.Spider):
    """bilibili爬虫"""
    name = "user"
    # 4千万用户id
    start_urls = range(1, 400000000)

    def get_user_agent(self):
        """浏览器头"""
        ua_list = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0"
        ]
        return {'User-Agent': random.choice(ua_list)}

    def get_proxies(self):
        '''阿布云代理ip服务器'''
        proxyServer = "http://http-dyn.abuyun.com:9020"

        # 代理隧道验证信息
        proxyUser = "H500KAD7WD50V50D"
        proxyPass = "9787D9AE0B6E817F"

        proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")
        return proxyServer, proxyAuth

    def start_requests(self):
        '''初始化请求资源'''

        for mid in self.start_urls:
            url = 'https://space.bilibili.com/ajax/member/GetInfo'
            proxyServer, proxyAuth = self.get_proxies()
            payload = {
                'mid': str(mid)
            }
            head = {
                'Referer': 'https://space.bilibili.com/%s/' % mid,
                'Proxy-Authorization': proxyAuth
            }
            yield FormRequest(
                url=url,
                headers=head,
                formdata=payload,
                callback=self.parse,
                meta={'proxy': proxyServer}
            )


    def parse(self, response):
        """结果集"""
        try:
            # 获取items
            data = json.loads(response.body_as_unicode())
            status = data['status'] if 'status' in data.keys() else False
            if status == True and 'data' in data.keys():
                item_dict = SpiderUserItem()
                jsData = data['data']
                item_dict['source'] = 'user'
                item_dict['mid'] = jsData['mid']
                item_dict['name'] = jsData['name']
                item_dict['sex'] = jsData['sex']
                item_dict['rank'] = jsData['rank']
                item_dict['face'] = jsData['face']
                item_dict['fans_badge'] = 1 if jsData['fans_badge'] else 0
                item_dict['im9_sign'] = jsData['im9_sign']
                item_dict['regtime'] = jsData.get('regtime', 0) if jsData.get('regtime', 0) is not None else 0
                item_dict['spacesta'] = jsData['spacesta']
                item_dict['level'] = jsData['level_info']['current_level'] if jsData['level_info']['current_level'] else 0
                item_dict['birthday'] = jsData['birthday'] if 'birthday' in jsData.keys() else ''
                item_dict['sign'] = jsData['sign']
                item_dict['official_verify_type'] = jsData['official_verify']['type']
                item_dict['official_verify_desc'] = jsData['official_verify']['desc']
                item_dict['vip_type'] = jsData['vip']['vipType'] if jsData['vip']['vipType'] else -1
                item_dict['vip_status'] = jsData['vip']['vipStatus'] if jsData['vip']['vipStatus'] else -1
                item_dict['toutu'] = jsData['toutu']
                item_dict['toutu_id'] = jsData['toutuId']
                item_dict['insert_time'] = int(time.time())
                # 粉丝
                try:
                    res = requests.get(
                        url='https://api.bilibili.com/x/relation/stat?vmid=%s&jsonp=jsonp' % item_dict['mid'],
                        headers=self.get_user_agent()
                    )
                    if res.status_code == 200:
                        data = json.loads(res.text)
                        item_dict['following'] = data['data']['following']
                        item_dict['fans'] = data['data']['follower']
                    else:
                        item_dict['following'] = -1
                        item_dict['fans'] = -1
                except:
                    item_dict['archive'] = -2
                    item_dict['article'] = -2
                # 文章接口
                try:
                    res = requests.get(
                        url='https://api.bilibili.com/x/space/upstat?mid=%s&jsonp=jsonp' % item_dict['mid'],
                        headers=self.get_user_agent()
                    )
                    if res.status_code == 200:
                        data = json.loads(res.text)
                        item_dict['archive'] = data['data']['archive']['view']
                        item_dict['article'] = data['data']['article']['view']
                    else:
                        item_dict['archive'] = -1
                        item_dict['article'] = -1
                except:
                    item_dict['archive'] = -2
                    item_dict['article'] = -2
                yield item_dict

        except:
            print (traceback.format_exc())


