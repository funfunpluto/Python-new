#!/bin/python

import sys

def getTotalX(a, b):
    # Complete this function
    mi = int(max(a))
    mx = int(min(b))
    x = 0

    if mx < mi:
	x = 0
    else:
        for q in range(mi, mx+1):
            if all(q % aa == 0 for aa in a) and all (bb % q == 0 for bb in b):
		x += 1
    return x 
    
if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    total = getTotalX(a, b)
    print total

