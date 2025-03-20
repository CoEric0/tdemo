'''
数据库引入
'''

import sqlite3
from pathlib import Path


def create_db_link():
    '''
    创建数据库连接
    '''
    path = Path(__file__).parent / "data" / "lite.db"

    return path


def create_db_session(url: str = None):
    '''
    创建数据库会话
    '''
    db = sqlite3.connect(url)
    return db

CurrentSession = create_db_session(create_db_link())


