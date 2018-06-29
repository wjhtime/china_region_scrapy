import scrapy
from region.items import RegionItem
import os

class regionSpider(scrapy.Spider):

    name = "region"

    # allowed_domains = ['www.stats.gov.cn']

    start_urls = [
        "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/"
    ]

    def parse(self, response):
        for sel in  response.xpath("//tr[@class='provincetr']/td/a"):
            item = RegionItem()
            item['name'] = sel.xpath('text()').extract_first()
            item['url'] = self.start_urls[0] + sel.xpath('@href').extract_first()
            item['code'] = os.path.splitext(sel.xpath('@href').extract_first())[0]
            item['p_code'] = 0
            item['level'] = 1
            yield item
            yield scrapy.Request(item['url'], callback=self.parseCity, meta=item)


    def parseCity(self, response):
        for sel in  response.xpath("//tr[@class='citytr']"):
            item = RegionItem()
            item['name'] = sel.xpath('td[2]/a/text()').extract_first()
            item['url'] =  os.path.dirname(response.meta['url']) + '/' + sel.xpath('td[1]/a/@href').extract_first()
            item['code'] = sel.xpath('td[1]/a/text()').extract_first()
            item['p_code'] = response.meta['code']
            item['level'] = 2
            yield item
            yield scrapy.Request(item['url'], callback=self.parseCounty, meta=item)

    def parseCounty(self, response):
        for sel in  response.xpath("//tr[@class='countytr']"):
            item = RegionItem()
            item['name'] = sel.xpath('td[2]/a/text()').extract_first() or sel.xpath('td[2]/text()').extract_first()
            item['url'] = os.path.dirname(response.meta['url']) + '/' + (sel.xpath('td[1]/a/@href').extract_first() or '')
            item['code'] = sel.xpath('td[1]/a/text()').extract_first() or sel.xpath('td[1]/text()').extract_first()
            item['p_code'] = response.meta['code']
            item['level'] = 3
            yield item
            yield scrapy.Request(item['url'], callback=self.parseTown, meta=item)

    def parseTown(self, response):
        for sel in  response.xpath("//tr[@class='towntr']"):
            item = RegionItem()
            item['name'] = sel.xpath('td[2]/a/text()').extract_first() or sel.xpath('td[2]/text()').extract_first()
            item['url'] = os.path.dirname(response.meta['url']) + '/' + (sel.xpath('td[1]/a/@href').extract_first() or '')
            item['code'] = sel.xpath('td[1]/a/text()').extract_first() or sel.xpath('td[1]/text()').extract_first()
            item['p_code'] = response.meta['code']
            item['level'] = 4
            yield item
            yield scrapy.Request(item['url'], callback=self.parseVillage, meta=item)

    def parseVillage(self, response):
        for sel in response.xpath("//tr[@class='villagetr']"):
            item = RegionItem()
            item['name'] = sel.xpath('td[3]/text()').extract_first()
            item['url'] = ''
            item['code'] = sel.xpath('td[1]/text()').extract_first()
            item['p_code'] = response.meta['code']
            item['level'] = 5
            yield item