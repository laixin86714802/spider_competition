#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server.decorators import make_decorator

class VideoFilter(object):
    @staticmethod
    @make_decorator
    def filter_video_duration(result):
        duration = []
        value = []
        for i in result:
            duration.append(i['duration'])
            value.append(i['count'])
        return {'status': 200, 'msg': '成功', 'data': {'duration': duration, 'value': value}}, 200

    @staticmethod
    @make_decorator
    def filter_video_videos(result):
        data = []
        legend = []
        for i in result:
            legend.append(str(i['videos']))
            data.append({
                'name': str(i['videos']),
                'value': i['count']
            })
        return {'status': 200, 'msg': '成功', 'data': {'data': data, 'legend': legend}}, 200

    @staticmethod
    @make_decorator
    def filter_video_tname(result):
        data = []
        legend = []
        for i in result:
            if i['tname'] == '':
                i['tname'] = '空'
            legend.append(i['tname'])
            data.append({
                'name': i['tname'],
                'value': i['count']
            })
        return {'status': 200, 'msg': '成功', 'data': {'data': data, 'legend': legend}}, 200

    @staticmethod
    @make_decorator
    def filter_video_coin(result):
        coin = []
        value = []
        for i in result:
            coin.append(i['coin'])
            value.append(i['count'])
        return {'status': 200, 'msg': '成功', 'data': {'coin': coin, 'value': value}}, 200

    @staticmethod
    @make_decorator
    def filter_video_danmaku(result):
        danmaku = []
        value = []
        for i in result:
            danmaku.append(i['danmaku'])
            value.append(i['count'])
        return {'status': 200, 'msg': '成功', 'data': {'danmaku': danmaku, 'value': value}}, 200