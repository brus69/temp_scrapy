import scrapy
from urllib.parse import urljoin
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class TechnixSpider(CrawlSpider):
    name = "technix"
    allowed_domains = ["technix-rus.ru"]
    start_urls = ["https://technix-rus.ru/"]

    # Правила для извлечения ссылок и парсинга страниц
    rules = (
        Rule(LinkExtractor(), callback="parse_page", follow=True),
    )

    def parse_page(self, response):
        # Извлекаем данные с каждой страницы
        title = response.xpath('//title/text()').get()
        description = response.xpath('//meta[@name="description"]/@content').get()
        h1 = response.xpath('//h1/text()').get()
        url = response.url
        status_code = response.status

        yield {
            'URL': url,
            'Title': title or 'Нет заголовка',
            'Description': description or 'Нет описания',
            'H1': h1 or 'Нет H1',
            'Response Code': status_code,
        }

