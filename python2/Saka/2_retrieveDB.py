#!/usr/bin/env python

import re, os, sakaFunctions

items = sakaFunctions.retrievDBSim(38)
fn = 'allwords2_10.txt'

#print type(items[1])

sakaFunctions.write2txt(items, fn)
