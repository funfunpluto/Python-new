#!/usr/bin/python2
import os, re, sys, getopt
from datetime import date
from subprocess import Popen, PIPE
from email.mime.text import MIMEText
import socket
import csv

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

    shrsize = []   
 
    hstnm = socket.gethostname()
    hstnm = hstnm.split('.')
    hstnm = hstnm[0]
    
    ofn = d4 + '_' + hstnm
    ofncsv = ofn + '.csv'
    ofile = open(ofn, 'a')
   
    #with open(ofncsv, 'wb') as csvfile:

    csvlist = []
    for lin in lins:
        terms = line_parser(lin, '')
        #print terms[0], terms[2], terms[5]
        share = terms[0].split('data/')[-1]
        svr = terms[0].split('.')
        srv = svr[0] 
        srv = srv.split('/')
        srv = srv[-1]
        if srv == hstnm and share.find('usage') == -1: 
                #print srv, terms[2], share
            acctnum = num_acct_in_share(share)
            acctnum = str(acctnum.read())
            acctnum = acctnum.strip()
            sharel = share + '\t' + terms[2] + '\t' + acctnum
            ofile.writelines(sharel) 
            csvlist.append([share,terms[2],acctnum])
    ofile.close() 
    write2csv(csvlist, ofncsv)         


def write2csv(lst, ofncsv):
    fields = ['Share Name', 'Size', 'Number of Accts']
    
    # writing to csv file  
    with open(ofncsv, 'w') as csvfile:  
    # creating a csv writer object  
        csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
        csvwriter.writerow(fields)  
        
    # writing the data rows  
        csvwriter.writerows(lst) 


def num_acct_in_share(grp):
    cmd = "grep " + grp + ' /etc/passwd | wc -l'
    ss = os.popen(cmd)
    return ss


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
