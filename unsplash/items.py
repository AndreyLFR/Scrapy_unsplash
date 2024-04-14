# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose

def process_name(value):
    value = value[0].strip()
    return value

def process_photos(value):
    #все фотки приемлемого качества, поэтому беру первую. в url есть инфо о качестве, так что можно выбрать при необходимости
    return [s for s in value[0].split() if 'http' in s][0]


class UnsplashItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=Compose(process_name), output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=Compose(process_photos))
    url = scrapy.Field(output_processor=TakeFirst())
    query = scrapy.Field(output_processor=TakeFirst())
