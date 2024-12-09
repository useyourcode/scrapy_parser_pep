import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import SPIDER_NAME, ALLOWED_DOMAINS, START_URLS


class PepSpider(scrapy.Spider):
    name = SPIDER_NAME
    allowed_domains = [ALLOWED_DOMAINS]
    start_urls = [START_URLS]

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
