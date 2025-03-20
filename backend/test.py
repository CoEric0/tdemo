import sqlite3

import os

DATA_BASE_PATH = "backend/app/data/lite.db"

if os.path.exists(DATA_BASE_PATH):
    db = sqlite3.connect(DATA_BASE_PATH)

# 创建游标对象
cursor = db.cursor()

# 创建表
# id 自增 主键
# name 文本
# price 浮点数
# is_offer 整数
sql = '''create table if not exists item_table
        (id integer primary key autoincrement, name text, price real, is_offer integer)'''


# 执行
try:
    # 执行sql
    cursor.execute(sql)
    # 提交事务
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭
finally:
    cursor.close()
    db.close()