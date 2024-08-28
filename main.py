#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/23 下午7:40
# @Author  : wenrouyue
# @File    : main.py
import asyncio
from bot import FatherBot
from import_utils import *


async def main():
    config = load_config()
    name = config["botFather"]["name"]
    api_id = config["key"]["api_id"]
    api_hash = config["key"]["api_hash"]
    token = config["botFather"]["token"]
    async with FatherBot(name, api_id, api_hash, token).bot as bot:
        try:
            await bot.run()
        except Exception as e:
            log.error(f"启动过程中发生错误: {e}")


if __name__ == '__main__':
    log.info("Bot开始启动")
    asyncio.run(main())
