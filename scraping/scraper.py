import scrapy


class AllocineSpider(scrapy.Spider):
    name = "allocine_spider"
    start_urls = ['http://www.allocine.fr/films/']

    def parse(self, response):
        SET_SELECTOR = '.hred'
        for film in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h2 a ::text'
            yield {
                'name': film.css(NAME_SELECTOR).extract_first(),
            }
            pass
