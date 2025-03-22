from backend.common.model import Base
from sqlalchemy import String
from sqlalchemy import Mapped, mapped_column
from backend.common.model import id_key


# Base： 对象基类 from sqlalchemy.orm import declarative_base

# ORM：对象-关系映射，一个表对应一个类，表的字段对应类的属性，表的记录对应类的实体对象 
class Item(Base):
    '''
    商品表
    '''

    __tablename__ = "item_table"

    # 主键，一个id_key类型的 Mapped 映射列
    # Mapped 在新版本的 sqlalchemy 中被推荐使用，而非传统的 Column
    # init=False 表示不初始化, 多用于主键
    id: Mapped[id_key] = mapped_column(init=False)

    # 商品名称
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    # 商品价格
    price: Mapped[float] = mapped_column(nullable=False)

    # 是否打折
    is_offer: Mapped[bool] = mapped_column(nullable=False, default=False)

    # 创建者 修改者 创建时间 更新时间 从Base中继承
