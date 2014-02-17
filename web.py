#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author : twotruths
# desc : for web
# created : 2014-02-14

from bottle import Bottle, route, get, post, request, run, template, static_file, install, error
from bottle.ext import sqlite
import time

app = Bottle()
sqlitePlugin = sqlite.Plugin(dbfile = 'data.db')
app.install(sqlitePlugin)

@app.get('/favicon.ico')
def server_favicon() :
    return static_file('favicon.ico', root = './')

@app.get('/js/<filename>')
def server_js(filename) :
    return static_file(filename, root = './js')

@app.get('/css/<filename>')
def server_css(filename) :
    return static_file(filename, root = './css')

@app.get('/fonts/<filename>')
def server_fonts(filename) :
    return static_file(filename, root = './fonts')

@app.get('/img/<filename>')
def server_img(filename) :
    return static_file(filename, root = './img')

@app.error(404)
def error404(error) :
    return 'Nothing Here.'

@app.get('/')
def index(db) :
    data = db.execute('select * from items order by date desc limit 0, 20').fetchall()
    
    return template('index', items = data)

@app.post('/getItemList')
def getItemList(db) :
    data = db.execute('select * from items order by date desc limit ?, 20',\
        (request.forms.get('start'), )).fetchall()

    # rssId = request.forms.get('id')
    # flag = True
    # while flag :
    #     rssList = db.execute("select * from rss where parentId=?", (rssId, )).fetchall()


    # data = db.execute('select * from items where title in (%s) order by date desc limit ?, 20' %\
    #     ','.join('?'*len(titleList)), titleList + (request.forms.get('start'), ).fetchall()

    return template('getItemList', items = data, content = False)

# @app.post('/getRssList')
# def getRssList(db) :
#     data = db.execute("select * from rss where parentId=?",\
#         (request.forms.get('id'), )).fetchall()

# def getRssTitleList(db, rssId) :
#     rssTitleList = []

#     rssIdList = db.execute("select * from rss where parentId=?", (rssId, )).fetchall()
#     for rssIdItem in rssIdList :
#         rssTitleList.append(rssIdItem[2])
#         rssTitleList.extend(getRssTitleList)

if __name__ == '__main__' :
    run(app, host = 'localhost', port = 8080, reloader = False, debug = True)
