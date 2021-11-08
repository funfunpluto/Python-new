#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

applel = s - a
appler = t - a
appleh = 0

for aa in apple:
    if aa > 0 and aa >= s - a and aa <= t -a:
	appleh += 1
print appleh

    
oranger = b - t
orangel = b - s
orangeh = 0

for oo in orange:
    if oo < 0 and oo >= s - b and oo <= t - b:
	orangeh += 1
print orangeh

                                                                                                                                                                                                               
