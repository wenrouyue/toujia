#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/25 下午11:55
# @Author  : wenrouyue
# @File    : my_page.py
from mode.toujia_user import ToujiaUser
from page.base_page import BasePage

from import_utils import *


class MyPage(BasePage):
    def __init__(self, botData, callbackQuery):
        super().__init__(botData, callbackQuery)

    async def myInfo(self, url):
        if url:
            log.info(f"myInfo 参数：{url}")
        self.getBotMessage()
        text = "<b>用户中心</b>\n\n"
        log.info(f'{config["redisKey"]["userSearchCount"]}  {self.userId}')
        count = redisUtilsByTask.hget(config["redisKey"]["userSearchCount"], self.userId)
        user = ToujiaUser(tg_id=self.userId, name=self.name, user_name=self.userName)
        db_user = db.session.query(ToujiaUser).filter_by(tg_id=self.userId).first()
        log.info(db_user)
        if db_user:
            if user.name == db_user.name and user.user_name == db_user.user_name:
                log.info("用户存在，并且name username未更改，本次不做处理")
            else:
                log.info("用户存在，name username更改，开始修改用户的数据")
                db_user.user_name = user.name
                db_user.user_name = user.user_name
                db.update(db_user)
        vip_validity_time = f"过期时间：{db_user.vip_validity_time}\b" if db_user.vip_validity_time else ""
        text += (f"{db_user.name}，您好！以下是您的个人信息！\n\n"
                 f"vip等级：{'非会员' if db_user.vip_level == '0' else '会员'}\n"
                 f"{vip_validity_time}"
                 f"复制机器人：{'无权限' if db_user.is_copy == '0' else '可复制'}\n"
                 f"转发次数：{count if count else '0'} 次")
        await self.botMessage.st(text)
