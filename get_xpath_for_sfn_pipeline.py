#!/usr/bin/env python

#----------------------------------------------------------------
# Author: Jason Gors <jasonDOTgorsATgmail>
# Creation Date: 10-06-2015
# Purpose:
#----------------------------------------------------------------

# resp_contents = response.xpath('//table[@cellpadding=3]')
# table_rows = resp_contents.xpath('.//tr')

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
        cleaned_all_text.append([l[0], ' '.join(l[1:])])
    else:
        if (cnt == 0) and (l[0] == 'This presenter will not attend'):
            cleaned_all_text.append([u'NOTE:', l[0]])
        else:
            cleaned_all_text[-1][-1] += '; ' + l[0]

    # if cnt == 0:
        # if l[0] == 'This presenter will not attend':
            # cleaned_all_text.append([u'NOTE:', l[0]])
    # else:
        # if len(l) > 1:
            # cleaned_all_text.append([l[0], ' '.join(l[1:])])
        # else:
            # cleaned_all_text[-1][-1] += '; ' + l[0]

d = dict(cleaned_all_text)



cleaned_all_text = []
keyword_hit = False
support_hit = False
for l in all_text:
    print l
    if not keyword_hit:
        cleaned_all_text.append([l[0], ' '.join(l[1:])])
    else:
        # last_item_in_last_list = l_cleaned[-1][-1]
        cleaned_all_text[-1][-1] += ' ' + l[0]

    if 'Keyword' in l[0]:
        keyword_hit = True

d = dict(cleaned_all_text)


