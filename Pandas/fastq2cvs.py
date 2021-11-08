#!/usr/local/bin/python3

import os, sys, getopt
import pandas as pd


def argumanager():
    fn = ''
    usage = """use ./fastq2csv.py -f filename"""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:h",['fname='])
    except getopt.GetoptError as msg:
        print(msg)
        usg = "usage: %s %s" %(sys.argv[0], usage)
        print(usg)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-f':
            fn = arg
    if not fn:
        print("please provide a file name after ./fastq2csv.py -f filename")
        print("usage: %s %s" %(sys.argv[0], usage))
    else:
        lines = readlines(fn)
        #print(len(lines))
        eFastq, fFastq = parser2zipfastq(lines)
        izyfile = 'easyFasta.csv'
        #list2csv(eFastq, izyfile)
        df = readCsv(izyfile, ['Key','Seq'])     
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
