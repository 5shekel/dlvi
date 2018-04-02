#!/usr/bin/env python2
import bs4,sys




with open(sys.argv[1], 'r') as f:
    webpage = f.read().decode('utf-8')

soup = bs4.BeautifulSoup(webpage, "lxml")
for a in soup.findAll('a', href=True):
   Print ("https://vimeo.com%s" % a['href'])

