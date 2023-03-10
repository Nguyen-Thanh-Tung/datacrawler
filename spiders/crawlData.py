import scrapy

urls = []
file = open('joblinks.txt', 'r')
links = file.readlines()
for link in links:
    urls += [link]

i = 0
class DataSpider(scrapy.Spider):
    name = 'vietnamwork'

    start_urls = urls
    def parse(self, response):
        global i
        yield {
            'job_title': response.css('div.job-header-info h1.job-title::text').get().strip(),
            'company': response.css('div.job-header-info div.row a span::text').get().strip(),
            'salary': response.css('div.job-header-info span.salary strong::text').get().strip(),
            'location': str(list(filter(None, ([response.css('div.location div.location-name::text')[i].get().strip('+-–*o"•·●\\>■✅\n\r\"\\ ').replace('\t', '') \
                            for i in range(len(response.css('div.location div.location-name::text').getall()))
                            ])))).replace('[', '').replace(']', '').replace("'", ""),
            'position': response.css('div.job-header-info h1.job-title::text').get().strip().replace('\t', ''),
            'job_description': str(list(filter(None, ([response.css('div.description::text')[i].get().strip('+-–*o"•·●\\>■✅\n\r\"\\ ').replace('\t', '') \
                            for i in range(len(response.css('div.description::text').getall()))
                            ])))).replace('[', '').replace(']', '').replace("'", ""),
            'job_requirement': str(list(filter(None, ([response.css('div.requirements::text')[i].get().strip('+-–*o"•·●\\>■✅\n\r\"\\ ').replace('\t', '') \
                                for i in range(len(response.css('div.requirements::text').getall()))
                            ])))).replace('[', '').replace(']', '').replace("'", ""),
            'benefit': str(list(filter(None,([response.css('div.benefits div.benefit-name::text')[i].get().strip('+-–*o"•·●\\>■✅\n\r\"\\ ').replace('\t', '') \
                            for i in range(len(response.css('div.benefits div.benefit-name::text').getall()))
                        ])))).replace('[', '').replace(']', '').replace("'", ""),
            'quantity': "1"
        }
        i += 1