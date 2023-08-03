#!/usr/bin/env python3

import hashlib
import os.path
from newspaper import Article

dataFile = open('data.txt', 'r')
lines = [x.strip('\n') for x in dataFile]
dataFile.close()

keyFile = open('../../key.txt', 'r')
key = keyFile.read().strip('\n')
keyFile.close()

i = 0
newLines = []
for ln in lines:
    sp = ln.split('|')
    guid = hashlib.md5(sp[1].encode('utf-8')).hexdigest()
    if not os.path.isfile('articles/'+guid+'.html'):
        try:
            article = Article(sp[1])
            article.download()
            article.parse()

            articleHtml = '<!DOCTYPE html><html lang="en"><head><title>'+article.title+'</title><style type="text/css">body{font-size:20px;}</style></head><body>'
            articleHtml += '<h1>'+article.title+'</h1>'
            articleHtml += '<p><strong>Source: <a href="' + sp[1] + '" target="_blank">' + sp[1] + '</a></strong></p>'
            articleHtml += '<p>[<a href="../read.php?key='+key+'&id='+str(i)+'">mark read</a>]</p>'
            articleHtml += '<p>'
            articleHtml += article.text.replace('\n','<br>')
            articleHtml += '</p>'
            articleHtml += '<p>[<a href="../read.php?key='+key+'&id='+str(i)+'">mark read</a>]</p>'
            articleHtml += '</body></html>'
            articleFile = open('articles/' + guid + '.html', 'w')
            articleFile.write(articleHtml)
            articleFile.close()
            ln = ln + '|' + article.title
        except:
            print('error:'+sp[1]);
    newLines.append(ln)
    i += 1

dataFile = open('data.txt', 'w')
dataFile.write('\n'.join(newLines))
dataFile.close()
