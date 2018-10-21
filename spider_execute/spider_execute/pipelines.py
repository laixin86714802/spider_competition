# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi

class SpiderExecutePipeline(object):
    def __init__(self, dbpool):
        # 连接池dbpool
        self.dbpool = dbpool
        # 定义查重队列
        self.ids_seen = set()

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass = pymysql.cursors.DictCursor,
            use_unicode= True,
        )
        # 定义接口
        dbpool = adbapi.ConnectionPool('pymysql', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        """按source字段区分"""
        # 用户表
        if item['source'] == 'user':
            query = self.dbpool.runInteraction(self.do_insert_user, item)
            query.addErrback(self.handle_error, item, spider)
            return item
        # 视频表
        elif item['source'] == 'video':
            query = self.dbpool.runInteraction(self.do_insert_video, item)
            query.addErrback(self.handle_error, item, spider)
            return item
        # 关注表
        elif item['source'] == 'follow':
            query = self.dbpool.runInteraction(self.do_insert_follow, item)
            query.addErrback(self.handle_error, item, spider)
            return item
        # 粉丝表
        elif item['source'] == 'fans':
            query = self.dbpool.runInteraction(self.do_insert_fans, item)
            query.addErrback(self.handle_error, item, spider)
            return item

    def do_insert_user(self, tx, item):
        """写入数据库"""
        sql = '''insert into bilibili_user_info(mid, name, sex, rank, face, fans_badge, im9_sign, regtime, spacesta, level, birthday, sign, official_verify_type, official_verify_desc, vip_type, vip_status, toutu, toutu_id, following, fans, article, archive, insert_time) 
            values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        params = (
            item['mid'],
            item['name'],
            item['sex'],
            item['rank'],
            item['face'],
            item['fans_badge'],
            item['im9_sign'],
            item['regtime'],
            item['spacesta'],
            item['level'],
            item['birthday'],
            item['sign'],
            item['official_verify_type'],
            item['official_verify_desc'],
            item['vip_type'],
            item['vip_status'],
            item['toutu'],
            item['toutu_id'],
            item['following'],
            item['fans'],
            item['article'],
            item['archive'],
            item['insert_time']
        )
        tx.execute(sql, params)


    def do_insert_video(self, tx, item):
        """写入数据库"""
        sql = '''insert into bilibili_video_info(aid, ctime, `desc`, duration, mid, title, videos, tname, coin, danmaku, `like`, dislike, favorite, his_rank, reply, `share`, `view`, insert_time) 
            values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        params = (
            item['aid'],
            item['ctime'],
            item['desc'],
            item['duration'],
            item['mid'],
            item['title'],
            item['videos'],
            item['tname'],
            item['coin'],
            item['danmaku'],
            item['like'],
            item['dislike'],
            item['favorite'],
            item['his_rank'],
            item['reply'],
            item['share'],
            item['view'],
            item['insert_time']
        )
        tx.execute(sql, params)

    def do_insert_follow(self, tx, item):
        """写入数据库"""
        sql = '''insert into bilibili_followings_info(mid, fmid, mtime, uname, official_verify_type, official_verify_desc, sign, insert_time) 
            values(%s, %s, %s, %s, %s, %s, %s, %s)'''
        params = (
            item['mid'],
            item['fmid'],
            item['mtime'],
            item['uname'],
            item['official_verify_type'],
            item['official_verify_desc'],
            item['sign'],
            item['insert_time']
        )
        tx.execute(sql, params)

    def do_insert_fans(self, tx, item):
        """写入数据库"""
        sql = '''insert into bilibili_fans_info(mid, fmid, mtime, uname, official_verify_type, official_verify_desc, sign, insert_time) 
            values(%s, %s, %s, %s, %s, %s, %s, %s)'''
        params = (
            item['mid'],
            item['fmid'],
            item['mtime'],
            item['uname'],
            item['official_verify_type'],
            item['official_verify_desc'],
            item['sign'],
            item['insert_time']
        )
        tx.execute(sql, params)

    def handle_error(self, failue, item, spider):
        """异常处理"""
        print (failue)