# -*- coding: utf-8 -*-
import scrapy
from DataProject.items import DetailsItem


class LawFirmDetailsSpider(scrapy.Spider):
    name = 'law-firm-details'
    allowed_domains = ['legal500.com']
    start_urls = ['http://legal500.com/']

    def parse(self, response):
        file = open("urls.txt")
        urls_in_file = file.read()
        urls = urls_in_file.splitlines()
        for url in urls:
            company_url = response.urljoin(url)
            request = scrapy.Request(company_url, callback=self.parse_details)
            request.meta['url'] = company_url
            yield request

    def parse_details(self, response):
        self.log('company url: ' + response.url)
        host_name = 'https://www.legal500.com'

        details_item = DetailsItem()
        details_item['company_name'] = response.css('#left-col h2::text').extract_first()
        details_item['company_logo'] = host_name + response.css('#left-col img::attr(data-lazy-src)').extract_first()
        details_item['address'] = response.css('.address-box address').extract_first().replace('<address>\n\n    ', '').replace('<br>', '').replace('\n</address>', '')
        details_item['website'] = response.css('.firm-website::attr(href)').extract_first()
        details_item['phone_number'] = response.css('.contact-links span::text').extract()[2]
        details_item['email_address'] = response.css('.firm-email::attr(href)').extract_first().split(':')[1].split('?')[0]
        details_item['practice_heads'] = ";".join(response.css('#rankings_section div .practice-heads-list p a::text').extract())
        details_item['key_clients'] = ";".join(response.css('#rankings_section div .client-list p::text').extract())
        details_item['lawyers'] = ";".join(response.css('#lawyer_profiles table tbody tr td.profile-name::text').extract())
        yield details_item


