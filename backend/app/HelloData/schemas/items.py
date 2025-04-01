from pydantic import ConfigDict
from datetime import datetime

from backend.common.schema import SchemaBase
'''
继承BaseModel,帮助fastapi识别为body
'''


class ItemSchemaBase(SchemaBase):
    name: str
    price: float
    is_offer: bool  = False

class CreateItemParam(ItemSchemaBase):
    pass

class UpdateItemParam(ItemSchemaBase):
    pass

# 响应模式
class GetItemDetail(ItemSchemaBase):
    # 父类继承，允许从SQLAlchemy对象属性创建模型实例
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_offer: bool
    created_time: datetime
    updated_time: datetime | None = None
    