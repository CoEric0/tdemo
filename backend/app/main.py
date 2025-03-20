from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

import sqlite3
from pathlib import Path

app = FastAPI()
DATA_BASE_PATH = Path(__file__).parent.parent / "data" / "lite.db"

'''
继承BaseModel,帮助fastapi识别为body
'''
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


'''
装饰器语法 指定路由
'''
@app.get("/")
async def read_root():
    '''
    字典语法，返回Json
    '''
    return {"Hello": "World"}


'''
动态路由，?关键字参数在函数中定义
'''
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    db = sqlite3.connect(DATA_BASE_PATH)
    cursor = db.cursor()

    sql = "select * from item_table where id = ?"

    value = (item_id,)
    cursor.execute(sql, value)
    
    item = cursor.fetchone() # 获取一条数据

    return {"item_id": item_id, "item": item}


'''
put方法，通过装饰器语句定义
引入Body
同一路由下可以有不同的方法
'''
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    '''
    引入item
    '''
    db = sqlite3.connect(DATA_BASE_PATH)
    cursor = db.cursor()

    sql = "insert into item_table(id, name, price, is_offer) values(?, ?, ?, ?)"

    value = (item_id, item.name, item.price, item.is_offer)
    cursor.execute(sql, value)

    db.commit() # 提交到数据库，而不是停留在内存中

    return {"item_name": item.name, "item_id": item_id}


'''
Body 解包；
Post 方法相比get支持body，容量稍微大一点，安全性稍微高一点
'''
@app.post("/bb")
async def is_expensive(item: Item):
    price = item.price
    return {"item_name": item.name, "item_price": item.price, "is_expensive": price > 100}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
