#!/usr/bin/env python

import re, os, mysqlDB, sakaFunctions


alines = sakaFunctions.readlines('page10_2.xml')
aryEles = sakaFunctions.lineParser2Array(alines)


#sakaFunctions.write2txt(aryEles, 'arrayFile2')
        
#oriTable = 'create table allwords (wordID int not null auto_increment, words text, primary key (wordID));'

#mysqlDB.createTbl(oriTable) 
i = sakaFunctions.insert2allWords(aryEles)
print i

