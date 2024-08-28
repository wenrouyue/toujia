#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 下午5:22
# @Author  : wenrouyue
# @File    : mysql_utils.py
# import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.config import load_config

config = load_config()


class DatabaseManager:
    def __init__(self):
        self.DATABASE_URI = config["database"]["database_uri"]
        self.engine = create_engine(self.DATABASE_URI, pool_size=config["database"]["pool_size"],
                                    max_overflow=config["database"]["pool_size"], echo=True)
        self.SessionFactory = sessionmaker(bind=self.engine)
        self.session = self.SessionFactory()

    def add(self, obj):
        """ 添加对象到数据库并提交 """
        try:
            self.session.add(obj)
            self.session.commit()
            print("对象添加成功！")
        except Exception as e:
            self.session.rollback()
            print(f"添加对象时出错: {e}")
        finally:
            self.session.close()

    def update(self, obj):
        """ 更新对象并提交 """
        try:
            self.session.merge(obj)  # 使用 merge 来更新对象
            self.session.commit()
            print("对象更新成功！")
        except Exception as e:
            self.session.rollback()
            print(f"更新对象时出错: {e}")
        finally:
            self.session.close()

    def delete(self, obj):
        """ 删除对象并提交 """
        try:
            self.session.delete(obj)
            self.session.commit()
            print("对象删除成功！")
        except Exception as e:
            self.session.rollback()
            print(f"删除对象时出错: {e}")
        finally:
            self.session.close()