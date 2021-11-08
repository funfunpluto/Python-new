#!/usr/bin/python

import os, re, sys, pyTools, getopt

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
    if os.path.isdir(dir):
        items = os.listdir(dir)
        print items
        for item in items:
            item = dir + item
            if os.path.isdir(item):
                print item, "is a directory"
            elif os.path.isfile(item):
                replace_file_term(item, nstring, ostring)

def dir_manipulation(input):
    if os.path.isdir(input):
        items = os.listdir(input)
    return items
    
def replace_file_term(filename, nstring, ostring):
    content = open(filename, 'r').read()
    omatch = re.search(ostring, content)
    if omatch:
        ofile = filename + '.old'
        os.rename(filename, ofile)
        lines = pyTools.readlines(ofile)
        nfile = open(filename, 'a')
        for line in lines:
            line = line.replace(ostring,nstring)
            nfile.write(line)
        nfile.close()
               
if __name__ == "__main__":
    argumanager()
