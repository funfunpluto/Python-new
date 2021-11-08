#!/usr/bin/python


import os, re, sys, getopt

def argumanager():
    ostring = ''
    nstring = ''
    dir = ''
    usage = """use word_replace.py -o old_string -n new_string -d dirname"""
    try:
        opts, protfiles = getopt.getopt(sys.argv[1:], "o:n:d:")
    except getopt.error, msg:
        print msg
        print "usage: %s %s" %(sys.argv[0], usage)
        raise sys.exit()
    for o, v in opts:
        if o == '-o':
            ostring = v
            print ostring
        if o == '-n':
            nstring = v
            print nstring
        if o == '-d':
            dir = v
    if not ostring or not dir:
        print "usage: %s %s" %(sys.argv[0], usage)
        raise sys.exit()

if __name__ == "__main__":
    argumanager()
