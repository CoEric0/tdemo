
from app.HelloData.models.items import Item
from app.HelloData.schemas.items import CreateItemParam, UpdateItemParam
from sqlalchemy import select, update

# from database.db import create_db_session, SQLALCHEMY_DATABASE_URL

'''
在新版 sqlalchemy 中（1.4+），不再使用 query 等方法，改用 insert, update, delete, select 方法
'''

class ItemCRUD():
    async def get_item_by_id(self, session, item_id: int) -> Item | None:
        '''
        获取商品
        异步方法，异步调用
        '''
        # sql = "select * from item_table where id = ?"
        # value = (item_id,)

        
        # item = await db.query(Item).filter(Item.id == item_id).one_or_none()
        stmt = select(Item).where(Item.id == item_id)

        '''
        SELECT item_table.id, item_table.name, item_table.price, item_table.is_offer, item_table.created_time, item_table.updated_time 
        FROM item_table 
        WHERE item_table.id = :id_1
        '''
        item = await session.execute(stmt)
        item = item.scalar_one_or_none()

        return item
    
    async def create_item(self, session, item: CreateItemParam) -> None:
        '''
        创建商品
        实现数据库增加操作有较大不同
        不应该在此考虑商品重复的问题
        '''
        # sql = "insert into item_table(id, name, price, is_offer) values(?, ?, ?, ?)"
        # value = (item.id, item.name, item.price, item.is_offer)

        new_item = Item(name = item.name, price = item.price, is_offer = item.is_offer)
        # INSERT INTO item_table (name, price, is_offer) VALUES (:name, :price, :is_offer)

        session.add(new_item)
        await session.commit()

        # 最佳实践
        # if flush:
        #     await session.flush()
        # if commit:
        #     await session.commit()

    async def update_item(self, session, item_id: int, item: UpdateItemParam) -> int:
        '''
        更新商品
        不应该在此考虑商品不存在的问题
        '''
        # 转换为字典（只包含已设置的字段）
        update_data = item.model_dump(exclude_unset=True)

        # 更新商品
        stmt = update(Item).where(Item.id == item_id).values(**update_data)
        result = await session.execute(stmt)
        await session.commit()

        # 返回受影响的行数
        return result.rowcount


    
# 变量名 :类型 = 实例创建
item_dao : ItemCRUD = ItemCRUD() 