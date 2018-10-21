#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server.decorators import make_decorator, Response
from models.video import VideoModel
from configs import db

class VideoOperation(object):
    @staticmethod
    @make_decorator
    def get_video_duration():
        """视频时长"""
        result = VideoModel.get_video_duration(db.spider)
        return Response(result=result)

    @staticmethod
    @make_decorator
    def get_video_videos():
        """视频数量"""
        result = VideoModel.get_video_videos(db.spider)
        return Response(result=result)

    @staticmethod
    @make_decorator
    def get_video_tname():
        """视频分区"""
        result = VideoModel.get_video_tname(db.spider)
        return Response(result=result)

    @staticmethod
    @make_decorator
    def get_video_coin():
        """硬币数量"""
        result = VideoModel.get_video_coin(db.spider)
        return Response(result=result)

    @staticmethod
    @make_decorator
    def get_video_danmaku():
        """弹幕数量"""
        result = VideoModel.get_video_danmaku(db.spider)
        return Response(result=result)