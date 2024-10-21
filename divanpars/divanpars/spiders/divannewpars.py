import scrapy

class DivanLightingSpider(scrapy.Spider):
    name = "divan_lighting"
    allowed_domains = ["divan.ru"]
    # URL страницы категории освещения
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        # Ищем все элементы освещения на странице
        items = response.css('div._Ud0k')  # Актуальный класс-контейнер

        for item in items:
            yield {
                'name': item.css('div.lsooF span::text').get(),
                'price': item.css('div.pY3d2 span::text').get(),
                'url': response.urljoin(item.css('a').attrib['href']),  # Полная ссылка
            }

