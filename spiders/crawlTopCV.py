import scrapy
import w3lib.html
import re

urls = []
file = open('job/topcv.txt', 'r')
links = file.readlines()
for link in links:
    urls += [link]

i = 0
class DataSpider(scrapy.Spider):
    name = 'topcv'

    start_urls = urls
    
    def parse(self, response):
        global i
        if (response.css('div#main div.box-header-job div.box-job-info h1.job-title').get() == None):
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
                'job_title': w3lib.html.remove_tags(response.css('div#main div.box-header-job div.box-job-info h1.job-title').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'company': w3lib.html.remove_tags(response.css('div#main div.box-header-job div.box-job-info a.text-dark-blue').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'salary': w3lib.html.remove_tags(response.css('div.box-detail-job > :nth-child(2) div :nth-child(1)').get().strip().replace('Mức lương', '')).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'location': w3lib.html.remove_tags(response.css('div.box-detail-job > :nth-child(3) div').get().strip().replace('- ', '')).replace('\r', '').replace('\t', '').replace('\n', ''),
                'position': w3lib.html.remove_tags(response.css('div#main div.box-header-job div.box-job-info h1.job-title').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'job_description': w3lib.html.remove_tags(response.css('div.box-detail-job > :nth-child(5)').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'job_requirement': w3lib.html.remove_tags(response.css('div.box-detail-job > :nth-child(7)').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'benefit': w3lib.html.remove_tags(response.css('div.box-detail-job > :nth-child(9)').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', '')
            }
        i += 1