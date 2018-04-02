#!/usr/bin/env python2
import bs4,sys

example='''
<div class ="foo">
     <a href ="http://example.com"> </a>
     <a href ="http://example2.com"> Title here </a>
</div>

<div class ="foo">
     <a href ="http://example3.com"> </a>
     <a href ="http://example4.com"> Title 2 here </a>
'''


with open(sys.argv[1], 'r') as f:
    webpage = f.read().decode('utf-8')

soup = bs4.BeautifulSoup(webpage, "lxml")
for a in soup.findAll('a', href=True):
    #print "https://vimeo.com", a['href']
    print ("https://vimeo.com%s" % a['href'])
