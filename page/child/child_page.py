#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 下午7:38
# @Author  : wenrouyue
# @File    : child_page.py
# @Description :
from pyrogram.raw.types import message

# from bot import ChildBot
from page.base_page import BasePage
from import_utils import *


class childPage(BasePage):

    def __init__(self, botData, callbackQuery):
        super().__init__(botData, callbackQuery)

    async def copyBot(self, url):
        if url:
            log.info(f"copyBot 参数：{url}")
        self.getBotMessage()
        text = "<b>子机器人管理</b>\n\n"
        button_list = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="🧑‍💼 复制机器人", callback_data="接收复制")],
        ])
        await self.botMessage.send(text, button_list)

    async def getUserBotToken(self, url):
        if url:
            log.info(f"getUserBotToken 参数：{url}")
        self.getBotMessage()
        await self.botMessage.send_reply("回复机器人TOKEN")

    async def userBotRun(self):
        log.info(self.baseMsg)
        log.info(self.baseMsg.text)
        from bot import ChildBot
        api_id = config["key"]["api_id"]
        api_hash = config["key"]["api_hash"]
        async with ChildBot('child', api_id, api_hash, self.baseMsg.text).bot as bot:
            await bot.run()
