import scrapy
from scrapy.spiders import Spider
from tutorial.items import ExItem

class ExSpider(scrapy.Spider):
    name = "ex"
    # allowed_domains = ["dmoz-odp.org"]
    start_urls = ["https://e-hentai.org/g/1380236/d00a0b2854/"]

    def parse(self, response):
        item = ExItem()
        name = response.xpath('//title//text()').extract()
        tags = response.xpath('//div[@id="taglist"]//tr')

        for tag in tags:
            item['parody'] = tag.re('"td_parody.*?"')
            self.logger.warning('--------------------------------')
            self.logger.warning(tag.re('"td_parody.*?"'))
            item['character'] = tag.re('"td_character.*?"')
            item['group'] = tag.re('"td_group.*?"')
            item['artist'] = tag.re('"td_artist.*?"')
            #item['parody'] = tag.re('"td_parody"')
            #item['parody'] = tag.re('"td_parody"')
            #item['parody'] = tag.re('"td_parody"')
            #item['parody'] = tag.re('"td_parody"')
            #item['parody'] = tag.re('"td_parody"')
            yield item
            
            

        # tr = response.xpath('//div[@id="taglist"]//tr')
        # for i in tr:
        #     print(tr)

        # filename = response.url.split("/")[-1] + '.html'
        # with open(filename, 'wb') as f:
        #    f.write(response.body)