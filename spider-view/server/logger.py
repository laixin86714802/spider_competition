# coding=utf-8
# author=veficos

import logging
import os

fmt = '''{
    'level': %(levelname)s,
    'sys_name': %(name)s,
    'file_name': %(filename)s,
    'sys_module': %(module)s,
    'function': [%(pathname)s:%(funcName)s:%(lineno)d],
    'stack_trace': %(exc_text)s,
    'message': %(message)s,
    'time': %(asctime)s
}'''


def create_logger():
    logger = logging.getLogger('etl-server')
    logger.setLevel(logging.INFO)
    filename = os.getcwd() + '/log_file/spider.log'

    fh = logging.FileHandler(filename, mode='a', encoding='utf-8')
    # formatter = logging.Formatter(fmt={
    #     'level': '%(levelname)s',
    #     'sys_host': '%(hostname)s',
    #     'sys_name': '%(name)s',
    #     'sys_module': '%(module)s',
    #     'function': '[%(pathname)s:%(funcName)s:%(lineno)d]',
    #     'stack_trace': '%(exc_text)s'
    # })
    formatter = logging.Formatter(
        fmt=fmt,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

log = create_logger()