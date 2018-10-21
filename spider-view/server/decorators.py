# coding=utf-8
# author=veficos

import functools

# 接口返回对象
class Response(dict):
    def __init__(self, *args, **kwargs):
        super(Response, self).__init__(*args, **kwargs)

# 封装装饰器
def make_decorator(f):
    def input_params(**params):
        restriction = {}
        values = {}
        for name in params:
            typ = params[name]
            try:
                isinstance(0, typ)
                restriction.update({name: typ})
            except:
                values.update({name: typ})

        def accept_func(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_result = func(*args, **kwargs)
                if not isinstance(last_result, Response):
                    raise Exception('the {func_name} return value must be a Response'.format(func_name=func.__name__))

                next_params = {}
                for k in restriction:
                    value = last_result.get(k, None)
                    if value is None:
                        raise Exception("{func_name} missing 1 required positional argument: {key}".format(func_name=f.__name__, key=k))

                    if not isinstance(value, restriction[k]):
                        raise Exception('{key} must be a {typ}'.format(key=k, typ=restriction[k].__name__))
                    next_params[k] = value

                if values:
                    next_params.update(values)
                return f(**next_params)
            return wrapper
        return accept_func

    return input_params

# 字典对象扩展
class DictModel(dict):
    def __init__(self, *args, **kwargs):
        super(DictModel, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        try:
            value = self[key]
            if type(value) == dict:
                value = self[key] = DictModel(value)
                return value
            return value
        except KeyError:
            raise AttributeError(r'"DictModel" object has no attribute "%s"' % key)

    def __setattr__(self, key, value):
        self[key] = value