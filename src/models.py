from dataclasses import dataclass


@dataclass
class Item:
    """Единица товара на складе."""

    sku: str
    name: str
    category: str
    quantity: int
    min_quantity: int = 0

    def is_low_stock(self) -> bool:
        """Остаток товара достиг минимального порога или ниже."""
        return self.quantity <= self.min_quantity

    def to_dict(self) -> dict:
        return {
            "sku": self.sku,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "min_quantity": self.min_quantity,
        }

    @staticmethod
    def from_dict(data: dict) -> "Item":
        return Item(**data)
