#!/usr/bin/python

import sys
import re


# Date,Open,High,Low,Close,Adj Close,Volume
# 2008-12-31,151.117126,154.495163,150.327271,152.830978,152.830978,5811000

for line in sys.stdin:
	words = re.split(',', line)
	anyo = re.split('-', words[0])[0]
	print( anyo  + "\t" +  words[4])