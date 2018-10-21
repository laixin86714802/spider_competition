#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs import api

from flask_restplus import fields

# 血缘关系请求值
graph_data_request = api.doc(params={
    'schedule_id': '调度id',
    'schedule_status': '调度状态: 0: 全部; 1: 正常; 2: 停止; 3: 运行中',
    'dependent_status': '调度依赖状态: 0: 全部; 1: 正常; 2: 停止',
    'show_type': '展示类型: 1: 关系图; 2:和弦图'
})

# 血缘关系返回值
graph_data_response_success = api.response(200, '成功', api.model('interface_response_success', {
    'state': fields.Integer(description=200),
    'msg': fields.String(description='成功'),
    'data': fields.Nested(model=api.model('response_data', {
        'data': fields.List(fields.Nested(model=api.model('data_response', {
            'id': fields.String(description='排序id'),
            'name': fields.Integer(description='调度id'),
            'category': fields.Integer(description='分组'),
            'symbolSize': fields.Integer(description='权重'),
            'x': fields.Integer(description='x轴坐标'),
            'y': fields.Integer(description='y轴坐标')
        }))),
        'links': fields.List(fields.Nested(model=api.model('links_response', {
            'source': fields.String(description='初始点'),
            'target': fields.Integer(description='结束点'),
            'lineStyle': fields.String(description='边样式')
        }))),
        'layout': fields.String('展示类型')
    }), description='关系数据')
}))