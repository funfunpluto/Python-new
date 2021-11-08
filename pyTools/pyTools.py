#!/usr/bin/env python

import re, pg, os

def readlines(filename):
    ifile = open(filename, 'r')
    lines = ifile.readlines()
    return lines
    
def lister_direct(lines, seperator):
    linList = []
    for line in lines:
        line = line.strip()
        items = seperator.split(line)
        linList.append(items)
    return linList

def lister(lines, seperator):
    linList = []
    for line in lines:
        items = seperator.split(line.strip())
        linList.append(items)
    return linList
        
def list2tuple(list):
    if type(list) is type([]):
        return tuple(list)

def line_collector(mark, lines):
    dict = {}
    for line in lines:
        kmatch = re.search(mark, line)
        if kmatch and not dict.has_key(mark):
            key = line.strip()
            key = key.replace(mark, '')
            dict[key] = []
        elif line != '\n':
            dict[key].append(line.strip())
    return dict

def dictSorter(adict):
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)
    #return adict

def create_table(dbname, cstr):
    cnx = pg.DB(dbname)
    qr = cnx.query(cstr)
    if qr:
        paren = re.compile('(')
        space = re.compile('\s+')
        clist = lister(cstr, paren)
        tname = lister(clist[0], space)[-1]
        print "Table ", tname, "has been created.\n"
    else:
        "Table creation failed.\n"

def append_list2str(list):
    lstr = ''
    for item in list:
        lstr += str(item) + ' '
    return lstr
