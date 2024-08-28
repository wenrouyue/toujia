#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/23 下午7:15
# @Author  : wenrouyue
# @File    : base_page.py
from typing import Optional, Union

from pyrogram import Client
from pyrogram.raw.types import Message
from pyrogram.types import CallbackQuery

from utils.bot_message import BotMessage


class BasePage:
    def __init__(self, bot_data=None, callbackQuery: Optional[Union[Message, CallbackQuery]] = None):
        self.baseMsg: Optional[Union[Message, CallbackQuery]] = None
        self.botMessage: Optional[BotMessage] = None
        self.botMessageByUser: Optional[BotMessage] = None
        if bot_data:
            self.bot: Optional[Client] = bot_data.get('bot')
            self.chatId = bot_data.get('chat_id')
            self.userId = bot_data.get('user_id')
            self.replyText = bot_data.get('reply_text')
            self.replyMsgId = bot_data.get('reply_msg_id')
            self.userName = bot_data.get('user_name')
            self.name = bot_data.get('name')
            self.baseMsg = callbackQuery
        # if isinstance(callbackQuery, Message):
        #     self.baseMsg = callbackQuery
        # elif isinstance(callbackQuery, CallbackQuery):
        #     self.baseMsg = callbackQuery
        # if callbackQuery and hasattr(callbackQuery, 'CallbackQuery'):
        #     self.callbackQuery = callbackQuery
        # elif callbackQuery:
        #     self.msg = callbackQuery

    def setAttributes(self, params):
        if params:
            for key, value in params.items():
                setattr(self, key, value)

    def getBotMessage(self, args=None):
        if args:
            self.botMessageByUser = BotMessage(self.bot, None, args)
            return self.botMessageByUser
        else:
            self.botMessage = BotMessage(self.bot,
                                         self.baseMsg)
            return self.botMessage
