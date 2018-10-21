# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request
from spider_execute.items import SpiderVideoItem

import json
import time
import traceback


class BilibiliSpider(scrapy.Spider):
    """bilibili爬虫"""
    name = "video"
    # 4千万视频id
    start_urls = range(65005, 400000000)
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

        for aid in self.start_urls:
            url = 'https://api.bilibili.com/x/web-interface/view?aid=%s' % aid
            yield Request(url=url, headers=self.head)

    def parse(self, response):
        """结果集"""
        try:
            # 获取items
            data = json.loads(response.body_as_unicode())
            if data['data']:
                item_dict = SpiderVideoItem()
                jsData = data['data']
                item_dict['source'] = 'video'
                item_dict['aid'] = jsData['aid']
                item_dict['pubdate'] = jsData['pubdate']
                item_dict['desc'] = jsData['desc']
                item_dict['duration'] = jsData['duration']
                item_dict['mid'] = jsData['owner']['mid']
                item_dict['title'] = jsData['title']
                item_dict['videos'] = jsData['videos']
                item_dict['tname'] = jsData['tname']
                item_dict['coin'] = jsData['stat']['coin']
                item_dict['danmaku'] = jsData['stat']['danmaku']
                item_dict['like'] = jsData['stat']['like']
                item_dict['dislike'] = jsData['stat']['dislike']
                item_dict['favorite'] = jsData['stat']['favorite']
                item_dict['his_rank'] = jsData['stat']['his_rank']
                item_dict['reply'] = jsData['stat']['reply']
                item_dict['share'] = jsData['stat']['share']
                item_dict['view'] = jsData['stat']['view']
                item_dict['insert_time'] = int(time.time())

                yield item_dict

        except:
            print(traceback.format_exc())


