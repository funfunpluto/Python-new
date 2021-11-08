#!/usr/bin/env python

import re, os, mysqlDB, sakaFunctions


alines = sakaFunctions.readlines('Pages/1_9page')

words,sakadic = sakaFunctions.lineParser(alines, '&apos;')

print words



smplDicTable = 'create table simpleDic (wordID int not null auto_increment, words varchar(255) not null, content text, primary key (wordID));'

sakaFunctions.createTbl(smplDicTable)

for word in words:
    sql = 'insert into simpleDic (words, content) values (\"'
    sql = sql + word + '\",'
    sql = sql + '\"' + sakadic[word] + '\");' 
    sakaFunctions.insert2TL(sql)	




