from app.HelloData.cruds.items_crud import item_dao
from app.HelloData.models.items import Item
from app.HelloData.schemas.items import ItemParam,OfferParam

class ItemService:
    @staticmethod
    async def get(item_id: int) -> ItemParam:
        item = await item_dao.get_item_by_id(item_id)
        return item

    @staticmethod
    async def create(item: OfferParam) -> Item:
        item = await item_dao.create_item(item)
        return item