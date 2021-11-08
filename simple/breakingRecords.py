#!/bin/python

import sys

def getRecord(s):
    # Complete this function
    mx = 0
    mi = 0
    for i in range(1,len(s)):
        if max(s[:i]) < s[i]:
            mx += 1
        if min(s[:i]) > s[i]:
            mi += 1
    return mx, mi 

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
