from fastapi import APIRouter

# api不接受数据库模型，只接受schema
# from app.HelloData.models.items import Item
from app.HelloData.schemas.items import GetItemDetail
from app.HelloData.services.price_service import price_service
from app.HelloData.services.items_service import item_service

from backend.common.response.response_schema import ResponseModel, response_base

router = APIRouter()

'''
Body 解包；
Post 方法相比get支持body，容量稍微大一点，安全性稍微高一点
'''
@router.post("/bb", summary="判断商品是否昂贵")
async def is_expensive(item: GetItemDetail) -> ResponseModel:
    return response_base.success(data=await price_service.is_expensive(item))
    
    
@router.get("/bb", summary="判断商品是否昂贵")
async def is_expensive(aitem_id: int) -> ResponseModel:
    item = await item_service.get(aitem_id)
    return response_base.success(data=await price_service.is_expensive(item))