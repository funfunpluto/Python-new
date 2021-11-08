#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    ma = max(ar)
    nn = ar.count(ma)
    return nn

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
