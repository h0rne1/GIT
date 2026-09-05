# Учёт складских товаров (warehouse-inventory)

Учебный проект курса *Git -> Linux -> Docker -> Docker Compose -> Архитектура -> Финальный проект*.

Консольное приложение для учёта товаров на складе: добавление, удаление, просмотр остатков и отчёт по товарам, которых осталось мало.

## Проектная тема

Тема: **учёт складских товаров**.

Выбрана как понятная предметная область для отработки Git-workflow: сущность «товар», операции прихода/расхода, отчётность — всё это удобно разбивать на отдельные ветки и коммиты, а в будущем можно расширять до полноценного REST API и контейнеризации (см. `api-plan.md`).

## Функциональность

- [x] Добавление товара на склад (`add`)
- [x] Удаление товара со склада (`remove`)
- [x] Просмотр списка товаров (`list`)
- [x] Отчёты по остаткам (команда `report`) — показывает товары с остатком ниже минимального порога

## Технологии

- Python 3
- Хранение данных в JSON-файле (`data/inventory.json`)
- `argparse` для интерфейса командной строки
- `pytest` для unit-тестов

## Установка и запуск

```bash
pip install -r requirements.txt

python main.py add A1 "Болты М6" Крепёж 120 --min-quantity 20
python main.py list
python main.py remove A1
python main.py report
```

## Структура проекта

```
warehouse-inventory/
  README.md
  project-notes.md
  api-plan.md
  requirements.txt
  src/
    models.py
    storage.py
    cli.py
    reports.py
  data/
    inventory.json
  tests/
    test_models.py
```

## Документация

- [project-notes.md](project-notes.md) — заметки и план разработки
- [api-plan.md](api-plan.md) — план REST API для будущих этапов курса
