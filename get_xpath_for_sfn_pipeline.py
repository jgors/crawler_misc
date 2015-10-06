#!/usr/bin/env python

#----------------------------------------------------------------
# Author: Jason Gors <jasonDOTgorsATgmail>
# Creation Date: 10-06-2015
# Purpose:
#----------------------------------------------------------------

resp_contents = response.xpath('//table[@cellpadding=3]')

table_rows = resp_contents.xpath('.//tr')

all_l = []
for tr in table_rows:
    # tds = tr.xpath('.//td/text()').extract()
    # tds = tr.xpath('string(.//td/text())').extract()
    # tds = tr.xpath('.//td/b/text()').extract()
    # print len(tds), tds


    l = []
    tds = tr.xpath('.//td')
    for num, td in enumerate(tds):
        txt = td.xpath('.//text()').extract()
        l.append(txt)
    all_l.append(tuple(l))

    # tds = tr.xpath('.//td').xpath('.//text()').extract()
    # print tds

