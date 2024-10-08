#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 下午5:42
# @Author  : wenrouyue
# @File    : toujia_user.py

import json
from typing import Any

from sqlalchemy import Column, String, func, DateTime

from mode.base_mode import BaseModel


class ToujiaUser(BaseModel):
    __tablename__ = 'toujia_user'  # 表名

    tg_id = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=True, comment='tg名字')
    user_name = Column(String(100), nullable=True, comment='tg用户名')
    vip_level = Column(String(100), default='0', comment='vip级别')
    vip_validity_time = Column(DateTime, nullable=True, comment='vip过期时间')
    is_block = Column(String(10), default='0', comment='0未拉黑 1已拉黑')
    is_delete = Column(String(10), default='0', comment='0未删除 1已删除')
    is_copy = Column(String(10), default='0', comment='0不能 1可以')

    # update_time = Column(DateTime, nullable=True, default=func.now(), onupdate=func.now(),
    #                      comment='更新时间')
    # create_time = Column(DateTime, nullable=True, default=func.now(), comment='创建时间')

    def __init__(self, tg_id, name, user_name, vip_level='0', is_block='0', is_delete='0', is_copy='0', **kw: Any):
        super().__init__(**kw)
        self.tg_id = tg_id
        self.name = name
        self.user_name = user_name
        self.vip_level = vip_level
        self.is_block = is_block
        self.is_delete = is_delete
        self.is_copy = is_copy

    def __repr__(self):
        return (f"<ToujiaUser(tg_id='{self.tg_id}', name='{self.name}', user_name='{self.user_name}', "
                f"vip_level='{self.vip_level}', vip_validity_time='{self.vip_validity_time}', "
                f"is_block='{self.is_block}', is_delete='{self.is_delete}', is_copy='{self.is_copy}', "
                f"update_time='{self.update_time}', create_time='{self.create_time}')>")

