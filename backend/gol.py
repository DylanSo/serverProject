# -*- coding: utf-8 -*-

def _init():  # 初始化
    global _global_dict
    _global_dict = {}


def set_value(key, value: int):
    # 定义一个全局变量
    _global_dict[key] = value


def get_value(key) -> int:
    # 获得一个全局变量
    return _global_dict[key]

