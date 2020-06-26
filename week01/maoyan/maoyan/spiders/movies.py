import scrapy
from maoyan.items import MaoyanItem
# from bs4 import BeautifulSoup
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']


    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)


        # 解析函数
    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-item film-channel"]')
        #for i in range(len(title_list)):
        # 在Python中应该这样写
        for movie in movies[:10]:
            # 在items.py定义
            url = 'https://maoyan.com' + movie.xpath('./a/@href').extract_first().strip()
            print(url)
            yield scrapy.Request(url=url, callback=self.parse2, dont_filter=False)

    # 解析具体页面
    def parse2(self, response):
        item = MaoyanItem()
        item['title'] = Selector(response=response).xpath('//h1[@class="name"]/text()').extract_first().strip()
        tages = Selector(response=response).xpath('//li[@class="ellipsis"]')
        item['mtype'] = ','.join(tages[0].xpath('./a/text()').extract())
        item['mtime'] = tages[2].xpath('./text()').extract_first().strip()
        yield item
