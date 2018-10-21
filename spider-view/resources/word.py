#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restplus.resource import Resource

from server.decorators import Response
from configs import api
from server.logger import log
from operations.word import WordOperation
from filters.word import WordFilter

class Sign(Resource):
    @staticmethod
    @WordFilter.filter_user_sign(result=list)
    @WordOperation.get_user_sign()
    def get():
        """签名词频统计"""
        log.info('签名词频统计')
        return Response()

class Name(Resource):
    @staticmethod
    @WordFilter.filter_user_name(result=list)
    @WordOperation.get_user_name()
    def get():
        """用户名词频统计"""
        log.info('用户名词频统计')
        return Response()

ns = api.namespace('word', description='词频统计')
ns.add_resource(Sign, '/sign')
ns.add_resource(Name, '/name')