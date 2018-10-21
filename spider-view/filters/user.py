#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server.decorators import make_decorator

class UserFilter(object):
    @staticmethod
    @make_decorator
    def filter_user_sex(result):
        data = []
        for i in result:
            if i['sex'] == '':
                i['sex'] = '空'
            data.append({
                'name': i['sex'],
                'value': i['count']
            })
        return {'status': 200, 'msg': '成功', 'data': data}, 200

    @staticmethod
    @make_decorator
    def filter_user_regtime(result):
        date = []
        value = []
        for i in result:
            date.append(i['regtime'])
            value.append(i['count'])
        return {'status': 200, 'msg': '成功', 'data': {'date': date, 'value': value}}, 200

    @staticmethod
    @make_decorator
    def filter_user_birthday(result):
        data = []
        legend = []
        for i in result:
            legend.append(i['birthday'])
            data.append({
                'name': i['birthday'],
                'value': i['count']
            })
        return {'status': 200, 'msg': '成功', 'data': {'data': data, 'legend': legend}}, 200

    @staticmethod
    @make_decorator
    def filter_user_sign(result):
        length = []
        value = []
        for i in result:
            length.append(i['sign'])
            value.append(i['count'])
        return {'status': 200, 'msg': '成功', 'data': {'sign': length, 'value': value}}, 200

    @staticmethod
    @make_decorator
    def filter_user_level(result):
        data = []
        for i in result:
            data.append({
                'name': str(i['level']),
                'value': i['count']
            })
        return {'status': 200, 'msg': '成功', 'data': data}, 200

    @staticmethod
    @make_decorator
    def filter_user_article(result):
        label = []
        value = []
        for i in result:
            label.append(i['label'])
            value.append(i['count'])
        return {'status': 200, 'msg': '成功', 'data': {'label': label, 'value': value}}, 200

    @staticmethod
    @make_decorator
    def filter_user_fans(result):
        label = []
        value = []
        for i in result:
            label.append(i['label'])
            value.append(i['count'])
        return {'status': 200, 'msg': '成功', 'data': {'label': label, 'value': value}}, 200

    @staticmethod
    @make_decorator
    def filter_user_following(result):
        label = []
        value = []
        for i in result:
            label.append(i['following'])
            value.append(i['count'])
        return {'status': 200, 'msg': '成功', 'data': {'label': label, 'value': value}}, 200