import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_links_peps = response.css(
            'section[id="index-by-category"] a.pep::attr(href)'
        ).getall()

        for pep_url in all_links_peps:
            yield response.follow(
                pep_url, callback=self.parse_pep
            )

    def parse_pep(self, response):
        header = response.css('h1.page-title::text').get().split(' – ')

        data = {
            'number': header[0][4:],
            'name': header[1],
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get(),
        }

        yield PepParseItem(data)
