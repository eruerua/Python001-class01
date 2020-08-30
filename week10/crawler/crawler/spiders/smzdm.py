import scrapy
from crawler.items import CrawlerItem
from scrapy.selector import Selector

class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['www.smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']

    
    def start_requests(self):
        url = 'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/'
        yield scrapy.Request(url=url, callback=self.parse)
    
    
    def parse(self, response):
        try:
            phones = Selector(response=response).xpath('//h5[@class="feed-block-title"]/a/@href').getall()
            if len(phones)==0:
                raise Exception('未找到链接！')
            for phone in phones[:10]:
                url = phone
                print(url)
                print('成功找到手机详情链接')
                yield scrapy.Request(url=url, callback=self.parse2, dont_filter=False)
        except Exception as e:
            print(e)
            print('手机详情页链接未抓取成功')

    def parse2(self, response):
        item = CrawlerItem()
        try:
            page = Selector(response=response).xpath('//ul[@class="pagination"]')
            author = Selector(response=response).xpath('//h1[@class="title J_title"]/text()').get().strip()
            author = ' '.join(author.split())
            print(author)
            if len(page)==0:
                print('只有一页评论')
                comments=self.comms(response)
                for comment in comments:
                    if comment == " " or comment == "  " :
                        pass
                    else:
                        item['author'] = author
                        item['comment'] = comment
                        yield item
                #####
            else:
                print('该页有多页评论')
                page_num = page[0].xpath('./li/a/text()').getall()
                print(page_num)
                num = int(page_num[-2])
                print(num)
                for n in range(1,num+1):
                    print(f'正在提取第{n}页')
                    if n == 1:
                        url = response.request.url + '/#comments'
                    else:
                        url = response.request.url + f'/p{n}/#comments'
                    yield scrapy.Request(url=url, callback=self.parse3, dont_filter=False)
        except Exception as e:
            print(e)
            print('手机详情页链接未抓取成功')    

    def parse3(self, response):
        item = CrawlerItem()
        try:
            author = Selector(response=response).xpath('//h1[@class="title J_title"]/text()').get().strip()
            author = ' '.join(author.split())
            comments=self.comms(response)
            for comment in comments:
                    if comment == " " or comment == "  " :
                        pass
                    else:
                        item['author'] = author
                        item['comment'] = comment
                        yield item
        except Exception as e:
            print(e)
            print('手机详情页链接未抓取成功')    

    def comms(self, response):
        return Selector(response=response).xpath('//div[@id="commentTabBlockNew"]//div[not(contains(@class,"blockquote_wrap"))]/div[@class="comment_conWrap"]//p/span/text()').extract()
