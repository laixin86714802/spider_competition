#!/usr/bin/env python
# -*- coding: utf-8 -*-

class WordModel(object):
    @staticmethod
    def get_user_sign(cursor):
        """获取用户签名"""
        command = '''
        SELECT sign
        FROM bilibili_user_info
        WHERE sign != ""
        LIMIT 100'''

        result = cursor.query(command)
        return result if result else []

    @staticmethod
    def get_user_name(cursor):
        """获取用户名"""
        command = '''
        SELECT `name`
        FROM bilibili_user_info
        WHERE `name` != ""
        LIMIT 100'''

        result = cursor.query(command)
        return result if result else []