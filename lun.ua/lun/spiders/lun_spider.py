import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import os

from ..items import LunItem


class MySpider(CrawlSpider):
    name = 'lun_town'
    allowed_domains = ['lun.ua']
    start_urls = ['https://lun.ua/uk/котеджі/київ',
                  'https://lun.ua/uk/котеджі/київська-обл',
                  'https://lun.ua/uk/котеджі/львів',
                  'https://lun.ua/uk/котеджі/вінниця',
                  'https://lun.ua/uk/котеджі/дніпро',
                  'https://lun.ua/uk/котеджі/житомир',
                  'https://lun.ua/uk/котеджі/луцьк',
                  'https://lun.ua/uk/котеджі/миколаїв',
                  'https://lun.ua/uk/котеджі/полтава',
                  'https://lun.ua/uk/котеджі/рівне',
                  'https://lun.ua/uk/котеджі/тернопіль',
                  'https://lun.ua/uk/котеджі/ужгород',
                  'https://lun.ua/uk/котеджі/харків',
                  'https://lun.ua/uk/котеджі/чернівці',
                  'https://lun.ua/uk/котеджі/івано-франківськ',
                  'https://lun.ua/uk/котеджі/хмельницький',
                  'https://lun.ua/uk/котеджі/суми',
                  'https://lun.ua/uk/котеджі/херсон',
                  'https://lun.ua/uk/котеджі/черкаси',
                  'https://lun.ua/uk/котеджі/чернігів',
                  'https://lun.ua/uk/котеджі/запоріжжя',
                  'https://lun.ua/uk/котеджі/кропивницький',
                  'https://lun.ua/uk/котеджі/одеса',
                  'https://lun.ua/uk/котеджі/київ?page=2',
                  'https://lun.ua/uk/котеджі/київ?page=3',
                  'https://lun.ua/uk/котеджі/київ?page=4',
                  'https://lun.ua/uk/котеджі/київ?page=5',
                  'https://lun.ua/uk/котеджі/київ?page=6',
                  'https://lun.ua/uk/котеджі/київ?page=7',
                  'https://lun.ua/uk/котеджі/київ?page=8',
                  'https://lun.ua/uk/котеджі/київ?page=9',
                  'https://lun.ua/uk/котеджі/київ?page=10',
                  'https://lun.ua/uk/котеджі/київ?page=11',
                  'https://lun.ua/uk/котеджі/київ?page=12',
                  'https://lun.ua/uk/котеджі/київ?page=13',
                  'https://lun.ua/uk/котеджі/київ?page=14',
                  'https://lun.ua/uk/котеджі/київ?page=15',
                  'https://lun.ua/uk/котеджі/київ?page=16',
                  'https://lun.ua/uk/котеджі/київ?page=17',
                  'https://lun.ua/uk/котеджі/київ?page=18',
                  'https://lun.ua/uk/котеджі/київ?page=19',
                  'https://lun.ua/uk/котеджі/київ?page=20',
                  'https://lun.ua/uk/котеджі/київ?page=21',
                  'https://lun.ua/uk/котеджі/київ?page=22',
                  'https://lun.ua/uk/котеджі/київська-обл?page=2',
                  'https://lun.ua/uk/котеджі/київська-обл?page=3',
                  'https://lun.ua/uk/котеджі/київська-обл?page=4',
                  'https://lun.ua/uk/котеджі/київська-обл?page=5',
                  'https://lun.ua/uk/котеджі/київська-обл?page=6',
                  'https://lun.ua/uk/котеджі/київська-обл?page=7',
                  'https://lun.ua/uk/котеджі/київська-обл?page=8',
                  'https://lun.ua/uk/котеджі/київська-обл?page=9',
                  'https://lun.ua/uk/котеджі/київська-обл?page=10',
                  'https://lun.ua/uk/котеджі/київська-обл?page=11',
                  'https://lun.ua/uk/котеджі/київська-обл?page=12',
                  'https://lun.ua/uk/котеджі/київська-обл?page=13',
                  'https://lun.ua/uk/котеджі/київська-обл?page=14',
                  'https://lun.ua/uk/котеджі/київська-обл?page=15',
                  'https://lun.ua/uk/котеджі/київська-обл?page=16',
                  'https://lun.ua/uk/котеджі/київська-обл?page=17',
                  'https://lun.ua/uk/котеджі/київська-обл?page=18',
                  'https://lun.ua/uk/котеджі/київська-обл?page=19',
                  'https://lun.ua/uk/котеджі/київська-обл?page=20',
                  'https://lun.ua/uk/котеджі/київська-обл?page=21',
                  'https://lun.ua/uk/котеджі/львів?page=2',
                  'https://lun.ua/uk/котеджі/львів?page=3',
                  'https://lun.ua/uk/котеджі/львів?page=4',
                  'https://lun.ua/uk/котеджі/івано-франківськ?page=2',
                  'https://lun.ua/uk/котеджі/харків?page=2',
                  'https://lun.ua/uk/котеджі/одеса?page=2']

    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = LunItem()
        item['oblast'] = response.xpath('//*[@id="building-contacts"]/div[2]/span/text()').get()
        item['town'] = response.xpath('//*[@id="building-contacts"]/div[2]/a/text()').get()
        item['title'] = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/h1/text()').get()
        item['developer_name'] = response.xpath(
            '//*[@id="building-contacts-content"]/div[2]/a/div/div[1]/span/text()').get()
        item['project_name'] = response.xpath('//div[@class="CottagePrices-cell -name"]').getall()
        item['project_area'] = response.xpath('//div[@class="CottagePrices-cell -area"]').getall()
        item['project_price_uah'] = response.xpath('//div[@data-currency="uah"]').getall()
        item['type_and_count'] = response.xpath('//*[@id="queues_states"]/table').get()
        if item.not_empty_values():
            return item

#    def parse_additional_page(self, response, item):
#        item['additional_data'] = response.xpath('//p[@id="additional_data"]/text()').get()
#        return item
