from lun.spiders.lun_spider import MySpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


process = CrawlerProcess(get_project_settings())
process.crawl(MySpider)
process.start()