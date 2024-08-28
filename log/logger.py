#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/23 下午5:58
# @Author  : wenrouyue
# @File    : logger.py

import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


class CustomTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=False):
        super().__init__(filename, when, interval, backupCount, encoding, delay)
        self.baseFilename = filename

    def doRollover(self):
        self.stream.close()
        timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        new_filename = f"logs/info-{timestamp}.log"
        self.rotate(self.baseFilename, new_filename)
        self.stream = self._open()


class LoggerConfig:
    def __init__(self, name, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.log_file = "logs/info.log"

        # 创建文件处理器
        # file_handler = TimedRotatingFileHandler(
        #     self.log_file, when='H', interval=24, backupCount=14)
        # file_handler.setLevel(logging.ERROR)

        # 创建文件处理器，每分钟创建一个新文件
        file_handler = CustomTimedRotatingFileHandler(self.log_file, when='D', interval=1, backupCount=30)
        file_handler.setLevel(logging.INFO)

        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # 创建日志格式
        formatter = logging.Formatter('%(asctime)s %(filename)s/%(funcName)s-%(levelname)s-[%(lineno)d]行：%(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 添加处理器到日志器
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger
