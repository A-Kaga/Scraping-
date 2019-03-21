import scrapy
import codecs
import json
import logging
from scrapy import Request
from scrapy.spiders import Spider
from scrapy.exporters import JsonItemExporter
from ex.items import ExItem


class ExSpider(scrapy.Spider):
    name = "ex"
    start_urls = "https://e-hentai.org/non-h/"
    # start_urls = ["https://e-hentai.org/g/1383690/847374c457/"]
    crawl_count = 0
    max_count = 5


    def start_requests(self):
        url = self.start_urls
        yield Request(url, callback=self.get_page, meta={'proxy': 'https://127.0.0.1:1080'})
    

    def get_page(self, response):
        pages = response.xpath('//td[@class="gl3c glname"]/@onclick').extract()
        for page in pages:
            page_url = page[-44:-3]
            yield Request(page_url, callback=self.parse)
        
        """ self.crawl_count += 1
        if self.crawl_count >= self.max_count:
            scrapy.exceptions.CloseSpider(reson='已达最大爬取限制')
        else:
            new_url = self.start_urls + str(self.crawl_count) + '/'
            yield Request(new_url, callback=self.get_page, meta={'proxy': 'https://127.0.0.1:1080'})
     """

    def parse(self, response):
        item = ExItem()
        left_table = response.xpath('//*[@id="gdd"]//td/text()').extract()
        tags = response.xpath('//div[@id="taglist"]//tr')

        for tag in tags:
            item['name'] = response.xpath('//h1/text()').extract()
            item['posted'] = left_table[1]
            item['language'] = left_table[7].split(' ')[0]
            item['favorited'] = left_table[-1].split(' ')[0]
            item['rating_counts'] = response.xpath('//*[@id="rating_count"]/text()').extract()
            item['rating_average'] = response.xpath('//*[@id="rating_label"]/text()').extract()[0].split(' ')[-1]

            item['url'] = response.url.split('/')[-3] + response.url.split('/')[-2]
            item['parody'] = tag.re('"td_parody.*?"')
            item['character'] = tag.re('"td_character.*?"')
            item['group'] = tag.re('"td_group.*?"')
            item['artist'] = tag.re('"td_artist.*?"')
            item['female'] = tag.re('"td_female.*?"')
            yield item