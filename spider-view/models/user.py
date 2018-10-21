#!/usr/bin/env python
# -*- coding: utf-8 -*-

class UserModel(object):
    @staticmethod
    def get_user_sex(cursor):
        """获取用户性别"""
        command = '''
        SELECT sex, COUNT(*) AS count
        FROM bilibili_user_info
        GROUP BY sex'''

        result = cursor.query(command)
        return result if result else []

    @staticmethod
    def get_user_regtime(cursor):
        """获取用户注册时间"""
        command = '''
        SELECT FROM_UNIXTIME(regtime,'%Y-%m') AS regtime, COUNT(*) AS count
        FROM bilibili_user_info
        WHERE regtime != 0
        GROUP BY FROM_UNIXTIME(regtime,'%Y-%m')'''

        result = cursor.query(command)
        return result if result else []

    @staticmethod
    def get_user_birthday(cursor):
        """获取用户生日"""
        command = '''
        SELECT birthday, COUNT(*) AS count
        FROM bilibili_user_info
        WHERE birthday != ''
        GROUP BY birthday'''

        result = cursor.query(command)
        return result if result else []

    @staticmethod
    def get_user_sign(cursor):
        """获取用户签名"""
        command = '''
        SELECT LENGTH(sign) AS sign, COUNT(*) AS count
        FROM bilibili_user_info
        GROUP BY LENGTH(sign)'''

        result = cursor.query(command)
        return result if result else []

    @staticmethod
    def get_user_level(cursor):
        """获取用户签名"""
        command = '''
        SELECT `level`, COUNT(*) AS count
        FROM bilibili_user_info
        GROUP BY `level`'''

        result = cursor.query(command)
        return result if result else []

    @staticmethod
    def get_user_article(cursor):
        """获取用户文章观看次数"""
        command = '''
        SELECT '0-10000' AS label, COUNT(*) AS count
        FROM bilibili_user_info
        WHERE article >=0 AND article < 10000
        UNION ALL
        SELECT '10000-100000', COUNT(*)
        FROM bilibili_user_info
        WHERE article >=10000 AND article < 100000
        UNION ALL
        SELECT '>100000', COUNT(*)
        FROM bilibili_user_info
        WHERE article >=100000'''

        result = cursor.query(command)
        return result if result else []

    @staticmethod
    def get_user_fans(cursor):
        """获取用户粉丝数"""
        command = '''
        SELECT '0-1000' AS label, COUNT(*) AS count
        FROM bilibili_user_info
        WHERE fans >=0 AND fans < 1000
        UNION ALL
        SELECT '1000-5000', COUNT(*)
        FROM bilibili_user_info
        WHERE fans >=1000 AND fans < 5000
        UNION ALL
        SELECT '5000-10000', COUNT(*)
        FROM bilibili_user_info
        WHERE fans >=5000 AND fans < 10000
        UNION ALL
        SELECT '10000-100000', COUNT(*)
        FROM bilibili_user_info
        WHERE fans >=10000 AND fans < 100000
        UNION ALL
        SELECT '>100000', COUNT(*)
        FROM bilibili_user_info
        WHERE fans >=100000'''

        result = cursor.query(command)
        return result if result else []

    @staticmethod
    def get_user_following(cursor):
        """获取用户关注数"""
        command = '''
        SELECT following, COUNT(*) AS count
        FROM bilibili_user_info
        GROUP BY following'''

        result = cursor.query(command)
        return result if result else []