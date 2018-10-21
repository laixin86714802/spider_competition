# coding=utf-8
# author=veficos


from server.status import make_result, APIStatus
from flask_restful import abort
from flask_restful import request

# post put请求数据
def get_payload():
    payload = request.json
    if payload:
        return payload
    abort(400, **make_result(status=APIStatus[400], msg='缺少请求数据'))

# get delete请求数据
def get_arg(key, default=None):
    value = request.args.get(key, default)
    if value is not None:
        return value
    abort(400, **make_result(status=APIStatus[400], msg='缺少请求参数%s' % key))
