# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DataprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DetailsItem(scrapy.Item):
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    company_logo = scrapy.Field()
    address = scrapy.Field()
    website = scrapy.Field()
    phone_number = scrapy.Field()
    email_address = scrapy.Field()
    practice_heads = scrapy.Field()
    key_clients = scrapy.Field()
    # memberships = scrapy.Field()
    lawyers = scrapy.Field()
