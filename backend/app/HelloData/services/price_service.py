from app.HelloData.models.items import Item

class PriceService:
    @staticmethod
    async def is_expensive(item: Item) -> bool:
        if item.price > 100:
            return True
        return False

price_service: PriceService = PriceService()
