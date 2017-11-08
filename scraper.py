#!/usr/bin/python
from requests import get
from bs4 import BeautifulSoup
import re

r = get('https://en.wikipedia.org/wiki/List_of_inventors')

soup = BeautifulSoup(r.content, 'lxml')
for lel in soup.select('div[class="mw-parser-output"] ul li'):
    if len(lel.text.split(", ")) > 1:
        text = lel.text.replace(u'\u2013', '%')
        text = text + "#"

        place = re.compile("\)\s?(,|%|\s)([a-zA-Z0-9-\/.,\s]+)(?=\S)(%|-|#)").split(text)
        ''' first = splitters[len(splitters)-1]
        splitters2 = first.split("%");
        last = splitters2[0] '''
        if len(place) > 1:
            print "\nLong string: " + text
            print "Place: " + place[2]

        ''' splitters = text.split("%")
        last = splitters[len(splitters)-1]
        print "Invention: " + last '''
