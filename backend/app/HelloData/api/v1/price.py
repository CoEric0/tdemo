from fastapi import APIRouter

router = APIRouter()

'''
Body 解包；
Post 方法相比get支持body，容量稍微大一点，安全性稍微高一点
'''
@router.post("/bb")
async def is_expensive(item: Item):
    price = item.price
    return {"item_name": item.name, "item_price": item.price, "is_expensive": price > 100}