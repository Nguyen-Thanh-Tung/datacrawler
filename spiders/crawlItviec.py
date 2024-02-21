import scrapy
import w3lib.html
import re

urls = []
file = open('job/itviec.txt', 'r')
links = file.readlines()
for link in links:
    urls += [link]

i = 0
class DataSpider(scrapy.Spider):
    name = 'itviec'

    start_urls = urls
    def parse(self, response):
        print(response.css('div.job-details').get())

        global i
        if (response.css('h1.job-details__title').get() == None):
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
                'job_title': w3lib.html.remove_tags(response.css('div.job-details > div.job-details__header > h1.job-details__title').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'company': w3lib.html.remove_tags(response.css('div.job-details > div.job-details__header > div.job-details__sub-title').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'salary': w3lib.html.remove_tags(""),
                'location': w3lib.html.remove_tags(response.css('div.job-details > div.job-details__overview > :nth-child(3)').get().strip().replace('Xem bản đồ', '')).replace('\r', '').replace('\t', '').replace('\n', ''),
                'position': w3lib.html.remove_tags(response.css('div.job-details > div.job-details__header > h1.job-details__title').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'job_description': w3lib.html.remove_tags(response.css('div.job-details > :nth-last-child(5)').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'job_requirement': w3lib.html.remove_tags(response.css('div.job-details > :nth-last-child(3)').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'benefit': w3lib.html.remove_tags(response.css('div.job-details > :nth-last-child(1)').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
            }
        i += 1