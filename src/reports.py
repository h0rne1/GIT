from typing import List

from .models import Item


def low_stock_report(items: List[Item]) -> List[Item]:
    """Возвращает товары, у которых остаток на складе <= минимального порога."""
    return [item for item in items if item.is_low_stock()]
