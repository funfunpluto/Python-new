#!/usr/bin/env python

import re, os, mysqlDB, sakaFunctions


alines = sakaFunctions.readlines('Converters/HK')

words,sakadic = sakaFunctions.lineParser(alines, '\t')


convTable = 'create table converterList (Letters varchar(255) not null, HK varchar(255), primary key (Letters));'

sakaFunctions.createTbl(convTable)

#for word in words:
#    sql = 'insert into simpleDic (words, content) values (\"'
#    sql = sql + word + '\",'
#    sql = sql + '\"' + sakadic[word] + '\");' 
#    sakaFunctions.insert2TL(sql)	




