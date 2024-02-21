import scrapy
from scrapy.selector import Selector
import w3lib.html
import re

urls = []
file = open('job/carreerbuilder.txt', 'r')
links = file.readlines()
for link in links:
    urls += [link]

i = 0
class CarreerbuilderSpider(scrapy.Spider):
    name = 'carreerbuilder'
    
    start_urls = urls
    def parse(self, response):
        global i
        company = 'None'
        if (response.css('div.job-desc h1.title::text').get() == None):
            yield {
                'link': response.css('link[rel="canonical"]::attr("href")').get(),
                'job_title': 'None',
                'company': 'None',
                'salary': 'None',
                'location': 'None',
                'position': 'None',
                'job_description': 'None',
                'job_requirement': 'None',
                'benefit': 'None',
            }
        else:
            if (response.css('div.job-desc a.job-company-name::text').get() != None):
                company = response.css('div.job-desc a.job-company-name::text').get().strip()
            yield {
                'link': response.css('link[rel="canonical"]::attr("href")').get(),
                'job_title': response.css('div.job-desc h1.title::text').get().strip(),
                'company': company,
                'salary': response.css('section.job-detail-content div.bg-blue div.row div.item-blue:nth-child(3) li:nth-child(1) p::text').get().strip(),
                'location': response.css('div.map p a::text').get().strip(),
                'position': response.css('div.job-desc h1.title::text').get().strip(),
                'job_description': re.sub(' +', ' ', w3lib.html.remove_tags(response.css('section.job-detail-content div.detail-row.reset-bullet').get().strip()).replace("Mô tả Công việc", "")).replace('\r', '').replace('\t', '').replace('\n', ''),
                'job_requirement': re.sub(' +', ' ', w3lib.html.remove_tags(response.css('section.job-detail-content > div:nth-child(4)').get().strip()).replace("Yêu Cầu Công Việc", "")).replace('\r', '').replace('\t', '').replace('\n', ''),
                'benefit': re.sub(' +', ' ', w3lib.html.remove_tags(response.css('section.job-detail-content > :nth-child(2)').get().strip()).replace("Phúc lợi", "")).replace('\r', '').replace('\t', '').replace('\n', ''),
            }
        i += 1