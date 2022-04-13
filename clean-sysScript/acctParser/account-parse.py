#!/bin/python
import os, re, sys, getopt


def main(argv):
    inputfile = ''
    searchterm = ''
    try:
        opts, args = getopt.getopt(argv,"hi:s:",["ifile=","search="])
    except getopt.GetoptError:
        print 'account-parse.py -i <inputfile> -s <searchterm>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'account-parse.py -i <inputfile> -s <searchterm>'
            sys.exit()
        if opt in ("-i", "--ifile"):
            inputfile = arg
        if opt in ("-s", "--searchterm"):
            searchterm = arg
    if not inputfile or not searchterm:
	print 'account-parse.py -i <inputfile> -s <searchterm>'
        sys.exit()
    print searchterm
    print  '\n'
    getlines = get_lines(inputfile,searchterm)
    for line in getlines:
        accts = get_group_users(line)
        for acct in accts:
	    lins = get_lines('/etc/passwd',acct)
	    print "lins: ", lins
	    uname, dfid, fullname = line_parser(lins)
            print uname + ':', dfid + ':' , fullname

def get_lines(fn,tm):
    nfile = open(fn, 'r')
    lines = nfile.readlines()
    lins = []
    for line in lines:
	if re.search(tm, line):
	    lins.append(line)
    return lins

def get_group_users(lin):
    print 'lin: ', lin, type(lin)
    usrs = lin.split(':')  
    usrs = usrs[-1]
    accts = usrs.split(',')
    return accts    

def line_parser(line):
    terms = line.split(":")
    nm = terms[4].split(' ')
    nm = nm[0]
    return terms[0], terms[2], nm


if __name__ == "__main__":
    main(sys.argv[1:])
