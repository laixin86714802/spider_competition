#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs import api

from flask_restplus import fields

# 接口列表请求值
interface_list_request = api.doc(params={
    'interface_id': '接口ID',
    'interface_type': '接口类型',
    'run_times': '运行次数',
    'total_times': '运行总次数',
    'run_type': '账期类型',
    'status': '接口状态'
})

# 接口状态返回值
interface_status_response_success = api.response(200, '成功', api.model('interface_response_success', {
    'state': fields.Integer(description=200),
    'msg': fields.String(description='成功'),
    'data': fields.Nested(model=api.model('response_data', {
        's': fields.List(fields.Nested(model=api.model('status_response', {
            'name': fields.String(description='描述'),
            'value': fields.Integer(description='数值')
        }))),
        'd': fields.List(fields.Nested(model=api.model('status_response', {
            'name': fields.String(description='描述'),
            'value': fields.Integer(description='数值')
        }))),
        'm': fields.List(fields.Nested(model=api.model('status_response', {
            'name': fields.String(description='描述'),
            'value': fields.Integer(description='数值')
        })))
    }), description='圆环图')
}))