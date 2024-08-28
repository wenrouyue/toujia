#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 下午4:37
# @Author  : wenrouyue
# @File    : base_mode.py
# @Description :

from sqlalchemy import create_engine, Column, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    update_time = Column(DateTime, nullable=True, default=func.now(), onupdate=func.now(),
                         comment='更新时间')
    create_time = Column(DateTime, nullable=True, default=func.now(), comment='创建时间')
