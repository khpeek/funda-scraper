# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class NumberOfPagesSpider(CrawlSpider):
    name = "number_of_pages"
    allowed_domains = ["funda.nl"]

    def __init__(self, place='amsterdam'):
        self.start_urls = ["http://www.funda.nl/koop/%s/" % place]
        self.le_maxpage = LinkExtractor(allow=r'%s+p\d+' % self.start_urls[0])
        rules = (Rule(self.le_maxpage, ),)

    def parse(self, response):
        links = self.le_maxpage.extract_links(response)
        max_page_number = 0                                                 # Initialize the maximum page number
        for link in links:
            if link.url.count('/') == 6 and link.url.endswith('/'):         # Select only pages with a link depth of 3
                page_number = int(link.url.split("/")[-2].strip('p'))       # For example, get the number 10 out of the string 'http://www.funda.nl/koop/amsterdam/p10/'
                if page_number > max_page_number:
                    max_page_number = page_number                           # Update the maximum page number if the current value is larger than its previous value
        filename = "max_pages.txt"                         # File name with as prefix the place name
        with open(filename,'wb') as f:
            f.write('max_page_number = %s' % max_page_number)               # Write the maximum page number to a text file
