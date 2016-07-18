import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from funda.items import FundaItem

class FundaSoldSpider(CrawlSpider):

    name = "funda_spider_sold"
    allowed_domains = ["funda.nl"]

    def __init__(self, place='amsterdam'):
        self.start_urls = ["http://www.funda.nl/koop/verkocht/%s/p%s/" % (place, page_number) for page_number in range(1,1001)]
        # self.start_urls = ["http://www.funda.nl/koop/verkocht/%s/p1/" % place]  # For testing, extract just from one page
        self.base_url = "http://www.funda.nl/koop/verkocht/%s/" % place
        self.le1 = LinkExtractor(allow=r'%s+(huis|appartement)-\d{8}' % self.base_url)
        self.le2 = LinkExtractor(allow=r'%s+(huis|appartement)-\d{8}.*/kenmerken/' % self.base_url)

    def parse(self, response):
        links = self.le1.extract_links(response)
        slash_count = self.base_url.count('/')+1        # Controls the depth of the links to be scraped
        for link in links:
            if link.url.count('/') == slash_count and link.url.endswith('/'):
                item = FundaItem()
                item['url'] = link.url
                if re.search(r'/appartement-',link.url):
                    item['property_type'] = "apartment"
                elif re.search(r'/huis-',link.url):
                    item['property_type'] = "house"
                yield scrapy.Request(link.url, callback=self.parse_dir_contents, meta={'item': item})

    def parse_dir_contents(self, response):
        new_item = response.request.meta['item']
        title = response.xpath('//title/text()').extract()[0]
        postal_code = re.search(r'\d{4} [A-Z]{2}', title).group(0)
        address = response.xpath('//h1/text()').extract()[0].strip()
        price_span = response.xpath("//span[contains(@class, 'price-wrapper' )]/span[contains(@class, 'price' )]/text()").extract()[0]
        price = re.findall(r'\d+.\d+',price_span)[0].replace('.','')
        posting_date = response.xpath("//span[contains(@class, 'transaction-date') and contains(.,'Aangeboden sinds')]/strong/text()").extract()[0]
        sale_date = response.xpath("//span[contains(@class, 'transaction-date') and contains(.,'Verkoopdatum')]/strong/text()").extract()[0]

        new_item['postal_code'] = postal_code
        new_item['address'] = address
        new_item['price'] = price
        new_item['posting_date'] = posting_date
        new_item['sale_date'] = sale_date

        links = self.le2.extract_links(response)
        slash_count = self.base_url.count('/') + 2
        proper_links = filter(lambda link: link.url.count('/')==slash_count and link.url.endswith('/'), links)

        yield scrapy.Request(proper_links[0].url, callback=self.parse_details, meta={'item': new_item})

    def parse_details(self, response):
        new_item = response.request.meta['item']

        year_built_td = response.xpath("//th[contains(.,'Bouwjaar')]/following-sibling::td[1]/span/text()").extract()[0]
        year_built = re.findall(r'\d{4}',year_built_td)[0]
        area_td = response.xpath("//th[contains(.,'woonoppervlakte')]/following-sibling::td[1]/span/text()").extract()[0]
        area = re.findall(r'\d+',area_td)[0]
        rooms_td = response.xpath("//th[contains(.,'Aantal kamers')]/following-sibling::td[1]/span/text()").extract()[0]
        rooms = re.findall('\d+ kamer',rooms_td)[0].replace(' kamer','')
        bedrooms = re.findall('\d+ slaapkamer',rooms_td)[0].replace(' slaapkamer','')

        new_item['year_built'] = year_built
        new_item['area'] = area
        new_item['rooms'] = rooms
        new_item['bedrooms'] = bedrooms

        yield new_item
