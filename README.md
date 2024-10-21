# PS06

# README для Парсера Светильников с divan.ru

## Описание проекта

Этот проект представляет собой парсер на базе Scrapy, предназначенный для извлечения информации о светильниках с сайта divan.ru. Парсер собирает следующие данные:

- Название светильника
- Цена
- Ссылка на страницу с подробной информацией о товаре

Парсер разработан с использованием Python и фреймворка Scrapy. Этот инструмент позволяет автоматически собирать данные с веб-страниц, что удобно для анализа ассортимента или цен.

## Структура проекта


divan_lighting_scraper/
│
├── spiders/                     
│   └── divan_lighting_spider.py  # Основной файл парсера
│
├── scrapy.cfg                    # Конфигурационный файл Scrapy
└── README.md                     # Документация проекта


## Установка и настройка

Клонируйте проект:


git clone https://github.com/your-username/divan_lighting_scraper.git
cd divan_lighting_scraper


Создайте и активируйте виртуальное окружение:


python -m venv venv
source venv/bin/activate  # Для Linux/MacOS
venv\Scripts\activate     # Для Windows


Установите зависимости:


pip install scrapy


## Запуск парсера

Для запуска парсера и сохранения результатов в CSV файл используйте следующую команду:


scrapy crawl divan_lighting -o lighting.csv


- `divan_lighting` – имя паука.
- `-o lighting.csv` – выводит результаты в файл lighting.csv в формате CSV.

## Описание кода

Основной код: `divan_lighting_spider.py`


import scrapy

class DivanLightingSpider(scrapy.Spider):
    name = "divan_lighting"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/osveshchenie"]

    def parse(self, response):
        items = response.css('div._Ud0k')

        for item in items:
            yield {
                'name': item.css('div.lsooF span::text').get(),
                'price': item.css('div.pY3d2 span::text').get(),
                'url': item.css('a').attrib['href']
            }


- `name`: Имя паука для выполнения команд Scrapy.
- `allowed_domains`: Ограничивает домены


, с которых можно собирать данные.
- `start_urls`: URL страницы для начала парсинга.
- `parse`: Основной метод для извлечения данных. Использует CSS селекторы для поиска информации о товарах.

## Возможные ошибки и решения

- Ошибки CSS селекторов: Если структура HTML сайта изменится, обновите CSS селекторы.
- Проблемы с доступом: Если сайт блокирует парсер, используйте middleware или установите пользовательский User-Agent:

python
custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/85.0.4183.102 Safari/537.36'
}


## Расширение проекта

- Добавление функциональности для других категорий: Новые категории можно добавить, изменив `start_urls`.
- Использование базы данных: Вместо вывода в CSV можно настроить вывод в SQLite или PostgreSQL.

## Лицензия

Этот проект лицензирован под лицензией MIT.

Этот README теперь включает инструкции по сохранению данных в CSV файл с использованием Scrapy.

