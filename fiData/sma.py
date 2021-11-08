#! /usr/local/bin/python3
##https://stackoverflow.com/questions/42553891/function-for-simple-moving-average-sma/42554266#42554266

from collections import deque
import itertools

def moving_average(iterable, n=3):
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable) 
    # create an iterable object from input argument
    d = deque(itertools.islice(it, n-1))  
    # create deque object by slicing iterable
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n

# example on how to use it
for i in  moving_average([40, 30, 50, 46, 39, 44]):
    print(i)
