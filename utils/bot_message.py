#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/23 下午7:24
# @Author  : wenrouyue
# @File    : bot_message.py
import asyncio
from typing import Optional, Union

from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, Message, ForceReply, CallbackQuery
from import_utils import *


class BotMessage:
    def __init__(self, bot, msg, *args):
        self.bot: Optional[Client] = bot
        self.msg: Optional[Union[Message, CallbackQuery]] = msg
        # log.info(self.msg)
        if isinstance(self.msg, CallbackQuery):
            # callback消息
            self.chat_id = self.msg.message.chat.id
            self.msg_id = self.msg.message.id
        elif isinstance(self.msg, Message):
            self.chat_id = self.msg.chat.id
            self.msg_id = self.msg.id
        else:
            self.chat_id = args[0]

    async def send_again_reply(self, text, msg_id):
        try:
            text += f"\n\n消息id：{msg_id}"
            await self.bot.send_message(self.chat_id, text, reply_markup=ForceReply(selective=True),
                                        parse_mode=ParseMode.HTML)
        except Exception as e:
            log.info(e)
            log.info(f"BotMessage.send_again_reply 发送消息失败！text：{text}\nmsgId：{msg_id}")

    async def send_reply(self, text, msg_id=None):
        try:
            if msg_id:
                text += f"\n\n消息id：{msg_id}"
            else:
                text += f"\n\n消息id：{self.msg_id}"

            await self.bot.send_message(self.chat_id, text, reply_markup=ForceReply(selective=True),
                                        parse_mode=ParseMode.HTML)
        except Exception as e:
            log.info(e)
            log.info(f"BotMessage.send_reply 发送消息失败！text：{text}\nid：{msg_id}")

    async def st(self, text, del_flag=None, *args):
        try:
            send = self.chat_id
            if args:
                send = args[0]
            if del_flag != "del":
                await self.bot.send_message(send, text, parse_mode=ParseMode.HTML)
            else:
                sent_message = await self.bot.send_message(send, text, parse_mode=ParseMode.HTML)
                await self.delete_timeout(send, sent_message.id)
        except Exception as e:
            log.info(e)
            log.info(f"BotMessage.st 发送消息失败！text：{text}\ndel：{del_flag}\nargs：{args}")

    async def send(self, text, button_list, del_flag=None, *args):
        try:
            send = self.chat_id
            if args:
                send = args[0]
            # reply_markup = self.create_inline_keyboard(button_list)
            if del_flag != "del":
                await self.bot.send_message(send, text, reply_markup=button_list, parse_mode=ParseMode.HTML,
                                            disable_web_page_preview=True)
            else:
                sent_message = await self.bot.send_message(send, text, reply_markup=button_list,
                                                           parse_mode=ParseMode.HTML,
                                                           disable_web_page_preview=True)
                await self.delete_timeout(send, sent_message.id)
        except Exception as e:
            log.info(e)
            log.info(f"BotMessage.send 发送消息失败！text：{text}\nbuttonList：{button_list}\ndel：{del_flag}")

    async def delete_timeout(self, chat_id, message_id):
        await asyncio.sleep(5)
        try:
            await self.bot.delete_messages(chat_id, message_id)
        except Exception as e:
            log.info(e)

    async def send_order_photo(self, seller, text, qrcode_name, button_list=None):
        if button_list is None:
            button_list = []
        try:
            await self.bot.send_photo(self.chat_id, qrcode_name, caption=text,
                                      reply_markup=InlineKeyboardMarkup(button_list), parse_mode=ParseMode.HTML)
            log.info("这里创建订单后，需要10分钟后删除消息！")
        except Exception as e:
            log.info(e)

    async def delete_msg(self, chat_id, message_id):
        await self.bot.delete_messages(chat_id, message_id)

    # def create_inline_keyboard(self, button_list):
    #     inline_keyboard = [[InlineKeyboardButton(button['text'], callback_data=button[
    #         'callback_data']) if 'callback_data' in button else
    #                         InlineKeyboardButton(button['text'], url=button['url']) if 'url' in button else
    #                         InlineKeyboardButton(button['text'], switch_inline_query=button['switch_inline_query'])
    #                         for button in row] for row in button_list]
    #     return InlineKeyboardMarkup(inline_keyboard)

    async def answer(self, callback_query_id, text):
        try:
            await self.bot.answer_callback_query(callback_query_id, show_alert=True, text=text)
        except Exception as e:
            log.info(e)
