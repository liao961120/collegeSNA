import scrapy, datetime, socket
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest, Request
from scrapy.loader import ItemLoader
from college_network.items import CollegeNetworkItem


class freshmanntuNetworkSpider(CrawlSpider):
    name = "ntuNetwork"
    allowed_domains = ['freshman.tw']
    
    # Select a department as the ego of the network, in this case 臺大圖資
    start_urls =  ['http://freshman.tw/cross/104/001']
    

    # Rules for Horizontal and Vertical Crawling
    rules = (
        Rule(LinkExtractor(allow=r'cross/104/001[0-9]{3}'), callback='parse_item'),
    )
    
    
    def parse_item(self, response):
        l = ItemLoader(item=CollegeNetworkItem(), response=response)

        l.add_xpath('college', "//div[@class='row school-title-wrapper']/p/b/a/text()")
        l.add_xpath('department', "//div[@class='row school-title-wrapper']/p/b/text()[2]")
         
        l.add_xpath('department_attr', "//div[@class='card-block']/p/b[position() <= 6]/text()")
        l.add_xpath('department_attr_val', "//div[@class='card-block']/p/text()[position() <= 6]")

        l.add_xpath('overlap_college', "//div[@class='card-block']//small/a/text()")
        l.add_xpath('overlap_college_num', "//div[@class='card-block']//small/text()")
        l.add_xpath('applied_region', "//div[@class='card-block']/text()[re:test(., 'x\d{1,3}')]")
        

        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('rtrv_date', datetime.datetime.now())

        return l.load_item() 
