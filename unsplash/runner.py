from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from unsplash.spiders.imgparser import ImgparserSpider
import csv

if __name__ == '__main__':
    with open('outputfile.csv', 'a', newline='') as csvfile:
        fieldnames = ['name', 'url', 'query', 'path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
    query = input('Категория? ')
    install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
    configure_logging()
    process = CrawlerProcess(get_project_settings())
    process.crawl(ImgparserSpider, query=query)
    process.start()