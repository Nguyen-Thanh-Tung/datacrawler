import scrapy
import w3lib.html
import re

urls = []
file = open('job/joboko.txt', 'r')
links = file.readlines()
for link in links:
    urls += [link]

i = 0
class DataSpider(scrapy.Spider):
    name = 'joboko'

    start_urls = urls
    
    def parse(self, response):
        global i
        if (response.css('h1.job-info-ttl').get() == None):
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
            yield {
                'link': response.css('link[rel="canonical"]::attr("href")').get(),
                'job_title': w3lib.html.remove_tags(response.css('h1.job-info-ttl').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'company': w3lib.html.remove_tags(response.css('p.job-info-stl').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'salary': w3lib.html.remove_tags(response.css('ul.job-info-list > :nth-child(2)').get().strip().replace('Mức lương:', '')).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'location': w3lib.html.remove_tags(response.css('ul.job-info-list > :nth-child(1)').get().strip().replace('Địa điểm làm việc:', '')).replace('\r', '').replace('\t', '').replace('\n', ''),
                'position': w3lib.html.remove_tags(response.css('h1.job-info-ttl').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'job_description': w3lib.html.remove_tags(response.css('div.post-content > :nth-child(2)').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'job_requirement': w3lib.html.remove_tags(response.css('div.post-content > :nth-child(4)').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'benefit': w3lib.html.remove_tags("")
            }
        i += 1