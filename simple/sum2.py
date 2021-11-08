#! /usr/bin/env python

import sys

def simpleArraySum(n, ar):
    r = 0
    for i in range(0,n):
	r = r + ar[i]
    return r


n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
