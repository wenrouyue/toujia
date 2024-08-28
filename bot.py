#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/23 下午6:39
# @Author  : wenrouyue
# @File    : bot.py

from urllib.parse import urlencode

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import Message, CallbackQuery

from bot_router.router import Router, Input, Query
from utils import common
from import_utils import *

# Constants
RATE_LIMIT_COUNT = config["cache"]["RATE_LIMIT_COUNT"]
RATE_LIMIT_WINDOW = config["cache"]["RATE_LIMIT_WINDOW"]
cache = {}


async def is_rate_limited(user_id):
    # Redis Key 设计

    cache_key = f"rate_limit:{user_id}"
    # 通过 Redis 的 INCR 命令递增请求计数
    current_count = redisUtils.incr(cache_key)
    if current_count == 1:
        # 如果是第一次请求，设置过期时间
        redisUtils.expire(cache_key, RATE_LIMIT_WINDOW)
    if current_count > RATE_LIMIT_COUNT:
        log.info(f"用户 {user_id} 超过了速率限制.")
        return False
    log.info(f"用户 {user_id} 已发出 {current_count} 次请求.")
    return True


class FatherBot:
    def __init__(self, name=None, api_id=None, api_hash=None, token=None):
        self.token = token
        self.name = name
        self.api_id = api_id
        self.api_hash = api_hash
        self.router = Router()
        self.Input = Input()
        self.query = Query()
        self.config = load_config()
        if self.config["environment"] == "dev":
            log.info("开发环境，代理启动机器人")
            proxy = {
                "scheme": "socks5",
                "hostname": "127.0.0.1",
                "port": 10808
            }
            self.bot = Client(name=self.name,
                              api_id=self.api_id,
                              api_hash=self.api_hash,
                              bot_token=self.token,
                              proxy=proxy)
            self.add_handler(self.bot)
        else:
            log.info("服务器环境，无需代理启动机器人")
            self.bot = Client(name=self.name,
                              api_id=self.api_id,
                              api_hash=self.api_hash,
                              bot_token=self.token)
            self.add_handler(self.bot)

    def add_handler(self, bot: Client):
        bot.add_handler(MessageHandler(self.commod, filters.command(
            ["start", "help"]
        ) & filters.private))
        # app.add_handler()
        # app.add_handler(InlineQueryHandler(callback=self.Input))
        bot.add_handler(CallbackQueryHandler(callback=self.callback_query))
        # app.add_handler(ChatMemberUpdatedHandler(main_chat_member_update, ChatMemberUpdatedHandler.MY_CHAT_MEMBER))
        bot.add_handler(MessageHandler(filters=filters.private & filters.reply, callback=self.message))

    async def message(self, bot: Client, msg: Message):
        flag = await self.checkUser(msg.from_user.id)
        # chat_id = msg.chat.id
        # from_id = msg.from_user.id
        # chat_type = msg.chat.type
        log.info("message 接收消息了")
        log.info(msg)
        if flag and msg.reply_to_message:
            # 回复消息 监听成功
            if msg.text is not None:
                await self.Input.input(bot, msg)
            if msg.photo is not None:
                await self.Input.input(bot, msg)
        # elif is_manage:
        #     log.info("管理群组收到消息")
        #     await self.router.route("groupSearch", self.bot, message, "msg")
        # elif chat_type == "private":
        #     log.info("普通私聊")

    async def callback_query(self, bot: Client, call_back: CallbackQuery):
        if call_back.inline_message_id:
            flag = await self.checkUser(call_back.from_user.id)
            flag and await self.query.callback(call_back.data, bot, call_back)
        else:
            flag = await self.checkUser(call_back.message.chat.id)
            flag and await self.router.route(call_back.data, bot, call_back, "call_back")

    async def commod(self, bot: Client, msg: Message):
        # await self.router.route(msg.text, bot, msg, "msg")
        # 原始 message.text 可能是 "/start a_6465491111"
        parts = msg.text.split(maxsplit=1)
        command = parts[0]
        params = parts[1] if len(parts) > 1 else ""
        if params:
            query_params = urlencode({"param": params})
            formatted_msg = f"{command}?{query_params}"
        else:
            formatted_msg = f"{command}"
        await self.router.route(formatted_msg, bot, msg, "msg")

    async def checkUser(self, userId):
        is_ban = self.user_is_ban(userId)
        if is_ban:
            if await is_rate_limited(userId):
                return True
            else:
                await self.bot.send_message(userId, "操作频率太快了！请等待1分钟")
        else:
            await self.bot.send_message(userId, "您已经被拉黑，如有疑问联系管理员！")
        pass

    def user_is_ban(self, userId):
        bot_id = common.bot_get_id(self.bot)
        res = redisUtils.sismember(config["redisKey"]["userBlank"] + ":" + bot_id, userId)
        if res == 1:
            log.info(f"{userId}, is banned")
            return False
        return True


class ChildBot(FatherBot):
    def __init__(self, name=None, api_id=None, api_hash=None, token=None):
        super().__init__(name, api_id, api_hash, token)
