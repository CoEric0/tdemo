
from app.HelloData.models.items import Item
from app.HelloData.schemas.items import ItemParam,OfferParam

from database.db import create_db_session, DB_engine, SQLALCHEMY_DATABASE_URL

class ItemCRUD( ):
    async def get_item_by_id(self, db, item_id: int) -> Item | None:
        '''
        获取商品
        异步方法，异步调用
        '''
        # sql = "select * from item_table where id = ?"
        # value = (item_id,)

        
        item = await db.query(Item).filter(Item.id == item_id).one_or_none()

        return item
    
    async def create_item(self, db, item: OfferParam) -> Item:
        # sql = "insert into item_table(id, name, price, is_offer) values(?, ?, ?, ?)"
        # value = (item.id, item.name, item.price, item.is_offer)

        new_item = Item(name = item.name, price = item.price, is_offer = item.is_offer)
        await db.add(new_item)
        await db.commit()

        return new_item

    
# 变量名 :类型 = 实例创建
item_dao : ItemCRUD = ItemCRUD() 