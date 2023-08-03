#!/usr/bin/env python3

from bs4 import BeautifulSoup

dataFile = open('data.txt', 'w')

with open("ril_export.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    fp.close()

unread = True
for ul in soup.find_all('ul'):
    for li in ul.find_all('li'):
        a = li.find('a')
        ln = 'U|'
        if unread == False:
            ln = 'R|'
        ln += a.get('href')

        dataFile.write(ln+"\n");

    unread = False

dataFile.close()
