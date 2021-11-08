#!/bin/python

import sys

def solve(grades):
    # Complete this function
    ngrades = []
    for g in grades:
    	rr = g % 5 
    	print rr
        if g >= 38 and rr >= 3:
	   ng = g + 5 - rr 
        else:
           ng = g
        ngrades.append(ng)
    return ngrades

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
