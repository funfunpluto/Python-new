#!/bin/python

import sys


n = int(raw_input().strip())

pond = ''
for i in range(n):
    for j in range(1,n-i):
	pond += ' '
    
    for m in range(i+1):
    	pond += '#'
    print pond
    pond = ''
