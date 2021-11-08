#!/usr/bin/env python

import re, os, MySQLdb

def createTbl(tablesql): 
    db =  MySQLdb.connect(user='saka', passwd='saka1983', host='localhost', db='Saka')
    cursor = db.cursor()
    cursor.execute(tablesql)
    db.close()

def insert2TL(instsql): 
    db =  MySQLdb.connect(user='saka', passwd='saka1983', host='localhost', db='Saka')
    cursor = db.cursor()
    cursor.execute(instsql)
    db.close()

def retrievDBSim():
    db =  MySQLdb.connect(user='saka', passwd='saka1983', host='localhost', db='Saka')
    cursor = db.cursor()
    sql = 'select words from allwords' 
    cursor.execute(sql)
    items = cursor.fetchall ()
    db.close()
    return items	
