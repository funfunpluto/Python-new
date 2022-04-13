#!/usr/bin/python3
#import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument("echo", help="test")

#help="Usage:  ./4-make-adduser-with-group.py  -g <name of lab group> -f <facility type> -s <search string> -a [User is admin for shares] -p [User is PI]")
#args = parser.parse_args(['echo'])
#print(args)

import os, sys, getopt

def argumanager():
    uniqueStr = ''
    gname = ''
    facility = ''
    usage = """use ./4-make-adduser-with-group.py -g groupname -f facility -s uniqueStr """    
    dbfile = '/local/scripts/useradd/DXXX_PEOPLE.txt'
    pwfile = '/etc/passwd'
    gpfile = '/etc/group'
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "g:f:s:h",['uniqueStr=', 'gname=', 'facility='])
    except getopt.GetoptError as msg:
        print(msg)
        usg = "usage: %s %s" %(sys.argv[0], usage)
        print(usg) 
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-g':
            gname = arg
        if opt ==  '-f':
            facility = arg
        if opt == '-s':
            uniqueStr = arg
    if not uniqueStr:
        print("a unique string is necessary for search")
        print("usage: %s %s" %(sys.argv[0], usage))
        sys.exit(2) 
    if not gname:
        print("please provde group name after -g")
        print("usage: %s %s" %(sys.argv[0], usage))
        sys.exit(2) 
    if not facility:
        print("please select labs, depts, or centers")
        print("usage: %s %s" %(sys.argv[0], usage))
        sys.exit(2) 
    else:     
        searchdb =  searchFile(uniqueStr,dbfile)
        if searchdb == 1:
            searchpw = searchFile(uniqueStr, pwfile)
            searchgp = searchFile(gname, gpfile)
            if searchgp == 0:
                print("group not exist; please create it first")               
            elif searchpw == 0:
                ptnid, dfciid, name, phone, email, desc, loc = parseStr(uniqueStr, dbfile)
                print("/usr/sbin/useradd -u %s -b /%s/%s/homes -c \"%s, %s, %s, %s, %s\" %s" %(dfciid, facility, gname, name, email, desc, loc, phone, ptnid.lower()))
                print( "/usr/sbin/usermod -a -G %s %s" %(gname, ptnid.lower()))
            else:
                print("user account exists")
 
def searchFile(term,fname):
    rfile = 'sresult'
    cmd = "grep -i %s %s > %s" %(term,fname,rfile)
    os.system(cmd)
    found = 0
    if os.stat(rfile).st_size == 0:
        print("Search string %s not find in %s" %(term, fname))
    else:
        found = 1
    os.system("rm %s" %(rfile))
    return found

def parseStr(term, fname):
    rfile = 'sresult'
    cmd = "grep -i %s %s > %s" %(term,fname,rfile)
    os.system(cmd)
    ff =  open(rfile, 'r')
    line = ff.readline().strip()
    ff.close()
    os.system("rm %s" %(rfile))
    item = line.split(':')
    tnum = item[0].replace("/","-")
    dfciid = item[1]
    name = item[2][1:-1]
    uname = item[3]
    email = item[4]
    desc = item[5]
    loc  = item[6]
    return uname, dfciid, name, tnum, email, desc, loc

if __name__ == "__main__":
    argumanager()


