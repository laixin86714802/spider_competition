#!/usr/bin/env python
# -*- coding: utf-8 -*-

class VideoModel(object):
    @staticmethod
    def get_video_duration(cursor):
        """视频时长"""
        command = '''
        SELECT duration, COUNT(*) AS count
        FROM bilibili_video_info
        GROUP BY duration'''

        result = cursor.query(command)
        return result if result else []

    @staticmethod
    def get_video_videos(cursor):
        """视频数量"""
        command = '''
        SELECT videos, COUNT(*) AS count
        FROM bilibili_video_info
        GROUP BY videos'''

        result = cursor.query(command)
        return result if result else []

    @staticmethod
    def get_video_tname(cursor):
        """视频分区"""
        command = '''
        SELECT tname, COUNT(*) AS count
        FROM bilibili_video_info
        GROUP BY tname'''

        result = cursor.query(command)
        return result if result else []

    @staticmethod
    def get_video_coin(cursor):
        """硬币数量"""
        command = '''
        SELECT '0' AS coin, COUNT(*) AS count
        FROM bilibili_video_info
        WHERE coin = 0
        UNION ALL
        SELECT '1-100', COUNT(*) AS count
        FROM bilibili_video_info
        WHERE coin >= 1 AND coin < 100
        UNION ALL
        SELECT '100-500', COUNT(*) AS count
        FROM bilibili_video_info
        WHERE coin >= 100 AND coin < 500
        UNION ALL
        SELECT '>500', COUNT(*) AS count
        FROM bilibili_video_info
        WHERE coin >= 500'''

        result = cursor.query(command)
        return result if result else []

    @staticmethod
    def get_video_danmaku(cursor):
        """弹幕数量"""
        command = '''
        SELECT '0-100' AS danmaku, COUNT(*) AS count
        FROM bilibili_video_info
        WHERE danmaku < 100
        UNION ALL
        SELECT '0-200', COUNT(*)
        FROM bilibili_video_info
        WHERE danmaku >= 100 AND danmaku < 200
        UNION ALL
        SELECT '200-500', COUNT(*)
        FROM bilibili_video_info
        WHERE danmaku >= 200 AND danmaku < 500
        UNION ALL
        SELECT '500-2000', COUNT(*)
        FROM bilibili_video_info
        WHERE danmaku >= 500 AND danmaku < 2000
        UNION ALL
        SELECT '>2000', COUNT(*)
        FROM bilibili_video_info
        WHERE danmaku >= 2000'''

        result = cursor.query(command)
        return result if result else []