*   [简介](#简介)
*   [数据库](#数据库)
    *   [建表语句](#建表语句)
    *   [部分爬取数据](#部分爬取数据)
*   [爬虫](#爬虫)
    *   [说明](#说明)
    *   [模块](#模块)
    *   [类图](#类图)
    *   [结果](#结果)
    *   [注](#注)
*   [可视化](#可视化)
    *   [说明](#说明)
    *   [接口页面](#接口页面)
    *   [数据库配置](#数据库配置)
    *   [启动](#启动)
    *   [类图](#类图)
    *   [词频分析](#词频分析)
    *   [复杂网络](#复杂网络)

# 简介

爬虫: 使用scrapy异步爬虫获取b站用户, 视频, 关注等信息

后端: 使用flask微服务架构构建数据分析界面

前端: 使用bootstrap, echarts进行数据渲染

复杂网络: 使用gephi构建, 展示用户和up之间的关注依赖

词频分析: 使用jieba,wordcloud模块, 分析用户签名的词频

**最近工作比较忙, 项目从零开始写, 勿急**

# 数据库
![](/img/mysql_power.png)

## 建表语句
`/sql/DDL.txt`

## 部分爬取数据
`/sql/data.sql`

# 爬虫

## 说明
* 目录: `/spider_execute`
* 语言: `python3.6.4`
* 依赖: `pip install requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/`
* 数据库配置: 修改`/spider_execute/spider_execute/setting.py`
```
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'spider'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
MYSQL_PORT = 3306
```
* 启动爬虫:
```
cd ./spider_execute
# 用户爬虫
scrapy crawl user
# 视频爬虫
scrapy crawl video
# 关注爬虫
scrapy crawl follow
# 粉丝爬虫
scrapy crawl fans
```

**安装依赖库可能出现安装失败的问题, 请手动在这里下载依赖包**

[Python模块](http://www.lfd.uci.edu/~gohlke/pythonlibs/ "Python模块")

## 模块
* items: 实体类容器
* middlewares: 下载器中间件是介于Scrapy的request/response处理的钩子框架。
* pipelines: 管道, 异步将爬取结果保存到数据库中
* settings: 全局配置文件
* spiders/user: B站用户爬虫
* spiders/video: B站视频爬虫
* spiders/follow: 用户关注爬虫
* spiders/fans: 用户粉丝爬虫

## 类图
![](/img/scrapy_class.png)

## 结果
![](/img/mysql_count.png)

## 注
B站最近更新了防爬策略, 对用户信息接口频繁请求将会封禁, 代码中使用了代理IP, 请运行时注意.

# 可视化
![](/img/flask_user.png)

分为用户、视频、词频和复杂网络四大板块及详细的数十个小块

## 说明
使用flask微服务架构, 前后端分离, 对于展示的数据采用不同的接口渲染, 使加载速度变快

## 接口页面
`http://localhost:2333/`
![](/img/interface.png)

## 数据库配置
修改`/spider-view/superconf.json`中
```
{
    "mysql": {
        "spider": {
            "host": "localhost",
            "port": 3306,
            "database": "",
            "user": "",
            "password": "",
            "maxConnections": 10
        }
    }
}
```

## 启动
```
cd ./spider-view
python server.py
```

## 类图
![](/img/flask_class.png)

## 词频分析
```
# 用户名词频分析
/spider-view/word_cloud/name_cloud.py
# 用户签名频分析
/spider-view/word_cloud/sign_cloud.py
```

## 复杂网络
使用gephi渲染用户关注关系
![](/img/graph.png)