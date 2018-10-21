# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request
from spider_execute.items import SpiderFansItem

import json
import time
import traceback

class BilibiliSpider(scrapy.Spider):
    """bilibili爬虫"""
    name = "fans"
    # 4千万用户id
    start_urls = range(1, 400000000)
    url = 'https://api.bilibili.com/x/relation/followers?vmid=%s&pn=%s&ps=50&order=desc&jsonp=jsonp'
    # 复写settings
    custom_settings = {
        'AUTOTHROTTLE_ENABLED': False
    }
    # 复写head
    head = {
        'Host': 'api.bilibili.com'
    }

    def start_requests(self):
        '''初始化请求资源'''

        for mid in self.start_urls:
            self.mid = mid
            self.page = 1
            yield Request(
                url=self.url % (self.mid, self.page),
                headers=self.head,
                callback=self.parse
            )


    def parse(self, response):
        """结果集"""
        try:
            # 获取items
            data = json.loads(response.body_as_unicode())
            for jsData in data['data']['list']:
                item_dict = SpiderFansItem()
                item_dict['source'] = 'fans'
                item_dict['mid'] = self.mid
                item_dict['fmid'] = jsData['mid']
                item_dict['mtime'] = jsData['mtime']
                item_dict['uname'] = jsData['uname']
                item_dict['official_verify_type'] = jsData['official_verify']['type']
                item_dict['official_verify_desc'] = jsData['official_verify']['desc']
                item_dict['sign'] = jsData['sign']
                item_dict['insert_time'] = int(time.time())
                # 递归
                if len(data['data']) == 50 and self.page < 5:
                    self.page += 1
                    yield Request(
                        url=self.url % (self.mid, self.page),
                        headers=self.head,
                        callback=self.parse
                    )
                # 入库
                else:
                    yield item_dict

        except:
            print (traceback.format_exc())


