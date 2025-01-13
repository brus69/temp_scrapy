import scrapy

class SitemapSpider(scrapy.Spider):
    name = 'sitemap_spider'
    allowed_domains = ['technix-rus.ru']
    sitemap_urls = ['https://technix-rus.ru/sitemap_filter.xml']  # Укажите URL вашего sitemap.xml

    def parse(self, response):
        """Метод для обработки главного sitemap.xml и сбора ссылок"""
        # Извлекаем все ссылки на страницы из файла sitemap.xml
        urls = response.xpath('//url/loc/text()').getall()

        for url in urls:
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        """Метод для обработки каждой страницы, извлекаемой из sitemap.xml"""
        yield {
            'url': response.url,
            'title': response.css('title::text').get(),
            'description': response.xpath('//meta[@name="description"]/@content').get(),
            'h1': response.css('h1::text').get(),
        }










