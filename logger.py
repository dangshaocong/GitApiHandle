#-*- coding=utf-8 -*-
import os
import logging

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logs')

def get_logger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    fmt = logging.Formatter('%(asctime)s [%(levelname)s] - %(filename)s:%(lineno)d:%(funcName)s - %(message)s')

    fileH = logging.FileHandler('{path}/{name}.log'.format(path=path, name=name))
    fileH.setFormatter(fmt)
    fileH.setLevel(logging.DEBUG)

    errorH = logging.FileHandler('{path}/error.log'.format(path=path))
    errorH.setFormatter(fmt)
    errorH.setLevel(logging.ERROR)

    streamH = logging.StreamHandler()
    streamH.setFormatter(fmt)
    streamH.setLevel(logging.DEBUG)

    warnH = logging.FileHandler('{path}/warning.log'.format(path=path))
    warnH.setFormatter(fmt)
    warn_filter = logging.Filter()
    warn_filter.filter = lambda record: record.levelno == logging.WARNING
    warnH.addFilter(warn_filter)

    log.addHandler(fileH)
    log.addHandler(errorH)
    log.addHandler(streamH)
    log.addHandler(warnH)

    return log