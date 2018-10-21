#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server.decorators import make_decorator, Response
from models.user import UserModel
from configs import db

class UserOperation(object):
    @staticmethod
    @make_decorator
    def get_user_sex():
        """获取用户性别"""
        result = UserModel.get_user_sex(db.spider)
        return Response(result=result)

    @staticmethod
    @make_decorator
    def get_user_regtime():
        """获取用户注册时间"""
        result = UserModel.get_user_regtime(db.spider)
        return Response(result=result)

    @staticmethod
    @make_decorator
    def get_user_birthday():
        """获取用户生日"""
        result = UserModel.get_user_birthday(db.spider)
        return Response(result=result)

    @staticmethod
    @make_decorator
    def get_user_sign():
        """获取用户签名"""
        result = UserModel.get_user_sign(db.spider)
        return Response(result=result)

    @staticmethod
    @make_decorator
    def get_user_level():
        """获取用户等级"""
        result = UserModel.get_user_level(db.spider)
        return Response(result=result)

    @staticmethod
    @make_decorator
    def get_user_article():
        """获取用户文章观看次数"""
        result = UserModel.get_user_article(db.spider)
        return Response(result=result)

    @staticmethod
    @make_decorator
    def get_user_fans():
        """获取用户粉丝数"""
        result = UserModel.get_user_fans(db.spider)
        return Response(result=result)

    @staticmethod
    @make_decorator
    def get_user_following():
        """获取用户关注数"""
        result = UserModel.get_user_following(db.spider)
        return Response(result=result)