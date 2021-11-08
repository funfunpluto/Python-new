#!/bin/python

import sys


def kangaroo(x1, v1, x2, v2):
    if (v1 - v2) > 0  and (x2 - x1) % (v1 - v2) == 0:
        result ='Yes'
    else:
        result = 'No'
    return result

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

