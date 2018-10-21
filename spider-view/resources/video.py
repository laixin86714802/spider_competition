#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restplus.resource import Resource

from server.decorators import Response
from configs import api
from server.logger import log
from operations.video import VideoOperation
from filters.video import VideoFilter

class Duration(Resource):
    @staticmethod
    @VideoFilter.filter_video_duration(result=list)
    @VideoOperation.get_video_duration()
    def get():
        """视频时长"""
        log.info('视频时长')
        return Response()

class Videos(Resource):
    @staticmethod
    @VideoFilter.filter_video_videos(result=list)
    @VideoOperation.get_video_videos()
    def get():
        """视频数量"""
        log.info('视频数量')
        return Response()

class Tname(Resource):
    @staticmethod
    @VideoFilter.filter_video_tname(result=list)
    @VideoOperation.get_video_tname()
    def get():
        """视频分区"""
        log.info('视频分区')
        return Response()

class Coin(Resource):
    @staticmethod
    @VideoFilter.filter_video_coin(result=list)
    @VideoOperation.get_video_coin()
    def get():
        """硬币数量"""
        log.info('硬币数量')
        return Response()

class Danmaku(Resource):
    @staticmethod
    @VideoFilter.filter_video_danmaku(result=list)
    @VideoOperation.get_video_danmaku()
    def get():
        """弹幕数量"""
        log.info('弹幕数量')
        return Response()

ns = api.namespace('video', description='视频分析')
ns.add_resource(Duration, '/duration')
ns.add_resource(Videos, '/videos')
ns.add_resource(Tname, '/tname')
ns.add_resource(Coin, '/coin')
ns.add_resource(Danmaku, '/danmaku')
