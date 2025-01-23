#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/23 下午7:15
# @Author  : wenrouyue
# @File    : admin_page.py
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from import_utils import *
from mode.toujia_user import ToujiaUser
from page.base_page import BasePage


class AdminPage(BasePage):
    def __init__(self, botData, callbackQuery):
        super().__init__(botData, callbackQuery)

    async def botStart(self, url):
        if url:
            log.info(f"start 有参数。。。 进行处理：{url['param']}")
        self.getBotMessage()
        text = (
            f'💎 <b>{self.name}</b> 您好，欢迎使用超级神偷！\n\n本机器人可以转发禁止转发的公开频道链接！\n如果您只是普通用户无需大量转发本机器人完全免费！\n\n'
            f'如果您是频道主可操作下方按钮复制本机器人！\n为什么复制机器人？好处如下👇️\n\n'
            f'1️⃣ 实现专属机器人1对1服务！\n'
            f'2️⃣ 开启批量转发！\n'
            f'3️⃣ 转发限次数！\n'
            f'4️⃣ 支持指定转发到您的频道/群组！\n'
            f'5️⃣ 支持私密频道/群组下载(需要登录账户，介意勿用)！\n'
            f'6️⃣ 定时发布视频！(做频道必备)！')
        button_list = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="🧑‍💼 我的信息", callback_data="我的"),
             InlineKeyboardButton(text="💰️ 任务大厅", callback_data="任务"), ],
            [InlineKeyboardButton(text="✨️ 复制机器人", callback_data="复制"),
             InlineKeyboardButton(text="📑 使用教程", url="https://t.me/xxxx_bot"), ],
            [InlineKeyboardButton(text="🥱 聊天交友", url="https://t.me/xxxx_bot"),
             InlineKeyboardButton(text="👩‍💻 联系客服", url="https://t.me/xxxx_bot"), ],
        ])
        user = ToujiaUser(tg_id=self.userId, name=self.name, user_name=self.userName)
        db_user = db.session.query(ToujiaUser).filter_by(tg_id=self.userId).first()
        log.info(db_user)
        if db_user:
            if user.name == db_user.name and user.user_name == db_user.user_name:
                log.info("用户存在，并且name username未更改，本次不做处理")
            else:
                log.info("用户存在，name username更改，开始修改用户的数据")
                db_user.name = user.name
                db_user.user_name = user.user_name
                db.update(db_user)
        else:
            db.add(user)
        await self.botMessage.send(text, button_list)
