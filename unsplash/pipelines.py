# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import csv
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class UnsplashPipeline:
    def process_item(self, item, spider):
        with open('outputfile.csv', 'a', newline='') as csvfile:
            fieldnames = ['name', 'url', 'query', 'path']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': item['name'], 'url': item['url'], 'query': item['query'], 'path': item['photos'][0]['path']})
        return item

class PhotoPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img_url in item['photos']:
                try:
                    yield scrapy.Request(img_url)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item

