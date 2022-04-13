#!/usr/bin/python
import os, re, sys, getopt
from datetime import date
from subprocess import Popen, PIPE
from email.mime.text import MIMEText
# by Hong Zhang

"""
cron job on:
rc-data1
rc-data2
rc-data3
rc-stor2
rc-stor4
rc-stor5
rc-stor8
rc-stor9
rc-stor14
rc-stor15
rc-stor16
rc-enc1

Errors may occur when:
1. user id does not match with its gid (not sure how it could happen)
2. we may find that user accounts/groups were never removed when the shares are migrated or deleted

"""
def main(argv):
    pswfile = '/etc/passwd'
    grpfile = '/etc/group'
    searchfile = '/local/scripts/useradd/DFCI_PEOPLE.txt'
    hstnm = os.uname()[1]
    hstnm = line_parser(hstnm,'.')
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")
    dirname = '/rc/globalinfo/acct-left-dfci/' + d4
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    wfile = dirname + '/' + hstnm[0] + '.acct2del'

    getacclins = get_lines(grpfile) # collect records from /etc/group
    getinfolins = get_lines(pswfile) # collect records from /etc/passwd
    hrlists = get_lines(searchfile)  # collect records from HR data sheet
    stopstr = ['nfsnobody', 'lab', 'adm', 'admin', 'prg']    
    warry = []
   
    for getacclin in getacclins:
        print "getacclin: ", getacclin
        grpinfo  = line_parser(getacclin,':')
        print "grpinfo: ", grpinfo
        if len(grpinfo) > 3:
            acct, uuid, lst  = grpinfo[0], grpinfo[2], grpinfo[-1]
            if lst == '' and len(uuid) > 3 and len(uuid) < 6: 
                if not any(x in acct for x in stopstr):
                    i = 0
                    for hrlist in hrlists:
                        if re.search(uuid, hrlist,re.IGNORECASE): 
                            i = i + 1
                            rr = hrlist
                    if i == 0:
                        matching = [s for s in getinfolins if uuid in s]
                        print "matching: ", matching
                        acctinfos = line_parser(matching[0],':')
                        usrnm, uuid, ful, pth =  acctinfos[0], acctinfos[2], acctinfos[4], acctinfos[5]
                        wstr =  usrnm + '\t' +  uuid + '\t' + ful +  '\t' + pth  + '\n'
    			warry.append(wstr)		
    if len(warry) > 0:			
        ww = open(wfile, "a") 
        for warr in warry:
            ww.write(warr)
        ww.close()
        mailsubject = hstnm[0] + ' has obsolete user accounts'
        email2admin('hong_zhang@dfci.harvard.edu',wfile, mailsubject)    
        #email2admin('Douglas_Buell@dfci.harvard.edu',wfile, mailsubject)    
    else:
        sys.exit()
 
def email2admin(rcpt,sfile,sub):
    with open(sfile) as fp:
        body = fp.read()
    msg = MIMEText(body)
    msg["Subject"] = sub
    msg["To"] = rcpt
    msg["From"] = "root@rc-stor2.dfci.harvard.edu"
    p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
    p.communicate(msg.as_string())

def get_lines(fn):
    nfile = open(fn, 'r')
    lines = nfile.readlines()
    lins = []
    for line in lines:
        lins.append(line.strip())    
    return lins

def line_parser(line, splt):
    terms = line.split(splt)
    #nm = terms[4].split(' ')
    #nm = nm[0]
    return terms

if __name__ == "__main__":
    main(sys.argv[1:])
