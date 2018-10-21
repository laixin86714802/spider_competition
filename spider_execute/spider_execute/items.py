# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderUserItem(scrapy.Item):
    """用户表"""
    source = scrapy.Field()
    mid = scrapy.Field()
    name = scrapy.Field()
    sex = scrapy.Field()
    rank = scrapy.Field()
    face = scrapy.Field()
    fans_badge = scrapy.Field()
    im9_sign = scrapy.Field()
    regtime = scrapy.Field()
    spacesta = scrapy.Field()
    level = scrapy.Field()
    birthday = scrapy.Field()
    sign = scrapy.Field()
    official_verify_type = scrapy.Field()
    official_verify_desc = scrapy.Field()
    vip_type = scrapy.Field()
    vip_status = scrapy.Field()
    toutu = scrapy.Field()
    toutu_id = scrapy.Field()
    following = scrapy.Field()
    fans = scrapy.Field()
    article = scrapy.Field()
    archive = scrapy.Field()
    insert_time = scrapy.Field()

class SpiderVideoItem(scrapy.Item):
    """视频表"""
    source = scrapy.Field()
    aid = scrapy.Field()
    ctime = scrapy.Field()
    desc = scrapy.Field()
    duration = scrapy.Field()
    mid = scrapy.Field()
    title = scrapy.Field()
    videos = scrapy.Field()
    tname = scrapy.Field()
    coin = scrapy.Field()
    danmaku = scrapy.Field()
    like = scrapy.Field()
    dislike = scrapy.Field()
    favorite = scrapy.Field()
    his_rank = scrapy.Field()
    reply = scrapy.Field()
    share = scrapy.Field()
    view = scrapy.Field()
    insert_time = scrapy.Field()

class SpiderFollowingsItem(scrapy.Item):
    """关注表"""
    source = scrapy.Field()
    mid = scrapy.Field()
    fmid = scrapy.Field()
    mtime = scrapy.Field()
    uname = scrapy.Field()
    official_verify_type = scrapy.Field()
    official_verify_desc = scrapy.Field()
    sign = scrapy.Field()
    insert_time = scrapy.Field()

class SpiderFansItem(scrapy.Item):
    """粉丝表"""
    source = scrapy.Field()
    mid = scrapy.Field()
    fmid = scrapy.Field()
    mtime = scrapy.Field()
    uname = scrapy.Field()
    official_verify_type = scrapy.Field()
    official_verify_desc = scrapy.Field()
    sign = scrapy.Field()
    insert_time = scrapy.Field()