from src.models import Item


def test_is_low_stock_true():
    item = Item(sku="A1", name="Болты М6", category="Крепёж", quantity=5, min_quantity=10)
    assert item.is_low_stock() is True


def test_is_low_stock_false():
    item = Item(sku="A2", name="Гайки М6", category="Крепёж", quantity=50, min_quantity=10)
    assert item.is_low_stock() is False


def test_to_dict_from_dict_roundtrip():
    item = Item(sku="A3", name="Шайбы", category="Крепёж", quantity=20, min_quantity=5)
    restored = Item.from_dict(item.to_dict())
    assert restored == item
