import scrapy
from scrapy.http import HtmlResponse
from unsplash.items import UnsplashItem
from scrapy.loader import ItemLoader

class ImgparserSpider(scrapy.Spider):
    name = "imgparser"
    allowed_domains = ["unsplash.com"]

    def __init__(self, query):
        super().__init__()
        self.query = query
        self.start_urls = [f"https://unsplash.com/s/photos/{query}"]

    def parse(self, response: HtmlResponse):
        print(response.status)
        links = response.xpath("//figure[@itemprop='image']//a[@itemprop='contentUrl']")
        for link in links:
            yield response.follow(link, callback=self.parse_photo)


    def parse_photo(self, response: HtmlResponse):
        name = response.xpath("//h1/text()").get()
        loader = ItemLoader(item=UnsplashItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('photos', f"//img[@alt='{name}']/@srcset")
        loader.add_value('url', response.url)
        loader.add_value('query', self.query)
        yield loader.load_item()