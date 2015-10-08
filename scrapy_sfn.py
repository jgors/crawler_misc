#!/usr/bin/env python

#----------------------------------------------------------------
# Author: Jason Gors <jasonDOTgorsATgmail>
# Creation Date: 10-04-2015
# Purpose:
#----------------------------------------------------------------
import os
import json
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


url = 'http://www.abstractsonline.com/plan/start.aspx?mkey={D0FF4555-8574-4FBB-B9D4-04EEC8BA0C84}'

output_dir = './output'
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)


# class MySpider(scrapy.Spider):
    # name = "myspider"     # NOTE this must be uncommented for the spider to work
    # allowed_domains = ["abstractsonline.com"]
    # start_urls = [url]

    # these examples are using this:
    # http://doc.scrapy.org/en/1.0/topics/practices.html#run-scrapy-from-a-script

    ##################################### this works, but all the methods are very redundant
    # def parse(self, response):
        ## resp_contents = response.xpath("//a").xpath('@href').extract()
        # resp_contents = response.xpath("//a/@href").extract()
        # for href in resp_contents:
            # if 'Browse.aspx' in href: 
                # full_url = response.urljoin(href)
                # request = scrapy.Request(full_url, callback=self.parse_Browse_pg, 
                                        # # meta={'dataset': dataset}, 
                                        # )
                # yield request

    # def parse_Browse_pg(self, response):
        # resp_contents = response.xpath("//a/@href").extract()
        # for href in resp_contents:
            # if 'BrowseResults.aspx?date=' in href: 
                # full_url = response.urljoin(href)
                # print full_url
                # request = scrapy.Request(full_url, callback=self.parse_BrowseResults_pg, 
                                        # # meta={'dataset': dataset}, 
                                        # )
                # yield request

    # def parse_BrowseResults_pg(self, response):
        # resp_contents = response.xpath("//a/@href").extract()
        # for href in resp_contents:
            # if 'ViewSession.aspx?' in href: 
                # full_url = response.urljoin(href)
                # print full_url
                # request = scrapy.Request(full_url, callback=self.parse_ViewSession_pg, 
                                        # # meta={'dataset': dataset}, 
                                        # )
                # yield request

    # def parse_ViewSession_pg(self, response):
        # resp_contents = response.xpath("//a/@href").extract()
        # for href in resp_contents:
            # if 'ViewAbstract.aspx?mID=' in href: 
                # full_url = response.urljoin(href)
                # print full_url
                # request = scrapy.Request(full_url, callback=self.parse_ViewAbstract_pg, 
                                        # # meta={'dataset': dataset}, 
                                        # )
                # yield request

    # def parse_ViewAbstract_pg(self, response):
        # resp_contents = response.xpath('//table[@cellpadding=3]').xpath('.//tbody')
        # print resp_contents 
    #####################################


    ##################################### simplify the parse methods above into one (FIXME doesn't work)
    # def start_requests(self):
        # yield scrapy.Request(url, self.parse)

    # def parse(self, response, pg_to_parse='Browse.aspx', parser=None):
        # if parser:
            # self.parse = parser 

        # resp_contents = response.xpath("//a/@href").extract()
        # for href in resp_contents:
            # if pg_to_parse in href: 
                # full_url = response.urljoin(href)
                # print full_url
                # request = scrapy.Request(full_url, callback=self.parse, 
                                        # # meta={'dataset': dataset}, 
                                        # )
                # yield request

    # def parse_ViewAbstract_pg(self, response):
        # resp_contents = response.xpath('//table[@cellpadding=3]').xpath('.//tbody')
        # print resp_contents 

    # parse(pg_to_parse='Browse.aspx')
    # parse(pg_to_parse='BrowseResults.aspx?date=')
    # parse(pg_to_parse='ViewSession.aspx?')
    # parse(pg_to_parse='ViewAbstract.aspx?mID=', parser=parse_ViewAbstract_pg)
    #####################################


url = 'http://www.abstractsonline.com/plan/start.aspx?mkey={D0FF4555-8574-4FBB-B9D4-04EEC8BA0C84}'
# url = 'http://www.abstractsonline.com/plan/start.aspx?mkey='

