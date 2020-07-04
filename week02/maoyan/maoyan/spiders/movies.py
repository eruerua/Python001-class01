import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']


    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)


    # 解析链接
    def parse(self, response):
        try:
            movies = Selector(response=response).xpath('//div[@class="movie-item film-channel"]')
            for movie in movies[:10]:
                url = 'https://maoyan.com' + movie.xpath('./a/@href').extract_first().strip()
                print(url)
                yield scrapy.Request(url=url, callback=self.parse2, dont_filter=False)
        except:
            item = MaoyanItem()
            item['title']=item['mtype']=item['mtime']='未抓取成功'
            yield item
    # 解析具体页面
    def parse2(self, response):
        item = MaoyanItem()
        try:
            item['title'] = Selector(response=response).xpath('//h1[@class="name"]/text()').extract_first().strip()
            tages = Selector(response=response).xpath('//li[@class="ellipsis"]')
            item['mtype'] = ','.join(tages[0].xpath('./a/text()').extract())
            item['mtime'] = tages[2].xpath('./text()').extract_first().strip()
        except:
            item['title']=item['mtype']=item['mtime']='未抓取成功'
        yield item