#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.word import WordModel
from configs import db
from collections import Counter
import jieba.posseg as psg
import re
from wordcloud import WordCloud

def NameClouds():
    """用户名词云"""
    result = WordModel.get_user_name(db.spider)
    data = []
    text = ''
    for i in result:
        text += re.sub(r'[-,$\(\)#\+\&\*:：\.·`・|\s，。！/~\r\n=\!？、…_;\\—@\?（）～\']', '', i['sign'])
    seg_list = [x.word for x in psg.cut(text) if x.flag.startswith('n')]
    all_words = Counter(seg_list).most_common(200)
    for i, _ in all_words:
        data.append(i)
    cloud_text = ",".join(data)
    wc = WordCloud(
        background_color="white",
        max_words=200,
        font_path="C:/Windows/Fonts/STFANGSO.ttf",
        min_font_size=15,
        max_font_size=50,
        width=400
    )
    wc.generate(cloud_text)
    wc.to_file('../static/images/name_cloud.png')


if __name__ == '__main__':
    NameClouds()