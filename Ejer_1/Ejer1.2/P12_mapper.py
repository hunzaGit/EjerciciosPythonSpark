#!/usr/bin/python

import sys
import re

for line in sys.stdin:
	#line = 
    #line = re.sub( '"', '', line )
    words = line.split()
    print( words[6] + "\t1")