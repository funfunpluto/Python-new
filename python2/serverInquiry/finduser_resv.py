#!/usr/bin/env python

import re, pg, os

def readlines(filename):
    ifile = open(filename, 'r')
    lines = ifile.readlines()
    return lines
    

def line_collector(mark, lines, markstr):
    for line in lines[1:]:
	kmatch = re.search(mark, line.lower())
	if kmatch:
	    print line
	elif not re.search(mark, markstr):
	    kname = mark 	        
    return kname
	
alines = readlines('DFCI_PEOPLE.txt')
ulines = readlines('userid.txt')
islines = readlines('isilon_user')
uline = ulines[0].strip()
ulist = uline.split(", ") 

        

markstr = ''
for ul in ulist:
    mk = line_collector(ul, alines, markstr)
    markstr = markstr + '; ' + mk
print markstr
