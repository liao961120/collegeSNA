# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CollegeNetworkItem(scrapy.Item):

    # Primary fields
    college = scrapy.Field()
    department = scrapy.Field()
    
    department_attr = scrapy.Field()
    department_attr_val = scrapy.Field()
    
    overlap_college = scrapy.Field()
    overlap_college_num = scrapy.Field()
    applied_region = scrapy.Field()
    

    # Calculated fields

    # Housekeeping fields
    url = scrapy.Field()
    rtrv_date = scrapy.Field()



    # define the fields for your item here like:
    # name = scrapy.Field()
#    pass
