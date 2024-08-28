#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/25 下午11:58
# @Author  : wenrouyue
# @File    : task_centre_page.py
from page.base_page import BasePage

from import_utils import *


class TaskCentrePage(BasePage):
    def __init__(self, botData, callbackQuery):
        super().__init__(botData, callbackQuery)

    async def taskCentre(self, url):
        if url:
            log.info(f"taskCentre 参数：{url}")
        self.getBotMessage()
        text = "<b>任务大厅</b>\n\n"
        await self.botMessage.st(text)
