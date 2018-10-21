#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restplus.resource import Resource

from server.decorators import Response
from configs import api
from server.logger import log
from operations.user import UserOperation
from filters.user import UserFilter

class Sex(Resource):
    @staticmethod
    @UserFilter.filter_user_sex(result=list)
    @UserOperation.get_user_sex()
    def get():
        """性别"""
        log.info('获取用户性别')
        return Response()

class Regtime(Resource):
    @staticmethod
    @UserFilter.filter_user_regtime(result=list)
    @UserOperation.get_user_regtime()
    def get():
        """注册时间"""
        log.info('获取用户注册时间')
        return Response()

class Birthday(Resource):
    @staticmethod
    @UserFilter.filter_user_birthday(result=list)
    @UserOperation.get_user_birthday()
    def get():
        """生日"""
        log.info('获取用户生日')
        return Response()

class Sign(Resource):
    @staticmethod
    @UserFilter.filter_user_sign(result=list)
    @UserOperation.get_user_sign()
    def get():
        """签名"""
        log.info('获取用户签名')
        return Response()

class Level(Resource):
    @staticmethod
    @UserFilter.filter_user_level(result=list)
    @UserOperation.get_user_level()
    def get():
        """等级"""
        log.info('获取用户等级')
        return Response()

class Article(Resource):
    @staticmethod
    @UserFilter.filter_user_article(result=list)
    @UserOperation.get_user_article()
    def get():
        """文章观看次数"""
        log.info('获取用户文章观看次数')
        return Response()

class Fans(Resource):
    @staticmethod
    @UserFilter.filter_user_fans(result=list)
    @UserOperation.get_user_fans()
    def get():
        """粉丝数"""
        log.info('获取用户粉丝数')
        return Response()

class Following(Resource):
    @staticmethod
    @UserFilter.filter_user_following(result=list)
    @UserOperation.get_user_following()
    def get():
        """关注数"""
        log.info('获取用户粉丝数')
        return Response()


ns = api.namespace('user', description='用户分析')
ns.add_resource(Sex, '/sex')
ns.add_resource(Regtime, '/regtime')
ns.add_resource(Birthday, '/birthday')
ns.add_resource(Sign, '/sign')
ns.add_resource(Level, '/level')
ns.add_resource(Article, '/article')
ns.add_resource(Fans, '/fans')
ns.add_resource(Following, '/following')
