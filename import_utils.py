#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 下午6:50
# @Author  : wenrouyue
# @File    : import_utils.py
from config.config import load_config
from utils.mysql_utils import DatabaseManager
from utils.redis_utils import RedisUtil
from log.logger import LoggerConfig
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

log = LoggerConfig(__name__).get_logger()
config = load_config()
redisUtils = RedisUtil(config["redis"]["host"], config["redis"]["port"], config["redis"]["password"],
                       config["redis"]["db"])
redisUtilsByTask = RedisUtil(config["redis"]["host"], config["redis"]["port"], config["redis"]["password"],
                             config["redis"]["taskDb"])


db = DatabaseManager()