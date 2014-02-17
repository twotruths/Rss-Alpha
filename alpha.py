# -*- coding: utf-8 -*-

# author : truths
# desc : for alpha tests
# created : 2014-02-13

#import urllib.request

#print(urllib.request.urlopen('http://www.baidu.com').read().decode('utf-8'))

import sqlite3

db = sqlite3.connect('data.db')
cu = db.cursor()
cu.execute('create table items\
    (id integer primary key autoincrement, date integer, title text, link text, desc text)')
db.commit()
cu.close()
db.close()
