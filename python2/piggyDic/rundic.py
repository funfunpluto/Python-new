#!/usr/bin/env python

import re, os, sys, getopt
import random 


def readlines(filename):
    ifile = open(filename, 'r')
    lines = ifile.readlines()
    return lines

lins = readlines('piggydic')
    
dic = {}
for lin in lins:
    wd = lin.split('-')[0]
    mn = lin.split('-')[1]
    dic[wd] = mn
    
pstr = "random item from list is: " + random.choice(dic.values())    
val = raw_input(pstr)
print pstr

num = 0

for ww in dic.keys():
    if re.search(val, ww,re.IGNORECASE):
        num = 1

if num == 1:
    print "Bravo"
else:
    cc = "sorry, kitten, the correct answer is: "+ ww
    print ww

    


        
