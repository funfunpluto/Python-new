#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))

mi = sum(arr) - max(arr)
ma = sum(arr) - min(arr)

aa = str(mi)
aa += ' '
aa += str(ma)

print aa
