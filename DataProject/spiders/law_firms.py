import scrapy


class LawFirmsSpider(scrapy.Spider):
    name = 'law-firms'
    allowed_domains = ['www.legal500.com']
    start_urls = ['https://www.legal500.com/c/france/directory/']

    def parse(self, response):
        host_name = 'https://www.legal500.com'
        companies = {}
        for company in response.css('#directoryUL li.single-office'):
            companies['company_name'] = company.css('strong::text').extract_first()
            companies['url'] = host_name + company.css('a::attr(href)').extract_first()
            companies['city'] = company.css('a').get(default='').split('<br>')[1].split('</a>')[0].strip()
            f = open("urls.txt", "a")
            f.write(companies['url'] + "\n")
            f.close()
            yield companies
