#!/bin/python

import sys

def timeConversion(s):
    if s[-2:] == 'PM' and int(s[:2]) < 12:
        nn = str(int(s[:2]) + 12)
        ns = nn
        ns += s[2:-2]
    elif s[-2:] == 'AM' and int(s[:2]) == 12:
        ns = '00'
        ns += s[2:-2]
    else:
        ns = s[:-2]
    return ns

s = raw_input().strip()
result = timeConversion(s)
print(result)
