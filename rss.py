#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : twotruths
# desc : process the opml file for rss/atom
# created : 2014-02-13

from xml.etree import ElementTree
import urllib.request
import sqlite3
import time, threading, re
import chardet

def processItems(dbname, source, items) :
    db = sqlite3.connect(dbname)
    cu = db.cursor()
    for item in items :
        title = item.find('title').text
        link = item.find('link').text
        desc = item.find('description').text

        pubDate = item.find('pubDate')
        if pubDate is None :
            pubDate = item.find('pubdate')

        date = time.mktime(time.strptime(pubDate.text[0:25], '%a, %d %b %Y %H:%M:%S'))

        # print(date, title, link, desc)

        cu.execute('select * from items where title=? and date=?', (title, date,))
        data = cu.fetchall()
        if len(data) == 0 :
            cu.execute('insert into items values (NULL, ?, ?, ?, ?, ?)', (date, source, title, link, desc,))

    cu.close()
    db.commit()
    db.close()

def processRss(dbname, url) :
    urlDoc = urllib.request.urlopen(url)
    rssBytes = urlDoc.read()
    rssChar = chardet.detect(rssBytes)['encoding']

    # decode with gbk when the detected charset is gb2312, to display simp and trad chinese at the same time
    if rssChar == 'GB2312' or rssChar == 'Big5' :
        rssChar = 'gbk'

    rssData = rssBytes.decode(rssChar, 'ignore')

    rssData = re.sub(r'encoding.*>', r'encoding="utf-8"?>', rssData, 1)
    # print(rssData.encode('gbk', 'ignore').decode('gbk'))

    rssDoc = ElementTree.fromstring(rssData)
    urlDoc.close()

    root = rssDoc
    channel = root.find('channel')
    title = channel.find('title').text

    items = channel.findall('item')
    processItems(dbname, title, items)

def processOutlines(dbname, outlines) :
    db = sqlite3.connect(dbname)
    cu = db.cursor()

    for outline in outlines.findall('outline') :
        print(outline.attrib['text'].encode('GBK', 'ignore').decode('GBK'))
        if not ('xmlUrl' in outline.attrib) :
            # cu.execute("insert into rss values (NULL, ?, ?, 0)",\
            #     (parentId, outline.attrib['title'], ))
            # cu.execute("select * from rss where parentId=? and title=?",\
            #     (parentId, outline.attrib['title'], ))
            processOutlines(dbname, outline)
        else :
            if outline.attrib['type'] == 'rss' :
                # start a new thread to get the Rss xml data
                # processRss(dbname, outline.attrib['xmlUrl'])

                # cu.execute("insert into rss values (NULL, ?, ?, 1)",\
                #     (parentId, outline.attrib['title'], ))
                rssThread = threading.Thread(target = processRss, args = (dbname, outline.attrib['xmlUrl']))
                rssThread.start()

    cu.close()
    db.commit()
    db.close()

def processOpml(opmlname, dbname) :
    db = sqlite3.connect(dbname)

    # if there's no items or rss table, create one.
    cu = db.cursor()
    if len(cu.execute("select * from sqlite_master where type='table' and name='items'").fetchall()) == 0 :
        cu.execute("create table items\
            (id integer primary key autoincrement, date integer, source text,\
            title text, link text, desc text)")
        db.commit()
    # if len(cu.execute("select * from sqlite_master where type='table' and name='rss'").fetchall()) == 0 :
    #     cu.execute('create table rss\
    #         (id integer primary key autoincrement, parentId integer, title text, isRss integer)')
    #     db.commit()
    # cu.execute("delete * from rss")
    # cu.execute("insert into rss values (0, 0, 'none', 0)")
    # cu.execute("insert into rss values (1, 0, 'all', 0)")
    # db.commit()

    cu.close()
    db.close()

    opmlDoc = ElementTree.parse(opmlname)

    root = opmlDoc.getroot()
    body = root.find('body')
    outlines = body

    processOutlines(dbname, outlines)

if __name__ == '__main__' :
    while True :
        processOpml('feeds.opml', 'data.db')
        time.sleep(60 * 15)
