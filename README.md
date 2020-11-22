# Data Project - Web Scraping

## Run Instructions
1. Run ```scrapy crawl law-firms -o law-firm.csv``` to get a list of companies
2. Run ```scrapy crawl law-firm-details -o law-firm-details.csv``` to get a detailed list of of companies
3. Run ```python visual.py``` to generate a table of data extracted 

## Description
This is a Web Scraping project that extract data from https://www.legal500.com/c/france/directory/, a directory of law firms in France. It also get detailed info for each company.

I used scrapy framework to extract law firms with a single-office. I had a challenge to get multiple-offices info. Also, the are some companies that with missing detailed info/pages are different! e.g: https://www.legal500.com/firms/12017-racine-ocean-indien/21537-saint-denis-de-la-reunion-france/, https://www.legal500.com/firms/14475-pech-de-laclause-bathmanabane-associes/18902-paris-france/, https://www.legal500.com/firms/18573-huglo-lepage-avocats/25232-paris-france/ etc.

In general, this was a very interesting exercise, beaucause I had new experience in scraping HTML tables and using Scrapy shell to find a right Selector. Scrapy shell was a good practice to save time while analyzing the webpages and identifying a good Selector.
