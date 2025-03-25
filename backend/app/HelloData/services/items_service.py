from app.HelloData.cruds.items_crud import item_dao
from app.HelloData.models.items import Item
from app.HelloData.schemas.items import CreateItemParam, UpdateItemParam
from backend.common.exception import errors

from database.db import async_db_session

class ItemService:
    @staticmethod
    async def get(aitem_id: int) -> Item:
        async with async_db_session() as db:
            item = await item_dao.get_item_by_id(db, aitem_id)
            if not item:
                raise errors.NotFoundError(msg="商品不存在")
        return item

    @staticmethod
    async def create(aitem: CreateItemParam) -> None:
        async with async_db_session() as db:
            # 重复检查等其他逻辑可以放在此处
            # name = await item_dao.get_by_title(db, aitem.name) ...
            await item_dao.create_item(db, aitem)

    @staticmethod
    async def update(aitem_id: int, aitem: UpdateItemParam) -> int:
        async with async_db_session() as db:
            # 多种业务逻辑
            item = await item_dao.get_item_by_id(db, aitem_id)
            if not item:
                raise errors.NotFoundError(msg="商品不存在")
            # if item.name != aitem.name:
            #     if await item_dao.get_item_by_name(db, aitem.name):
            #         raise errors.NotFoundError(msg="商品名称已存在")

            # 更新商品
            cnt = await item_dao.update_item(db, aitem_id, aitem)
            return cnt


item_service: ItemService = ItemService()