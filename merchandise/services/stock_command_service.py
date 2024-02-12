from merchandise.models import Merchandise, Stock


class StockCommandService:

    @staticmethod
    def create(merchandise: Merchandise) -> None:
        s = Stock.objects.all()
        print([o.merchandise.name for o in s])
        stock: Stock = Stock.create(merchandise=merchandise)
        stock.save()
