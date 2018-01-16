#!/usr/bin/python

import sys
import re


# Date,Open,High,Low,Close,Adj Close,Volume
# 2008-12-31,151.117126,154.495163,150.327271,152.830978,152.830978,5811000

for line in sys.stdin:
	words = re.split(',', line)
	print( words[0]  + "\t" +  words[4])

	


'''
for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r"\W+", line)
    
    for word in words:
        print( word.lower() + "\t1" )
'''