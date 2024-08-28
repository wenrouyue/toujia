#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/23 下午7:13
# @Author  : wenrouyue
# @File    : callback.py
from page.admin.admin_page import AdminPage
from page.child.child_page import childPage
from page.task.task_centre_page import TaskCentrePage
from page.user.my_page import MyPage


class Callback:
    def __init__(self):
        self.call_basks = [
            ["/start", AdminPage, AdminPage.botStart],
            ["test", AdminPage, AdminPage.botStart],
            ["我的", MyPage, MyPage.myInfo],
            ["任务", TaskCentrePage, TaskCentrePage.taskCentre],
            ["复制", childPage, childPage.copyBot],
            ["接收复制", childPage, childPage.getUserBotToken],


        ]

    def get_callbacks(self):
        return self.call_basks
