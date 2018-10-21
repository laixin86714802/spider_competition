#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server.decorators import make_decorator, Response
from models.word import WordModel
from configs import db

class WordOperation(object):
    @staticmethod
    @make_decorator
    def get_user_sign():
        """获取用户签名"""
        result = WordModel.get_user_sign(db.spider)
        return Response(result=result)

    @staticmethod
    @make_decorator
    def get_user_name():
        """获取用户名"""
        result = WordModel.get_user_name(db.spider)
        return Response(result=result)