from fastapi import APIRouter

from app.HelloData.schemas.items import GetItemDetail, CreateItemParam, UpdateItemParam
from app.HelloData.services.items_service import item_service

from backend.common.response.response_schema import ResponseModel, ResponseSchemaModel, response_base

# from database.db import DB_engine as db


router = APIRouter()


# '''
# 动态路由，?关键字参数在函数中定义
# '''
@router.get("/items/{item_id}",summary="获取商品")
async def read_item(item_id: int) -> ResponseSchemaModel[GetItemDetail]:
    # 数据的传输在此处控制，dao 返回的 model 对象不影响在api接口返回 schema 对象
    item = await item_service.get(item_id)
    return response_base.success(data=item)

# '''
# put方法，通过装饰器语句定义
# 引入Body
# '''
@router.put("/items/create",summary="创建商品")
async def create_item(aitem: CreateItemParam) -> ResponseModel:
    await item_service.create(aitem)

    return response_base.success()

@router.put("/items/update/{aitem_id}",summary="更新商品")
async def update_item(aitem_id: int, aitem: UpdateItemParam) -> ResponseModel:
    cnt = await item_service.update(aitem_id, aitem)

    if cnt > 0:
        return response_base.success(data=cnt)
    else:
        return response_base.fail()