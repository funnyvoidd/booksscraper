# Books Scraper

Парсер для сбора данных о книгах с books.toscrape.com.

## Возможности

- Сбор всех книг каталога.
- Фильтрация по категории.
- Автоматический обход пагинации.
- Извлечение:
  - названия книги;
  - цены;
  - рейтинга;
  - наличия на складе;
  - ссылки на изображение.
- Экспорт данных в CSV.

## Используемые технологии

- Python 3
- requests
- BeautifulSoup4
- argparse
- csv

## Установка

```bash
git clone <repository-url>
cd books-scraper
pip install -r requirements.txt
```

## Запуск

Собрать все книги:

```bash
python scraper.py
```

Собрать книги категории Science:

```bash
python scraper.py --category "Science"
```

Собрать книги категории Travel:

```bash
python scraper.py --category "Travel"
```

## Результат

После завершения работы создаётся файл:

```text
books.csv
```

Пример структуры:

| title | price | rating | availability | image_url |
|---------|---------|---------|---------|---------|
| A Light in the Attic | £51.77 | 3 | In stock | https://... |

## Возможные улучшения

- Экспорт в Excel (.xlsx)
- Сохранение в SQLite/PostgreSQL
- Многопоточность
- Логирование
- Асинхронный парсинг (aiohttp)