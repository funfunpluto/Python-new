#!/usr/bin/python
import os, re, sys, getopt
from datetime import date
from subprocess import Popen, PIPE
from email.mime.text import MIMEText
import csv

# by Hong Zhang

"""
statistics on share usage 
primary servers:

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

mirror servers
rc-miorr1
rc-miorr2
rc-miorr3
rc-miorr4
rc-miorr5
rc-hsm2
rc-enc2
"""

def main(argv):
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")

    cmd =  "grep data /rc/globalinfo/usage/latest/* | more"
    rfile = d4 + '.lstshareusage' 
    tocmd = cmd + ' > ' + rfile

    syscmd(tocmd)
    lins = get_lines(rfile)
    #print(lins[0])
    #print(len(lins))
 
    #wfile = d4 + '.weirdshare'
    #mfile = d4 + '.pri-mir'
    pairdcsv = d4 + 'paird.csv'
    impcsv = d4 + 'imp.csv'

    shrsize = 0
    shdict = {}

    for lin in lins:
        terms = line_parser(lin, '')
        #print terms[0], terms[2], terms[5]
        svnm = terms[0].split('.')[0]
        svnm = svnm.split('/')[-1]
        #print svnm, terms[2], terms[5]
        if terms[5] not in shdict.keys(): 
 	    shdict[terms[5]] = [[svnm, terms[2]]]
        else:
            shdict[terms[5]].append([svnm, terms[2]])
        shrsize = shrsize + 1       

        #kshare = ['labs', 'centers', 'cores', 'dept']
        #if any(x in terms[5] for x in kshare):
        #    shdict[terms[5]].append(lin)
    #print shrsize
    #print len(shdict.keys())

    paird = []
    imp =[]

    for x in shdict.keys():
        if len(shdict[x]) == 2:
            print x, shdict[x][0], shdict[x][1]
            if shdict[x][0][1] ==  shdict[x][1][1]:
                mtch = 'Y'
            else:
                mtch = 'N'
            paird.append([x, shdict[x][0], shdict[x][1], mtch]) 


#           writ2file(mfile,x)
#           for y in shdict[x]:
#               writ2file(mfile,y) 
        else:
            loclist = []
            for y in shdict[x]:
                loclist.append(y)
            imp.append([x,loclist]) 
#           writ2file(wfile,x)
#           writ2file(wfile,len(shdict[x]))
#           for y in shdict[x]:
#               #print y
#               writ2file(wfile,y)

    pfields = ['Share Name', 'Souce/Destination', 'Souce/Destination', 'Properly backup']
    write2csv(pfields, paird, pairdcsv)
    write2csv('', imp, impcsv)
    

def write2csv(fields,lst, ofncsv):

    # writing to csv file  
    with open(ofncsv, 'w') as csvfile:
    # creating a csv writer object  
        csvwriter = csv.writer(csvfile)

    # writing the fields  
        csvwriter.writerow(fields)

    # writing the data rows  
        csvwriter.writerows(lst)

def writ2file(fn, ll):
    nfile = open(fn, 'a')
    nfile.write(str(ll) + '\n')
    nfile.close() 

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
