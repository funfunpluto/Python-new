#!/usr/local/bin/python3

import os, sys, getopt
import pandas as pd


def argumanager():
    exploits = []
    outfile = None
    if len (sys.argv) != 7:
        print ("Usage: ./compareHoldingChange.py -o <last-month> -n <this month> -r <result>")
        print ("Note: <exploits> can be 'all' or a list of exploits seperated by ','")
        exit (1)
    opts, args = getopt.getopt(sys.argv[1:], 'o:n:r:')
    for k, v in opts:
        if k == '-o':
            ofile = v
        if k == '-n':
            nfile = v
        if k == '-r':
            rfile = v
    print(ofile, nfile, rfile)
    #else:
    #    lines = readlines(fn)
    #    #print(len(lines))
    #    eFastq, fFastq = parser2zipfastq(lines)
    #    izyfile = 'easyFasta.csv'
    #    #list2csv(eFastq, izyfile)
    #    df = readCsv(izyfile, ['Key','Seq'])     
        #print(df.tail())
        #print(df.info())

def readlines(filename):
    ifile = open(filename, 'r')
    lines = ifile.readlines()
    ifile.close()
    return lines

def parser2zipfastq(lines):
    keys = []
    seqs = []
    options = []
    quals = []
    for i in range(int(len(lines)/4)):
        key = lines[i*4].split()[0]
        seq = lines[i*4+1]
        option = lines[i*4+2]
        qual = lines[i*4+3]
        keys.append(key)
        seqs.append(seq)
        options.append(option)
        quals.append(quals)
    easyFastq = zip(keys, seqs)
    fullFastq = zip(keys, seqs, options, quals) 
    return easyFastq, fullFastq


def list2csv(zip, filename):
    dataset = list(zip)
    df = pd.DataFrame(data = dataset)
    df.to_csv(filename, index=False,header=False)
        
def rmfile(fname):
    os.remove(fname)


def readCsv(fname, tags):
    df = pd.read_csv(fname, names = tags)
    return df
    

if __name__ == "__main__":
    argumanager()
