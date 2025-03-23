from app.HelloData.cruds.items_crud import item_dao
from app.HelloData.models.items import Item
from app.HelloData.schemas.items import ItemParam,OfferParam
from database.db import async_db_session

class ItemService:
    @staticmethod
    async def get(aitem_id: int) -> Item:
        async with async_db_session() as db:
            item = await item_dao.get_item_by_id(db, aitem_id)
            if not item:
                raise Exception("Item not found")
        return item

    @staticmethod
    async def create(aitem: OfferParam) -> Item:
        async with async_db_session() as db:
            item = await item_dao.create_item(db, aitem)
        return item


item_service: ItemService = ItemService()