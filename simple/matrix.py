#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
d1 = 0
d2 = 0
for i in range(0,n):
    for j in range(0,n):
        if i == j:
            d1 = d1 + a[i][j]
            
        if j + i== n - 1:
            d2 = d2 + a[i][j]
print abs(d1-d2)
