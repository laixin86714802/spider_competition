
# 简介

爬虫: 使用scrapy异步爬虫获取b站用户, 视频, 关注等信息

后端: 使用flask微服务架构构建数据分析界面

前端: 使用bootstrap, echarts进行数据渲染

复杂网络: 使用network构架有向图, 展示用户和up之间的关注依赖

词频分析: 使用jieba,wordcloud模块, 分析用户签名的词频

**最近工作比较忙, 项目从零开始写, 勿急**

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
![](/server/static/images/15155175263081.png)