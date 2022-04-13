#!/usr/bin/python2
import os, re, sys, getopt
from datetime import date
from subprocess import Popen, PIPE
from email.mime.text import MIMEText


# by Hong Zhang

"""
statistics on share usage 
"""

def main(argv):
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")

    cmd =  "grep data /rc/globalinfo/usage/latest/* | more"
    rfile = d4 + '.lstshareusage' 
    tocmd = cmd + ' > ' + rfile

    syscmd(tocmd)
    lins = get_lines(rfile)
    print(lins[0])
    print(len(lins))

    shrsize = []   
 

    for lin in lins:
        size = 0.0
        terms = line_parser(lin, '')
        #print terms[0], terms[2], terms[5]
        svr = terms[0].split('.')
        srv = svr[0] 
        srv = srv.split('/')
        srv = srv[-1]
        print srv, terms[2], terms[5]

def get_lines(fn):
    nfile = open(fn, 'r')
    lines = nfile.readlines()
    lins = []
    for line in lines:
        lins.append(line.strip())
    return lins

def line_parser(line,splt):
    if splt == '':
        terms = line.split()
    else:
        terms = line.split(splt)
    #nm = terms[4].split(' ')
    #nm = nm[0]
    return terms

def syscmd(cmd):
    os.system(cmd)


if __name__ == "__main__":
    main(sys.argv[1:])