class MySpider(CrawlSpider):
    name = "myspider"     # NOTE this must be uncommented for the spider to work
    allowed_domains = ["abstractsonline.com"]

    # def __init__(self, *args, **kwargs):
        # super(MySpider, self).__init__(*args, **kwargs)
        # if 'k' in kwargs:
            # k = kwargs['k']
            # starturl = url + k
            # self.start_urls = [starturl]
    start_urls = [url]

    # For logging in via a POST see:
    # http://doc.scrapy.org/en/1.0/topics/spiders.html#scrapy.spiders.Spider.start_requests

    # And `parse_start_url` could probably be used to grab out a cookie for storage before proceeding into the rules:
    # http://doc.scrapy.org/en/1.0/topics/spiders.html#scrapy.spiders.CrawlSpider.parse_start_url

    # this is using rules to crawl the pages
    # http://doc.scrapy.org/en/1.0/topics/spiders.html#crawlspider-example

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        # Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),
        # Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', )
                            # )
              # ),
        # # Extract links matching 'item.php' and parse them with the spider's method parse_item
        # Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
        # Rule(LinkExtractor(allow=('item\.php', ),
                            # ), 
               # callback='parse_item'),

        Rule(LinkExtractor(allow=('Browse\.aspx', ))),

        Rule(LinkExtractor(allow=('BrowseResults\.aspx\?date\=', ))),
        # Rule(LinkExtractor(allow=('BrowseResults\.aspx\?date\=10/17/2015', ))),

        Rule(LinkExtractor(allow=('ViewSession\.aspx\?', ))),
        # Rule(LinkExtractor(allow=('ViewSession\.aspx\?sKey\=6766b156-7f22-44eb-866e-b67953137129', ))),

        Rule(LinkExtractor(allow=('ViewAbstract\.aspx\?mID\=', )), callback='parse_ViewAbstract_pg'),
        # NOTE:
        # Can use `process_links` and/or ` process_request` to filter responses and/or requests inside 
        # each Rule for more flexability, and probably `cb_kwargs` to pass the data around.  
        # Also there are many arguments that can be give to LinkExtractor for parsing (lxml):
        # http://doc.scrapy.org/en/1.0/topics/link-extractors.html#topics-link-extractors
        # (particularly useful might be `restrict_xpaths` and `process_value` arguments)
    )


    def parse_ViewAbstract_pg(self, response):
        output = {'url': response.url}

        try:
            table_rows = response.xpath('//table[@cellpadding=3]/tr')#.extract()

            all_text = []
            for tr in table_rows:
                tds = tr.xpath('.//td').xpath('.//text()').extract()
                if tds:
                    cleaned_txt = []
                    for td in tds:
                        td = td.strip()
                        td = td.replace('\n', '')
                        if td:
                            cleaned_txt.append(td)
                    all_text.append(cleaned_txt)

            cleaned_all_text = []
            for cnt, l in enumerate(all_text):
                if len(l) > 1:
                    if l[0].endswith(':'):
                        l[0] = l[0][:-1]
                    cleaned_all_text.append([l[0], ' '.join(l[1:])])
                else:
                    if (cnt == 0) and (l[0] == 'This presenter will not attend'):
                        cleaned_all_text.append([u'NOTE', l[0]])
                    else:
                        cleaned_all_text[-1][-1] += '; ' + l[0]

            d = dict(cleaned_all_text)
            output.update(d)
            # print output
            # print

        except:
            print
            print "########################################"
            print "########################################"
            print "FAILURE at:"
            print response.url
            print "########################################"
            print "########################################"
            print
            # this is not thread safe, but it doesn't really matter here
            with open('./failures.txt', 'w') as f:
                f.write("FAILURE at:\n{}".format(response.url))

        fname = response.url.split('?')[-1].replace('&', '_')
        output_fname = '{}/{}'.format(output_dir, fname)
        with open(output_fname, 'w') as f:
            json.dump(output, f)


process = CrawlerProcess()
# process.crawl(MySpider(), k='{D0FF4555-8574-4FBB-B9D4-04EEC8BA0C84}')
process.crawl(MySpider())
process.start()


# how this should work:
#
# starting from this page:
#   http://www.abstractsonline.com/plan/start.aspx?mkey={D0FF4555-8574-4FBB-B9D4-04EEC8BA0C84}
#   follow this href:
#   Browse.aspx 
#
# then from that page, go to all of these pages:
#   BrowseResults.aspx?date=*
#   eg. BrowseResults.aspx?date=10/14/2015
#       ...
#       BrowseResults.aspx?date=10/23/2015
#
# then from there, go to all of these pages:
#   ViewSession.aspx?*
#
# then from there, go to all of these pages:
#   ViewAbstract.aspx?
#
# then from that page, get this: 
#   xpath_match('//table[@cellpadding=3]')

