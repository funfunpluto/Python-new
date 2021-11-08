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

def retrievDBSim(i):
    db =  MySQLdb.connect(user='saka', passwd='saka1983', host='localhost', db='Saka')
    cursor = db.cursor()
    sql = 'select words from allwords where wordID > %s'%str(i)    
    cursor.execute(sql)
    items = cursor.fetchall ()
    db.close()
    return items


def readlines(filename):
    ifile = open(filename, 'r')
    lines = ifile.readlines()
    return lines


def lineParser2Array(lines):
    aryItems = []
    for line in lines:
        items = re.split('<p>', line)
        for item in items:
            if item.find('Content>') == -1 and item != '</p>':
                aryItem = item.replace('</p>','')
                aryItems.append(aryItem)
    return aryItems


def lineParser(lines, sp):
    dic = {}
    keys = []
    for line in lines:
        items = re.split(sp, line)
        keys.append(items[0])
	dic[items[0]] = line
    return keys,dic


def write2txt(lines, fn):
    wfile = open(fn, 'a')
    for line in lines:
        if type(line) == type(''):
	    wfile.write(line)
            wfile.write('\n')
        else:
	    line = line[0]
	    wfile.write(line)
            wfile.write('\n\n')


def insert2allWords(items):
	#this function is for populating the allwords table, which only has two columns. One is the index, the other is the entry of the dictionary.	
    i = 0	
    for item in items:
        inst = 'insert into allwords (words) values (\''
        inst += item
        inst += '\');'
        insert2TL(inst)
	i = i + 1
    return i







