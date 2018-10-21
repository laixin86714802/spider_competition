#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server.decorators import make_decorator

from collections import Counter
import jieba.posseg as psg
import re

class WordFilter(object):
    @staticmethod
    @make_decorator
    def filter_user_sign(result):
        data = []
        legend = []
        text = ''
        for i in result:
            text += re.sub(r'[-,$\(\)#\+\&\*:：\.·`・|\s，。！/~\r\n=\!？、…_;\\—@\?（）～\']', '', i['sign'])
        seg_list = [x.word for x in psg.cut(text) if x.flag.startswith('n')]
        all_words = Counter(seg_list).most_common(200)
        for i, j in all_words:
            legend.append(i)
            data.append({
                'name': i,
                'value': j
            })
        return {'status': 200, 'msg': '成功', 'data': {'legend': legend, 'data': data}}, 200

    @staticmethod
    @make_decorator
    def filter_user_name(result):
        data = []
        legend = []
        text = ''
        for i in result:
            text += re.sub(r'[-,$\(\)#\+\&\*:：\.·`・|\s，。！/~\r\n=\!？、…_;\\—@\?（）～\']', '', i['name'])
        seg_list = [x.word for x in psg.cut(text) if x.flag.startswith('n')]
        all_words = Counter(seg_list).most_common(200)
        for i, j in all_words:
            legend.append(i)
            data.append({
                'name': i,
                'value': j
            })
        return {'status': 200, 'msg': '成功', 'data': {'legend': legend, 'data': data}}, 200