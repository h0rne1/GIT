import argparse

from .models import Item
from .storage import InventoryStorage
from .reports import low_stock_report


def cmd_add(args, storage: InventoryStorage):
    items = storage.load_items()
    items.append(
        Item(
            sku=args.sku,
            name=args.name,
            category=args.category,
            quantity=args.quantity,
            min_quantity=args.min_quantity,
        )
    )
    storage.save_items(items)
    print(f"Добавлен товар {args.sku} ({args.name}), кол-во: {args.quantity}")


def cmd_remove(args, storage: InventoryStorage):
    items = storage.load_items()
    remaining = [i for i in items if i.sku != args.sku]
    if len(remaining) == len(items):
        print(f"Товар с SKU {args.sku} не найден")
        return
    storage.save_items(remaining)
    print(f"Товар {args.sku} удалён со склада")


def cmd_list(args, storage: InventoryStorage):
    items = storage.load_items()
    if not items:
        print("Склад пуст")
        return
    for item in items:
        flag = " [МАЛО!]" if item.is_low_stock() else ""
        print(
            f"{item.sku:6} {item.name:20} {item.category:12} "
            f"кол-во={item.quantity}{flag}"
        )


def cmd_report(args, storage: InventoryStorage):
    items = storage.load_items()
    low = low_stock_report(items)
    if not low:
        print("Товаров с низким остатком нет")
        return
    print("Товары с низким остатком:")
    for item in low:
        print(
            f" - {item.sku} {item.name}: осталось {item.quantity} "
            f"(мин. {item.min_quantity})"
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="warehouse", description="Учёт складских товаров"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Добавить товар на склад")
    p_add.add_argument("sku")
    p_add.add_argument("name")
    p_add.add_argument("category")
    p_add.add_argument("quantity", type=int)
    p_add.add_argument("--min-quantity", type=int, default=0)
    p_add.set_defaults(func=cmd_add)

    p_remove = sub.add_parser("remove", help="Удалить товар со склада")
    p_remove.add_argument("sku")
    p_remove.set_defaults(func=cmd_remove)

    p_list = sub.add_parser("list", help="Показать все товары")
    p_list.set_defaults(func=cmd_list)

    p_report = sub.add_parser("report", help="Отчёт по товарам с низким остатком")
    p_report.set_defaults(func=cmd_report)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    storage = InventoryStorage()
    args.func(args, storage)
