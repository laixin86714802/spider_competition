# coding=utf-8
# author=veficos

from configs import app
# 路由加载
from route import *
# 接口加载
from resources import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2333, debug=False)