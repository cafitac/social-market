from merchandise.models import Merchandise, Stock


class StockCommandService:

    @staticmethod
    def create(merchandise: Merchandise) -> None:
        s = Stock.objects.all()
        stock: Stock = Stock.create(merchandise=merchandise)
        stock.save()
