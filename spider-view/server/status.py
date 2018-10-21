# coding=utf-8
# author=veficos


# API状态描述
APIStatus = {
    200: '成功',
    400: '参数错误',
    401: '未登录用户',
    403: '请求被拒绝',
    404: '未找到该资源',
    500: '服务器内部错误',
    503: '服务器超载'
}


def build_result(status, msg=None, data=None):
    if data:
        return {'status': status, 'msg': msg if msg else APIStatus[status], 'data': data}
    return {'status': status, 'msg': msg if msg else APIStatus[status]}


def make_result(status, msg=None, data=None):
    return {'status': status, 'msg': msg if msg else APIStatus[status], 'data': data}
