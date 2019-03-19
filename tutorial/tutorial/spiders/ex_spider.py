import scrapy
import codecs
import json
from scrapy import Request
from scrapy.spiders import Spider
from scrapy.exporters import JsonItemExporter
from tutorial.items import ExItem


class ExSpider(scrapy.Spider):
    name = "ex"
    # allowed_domains = ["dmoz-odp.org"]
    start_urls = ["https://e-hentai.org/non-h/"]
    # start_urls = ["https://e-hentai.org/g/1383690/847374c457/"]


    def start_requests(self):
        url = self.start_urls[0]
        yield Request(url, callback=self.get_page, meta={'proxy': 'https://127.0.0.1:1080'})
    

    def get_page(self, response):
        pages = response.xpath('//div[@class="it5"]/a/@href').extract()
        for page in pages:
            yield Request(page, callback=self.parse)
    

    def parse(self, response):
        item = ExItem()
        # name = response.xpath('//title//text()').extract()
        tags = response.xpath('//div[@id="taglist"]//tr')

        for tag in tags:
            item['url'] = response.url.split('/')[-3] + response.url.split('/')[-2]
            item['parody'] = tag.re('"td_parody.*?"')
            item['character'] = tag.re('"td_character.*?"')
            item['group'] = tag.re('"td_group.*?"')
            item['artist'] = tag.re('"td_artist.*?"')
            item['female'] = tag.re('"td_female.*?"')
            #item['parody'] = tag.re('"td_parody"')
            #item['parody'] = tag.re('"td_parody"')
            #item['parody'] = tag.re('"td_parody"')
            #item['parody'] = tag.re('"td_parody"')
            yield item
        
        # print("********************")        
        # print("********************")
        # print(item['female'])
        # print("********************")
        # print("********************")