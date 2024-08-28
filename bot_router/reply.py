#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/23 下午7:45
# @Author  : wenrouyue
# @File    : reply.py
from page.child.child_page import childPage


class Reply:
    def __init__(self):
        self.reply = [
            ["回复机器人TOKEN", childPage, childPage.userBotRun],
        ]

    def get_reply(self):
        return self.reply
