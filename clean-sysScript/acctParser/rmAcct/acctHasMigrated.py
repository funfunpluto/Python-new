#!/usr/bin/python
import os, re, sys, getopt
# by Hong Zhang
"""
After a share has been migrated to other server, its associated accounts should be deleted from the original server

     1. script accept a term which is group name

     2. scripts will generate a file with commands to remove both linux accounts and samba accounts

It will skip those accounts associated also to another share that still stay in this server
"""

def main(argv):
    gpname = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["gpname="])
    except getopt.GetoptError:
        print 'account-parse.py -i <groupname>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'acctHasMigrated.py -i <groupname>'
            sys.exit()
        if opt in ("-i"):
            gpname = arg
    if not gpname:
        print 'acctHasMigrated.py -i <groupname>'
        sys.exit()
    print  '\n'

    gpfile = '/etc/group'

    grplins = get_lines(gpfile)
    # acctL for users that have left DFCI; acctE for users that still at DFCI

    for lin in grplins:
        recs = lin.split(':') 
        if gpname == recs[0]: 
              getAccts = recs[3].split(',')

    #isfile = open(gpfile, 'r')
    #content = sfile.read()
    # acctL for users that have left DFCI; acctE for users that still at DFCI
    for acct in getAccts:
        #ocrs = re.findall(acct, content,re.IGNORECASE)
        #if len(acct) > 2:
        #    print acct
        #else:
        run_command4acct(acct, '/etc/samba/smbpasswd -x', 'rmfromsmb')       
        run_command4acct(acct, ' /usr/sbin/userdel', 'rmfromlinux')       

def run_command4acct(acct, command, ofile):
    oo = open(ofile,'a')
    pcmmd = command + ' ' + acct + '\n'
    oo.write(pcmmd)
    oo.close()

def get_lines(fn):
    nfile = open(fn, 'r')
    lines = nfile.readlines()
    lins = []
    for line in lines:
        lins.append(line.strip())  
    nfile.close()  
    return lins

if __name__ == "__main__":
    main(sys.argv[1:])
