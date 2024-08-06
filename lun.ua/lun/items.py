# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LunItem(scrapy.Item):

    title = scrapy.Field()
    oblast = scrapy.Field()
    town = scrapy.Field()
    developer_name = scrapy.Field()
    project_name = scrapy.Field()
    project_area = scrapy.Field()
    project_price_uah = scrapy.Field()
    type_and_count = scrapy.Field()

    def not_empty_values(self):
        return self['title'] or self['oblast'] or self['town'] or self['developer_name'] or self['project_name'] \
               or self['project_area'] or self['project_price_uah'] or self['type_and_count']
