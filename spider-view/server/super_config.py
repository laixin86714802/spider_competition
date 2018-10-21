#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json

class Serialize(dict):
    """字典对象扩展"""
    def __init__(self, *args, **kwargs):
        super(Serialize, self).__init__(*args, **kwargs)

    def __getitem__(self, key, default=None):
        """键值读取"""
        if isinstance(self.get(key, None), dict):
            return Serialize(self.get(key))
        return self.get(key, default)

    def __getattr__(self, key):
        """属性读取"""
        return self.__getitem__(key)

    def __setitem__(self, key, value):
        """键值赋值"""
        super(Serialize, self).__setitem__(key, value)

    def __setattr__(self, key, value):
        """属性赋值"""
        self.__setitem__(key, value)


class SuperConf(object):
    """配置读写项"""
    def __init__(self, path, intend=4, *args, **kwargs):
        self.path = path
        self.intend = intend
        self.stack = []
        self._serialize = Serialize({})
        self.read()

    def __getitem__(self, key, default=None):
        """键值读取"""
        if isinstance(self._serialize.get(key, None), dict):
            return Serialize(self._serialize[key])
        return self._serialize[key]

    def __getattr__(self, key):
        """属性读取"""
        return self.__getitem__(key)

    def __setitem__(self, key, value):
        """键值赋值"""
        self._serialize[key] = value


    def dump(self):
        """格式化为json字符串"""
        self.parse(self._serialize, 0)
        return ''.join(self.stack)

    def read(self):
        """读取文件"""
        fr = open(self.path, 'r')
        self._serialize = json.loads(fr.read())


    def guarantee(self):
        """写入文件"""
        with open(self.path, 'w') as fw:
            fw.write(self.dump())

    def parse(self, o, level=0):
        """value对象转换"""
        if o is None:
            self.stack.append('null')
        elif o is True:
            self.stack.append('true')
        elif o is False:
            self.stack.append('false')
        elif isinstance(o, (int, float)):
            self.stack.append(str(o))
        elif isinstance(o, str):
            self.stack.append(self.str(o))
        elif isinstance(o, (list, tuple)):
            self.parse_list(o, level)
        elif isinstance(o, dict):
            self.parse_dict(o, level)
        elif isinstance(o, unicode):
            self.stack.append(self.unicode(o))
        else:
            raise Exception('invalid json type %s!' % o)

    def parse_list(self, a=None, level=0):
        """列表对象格式化"""
        self.stack.append('[')
        level += 1
        for item in a:
            self.stack.append(self.newline(self.intend, level))
            self.parse(item, level)
            self.stack.append(',')

        len(a) and self.stack.pop()
        self.stack.append(self.newline(self.intend, level-1) + ']')

    def parse_dict(self, o=None, level=0):
        """字典对象格式化"""
        self.stack.append('{')
        level += 1
        for key, value in o.items():
            self.stack.append(''.join([
                self.newline(self.intend, level),
                self.str(str(key)) + ': '
            ]))
            self.parse(value, level)
            self.stack.append(',')

        len(o) and self.stack.pop()
        self.stack.append(''.join([
            self.newline(self.intend, level - 1), '}'
        ]))

    @staticmethod
    def newline(intend, level):
        """新起一行"""
        return '\n' + ' ' * intend * level

    @staticmethod
    def str(s):
        """构造字符串"""
        return '"' + s + '"'

    @staticmethod
    def unicode(s):
        """编码字符串"""
        return u'"' + s + u'"'
