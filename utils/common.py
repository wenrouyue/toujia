#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/23 下午7:40
# @Author  : wenrouyue
# @File    : common.py
from datetime import datetime, date


def get_name(first_name, last_name):
    t = ""
    if first_name:
        t += first_name
    if last_name:
        t += last_name
    return t


# 机器人获取自己id
def bot_get_id(bot):
    return bot.bot_token.split(":")[0]


# 格式化时间字符串
def parse_datetime(dt):
    if isinstance(dt, datetime):
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(dt, date):
        return dt.strftime('%Y-%m-%d')
    return None
