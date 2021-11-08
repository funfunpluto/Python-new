#!/usr/bin/env python

import xlrd, sys, argparse
from argparse import ArgumentParser

reload(sys)
sys.setdefaultencoding( "utf8" )


def xl2txt(ifn, ofn):
    reload(sys)
    sys.setdefaultencoding( "utf8" )
    workbook = xlrd.open_workbook(ifn, on_demand = True)
    sheet = workbook.sheet_by_index(0) #by the index it has in excel's sheet collection

    r = sheet.row(0) #returns all the CELLS of row 0,
    c = sheet.col_values(0) #returns all the VALUES of row 0,


    ofile = open(ofn, 'a')

    for i in xrange(sheet.nrows):
    	line = ''
   	for j in range(sheet.ncols):
            print sheet.row_values(i)[j]
            #ii = sheet.row_values(i)[j]
            #jj = ii.encode(
            item = str(sheet.row_values(i)[j])
	    item = item.replace(':', ' -')
            print item
            line += item
            line += '\t'
    	line += '\n'
    	ofile.write(line)

    ofile.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", dest="infile", help="input excel file", metavar="[input excel file]", required=True)    
    parser.add_argument("-o", "--outfile", dest="ofile", help="write to text file", metavar="[output text file]", required=True)    
    args = parser.parse_args()
    xl2txt(args.infile, args.ofile)
