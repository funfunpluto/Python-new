#!/usr/bin/python3
import os, re, sys, getopt
from datetime import date
from subprocess import Popen, PIPE
from email.mime.text import MIMEText
from statistics import mean, median, median_low, median_high, median_grouped, mode


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
        if re.search('T', terms[2]):
            size = float(terms[2][:-1]) * 1000000.0
        elif re.search('G', terms[2]):    
            size = float(terms[2][:-1]) * 1000.0
        elif re.search('M', terms[2]):
            size = float(terms[2][:-1])
        else:        
            size = 0.0
        shrsize.append(size)

    avg =  "The average usage of shares: " + str(mean(shrsize))
    medn =  "The median usage of shares: " + str(median(shrsize))
    lmedn =  "The lower median usage of shares: " + str(median_low(shrsize))
    hmedn =  "The higer median usage of shares: " + str(median_high(shrsize))
    gmedn =  "The median grouped usage of shares: " + str(median_grouped(shrsize))
    md =  "The mode usage of shares: " + str(mode(shrsize))
     
    print(avg)
    print(medn)            
    print(lmedn)            
    print(hmedn)            
    print(gmedn)            
    print(md)            

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
