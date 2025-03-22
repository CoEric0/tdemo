from backend.common.schema import SchemaBase
from typing import Optional

'''
继承BaseModel,帮助fastapi识别为body
'''


class ItemSchemaBase(SchemaBase):
    name: str
    

class ItemParam(ItemSchemaBase):
    price: float
    
    
class OfferParam(ItemParam):
    # 额外字段

    # 可选的布尔值，默认为None
    is_offer: Optional[bool] = None