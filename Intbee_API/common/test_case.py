# -*- coding: utf-8 -*-
# Created by apple on 2017/2/16.

import inspect
from unittest import TestCase
from modulefinder import Module


def iter_test_case_class(module: Module):
    """
    枚举module的所有TestCase子类
    :param module:
    :return:
    """
    return [obj for obj in vars(module).values() if inspect.isclass(obj) and issubclass(obj, TestCase)]
