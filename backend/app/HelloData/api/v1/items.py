from fastapi import APIRouter
from database.db import CurrentSession as db


router = APIRouter()


'''
动态路由，?关键字参数在函数中定义
'''
@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
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
@router.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    '''
    引入item
    '''
    cursor = db.cursor()

    sql = "insert into item_table(id, name, price, is_offer) values(?, ?, ?, ?)"

    value = (item_id, item.name, item.price, item.is_offer)
    cursor.execute(sql, value)

    db.commit() # 提交到数据库，而不是停留在内存中

    return {"item_name": item.name, "item_id": item_id}