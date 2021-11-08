#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pp = 0.0
nn = 0.0
zz = 0.0

for i in range(0,n):
    if arr[i] > 0:
        pp = pp + 1.0
    elif arr[i] == 0:
        zz = zz + 1.0
    else:
        nn = nn + 1.0
 
print pp/n
print nn/n
print zz/n
