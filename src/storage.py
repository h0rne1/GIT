import json
from pathlib import Path
from typing import List

from .models import Item

DEFAULT_DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "inventory.json"


class InventoryStorage:
    """Хранилище остатков склада в JSON-файле."""

    def __init__(self, data_file: Path = DEFAULT_DATA_FILE):
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.data_file.exists():
            self._write([])

    def _read(self) -> List[dict]:
        with open(self.data_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, items: List[dict]) -> None:
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)

    def load_items(self) -> List[Item]:
        return [Item.from_dict(d) for d in self._read()]

    def save_items(self, items: List[Item]) -> None:
        self._write([item.to_dict() for item in items])
