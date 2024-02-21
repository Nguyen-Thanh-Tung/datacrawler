import scrapy
import w3lib.html
import re

urls = []
file = open('job/glints.txt', 'r')
links = file.readlines()
for link in links:
    urls += [link]

i = 0
class DataSpider(scrapy.Spider):
    name = 'glints'

    start_urls = urls
    def parse(self, response):
        global i
        if (response.css('h1.TopFoldsc__JobOverViewTitle-sc-kklg8i-3').get() == None):
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
                'job_title': w3lib.html.remove_tags(response.css('h1.TopFoldsc__JobOverViewTitle-sc-kklg8i-3').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'company': w3lib.html.remove_tags(response.css('div.TopFoldsc__JobOverViewCompanyName-sc-kklg8i-5').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'salary': w3lib.html.remove_tags("div.TopFoldsc__BasicSalary-sc-kklg8i-15").get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'location': w3lib.html.remove_tags(response.css('div.job-details > div.job-details__overview > :nth-child(3)').get().strip().replace('Xem bản đồ', '')).replace('\r', '').replace('\t', '').replace('\n', ''),
                'position': w3lib.html.remove_tags(response.css('div.job-details > div.job-details__header > h1.job-details__title').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'job_description': w3lib.html.remove_tags(response.css('div.job-details > :nth-last-child(5)').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'job_requirement': w3lib.html.remove_tags(response.css('div.job-details > :nth-last-child(3)').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
                'benefit': w3lib.html.remove_tags(response.css('div.job-details > :nth-last-child(1)').get().strip()).replace('&gt;', '>').replace('\r', '').replace('\t', '').replace('\n', ''),
            }
        i += 1