#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Wed Feb 13 15:28:23 EST 2013
# 
# 

from sys import argv

with open(argv[1], 'r') as f:
    text = f.read()

care = text[text.index('%START%')+7:text.index('%END%')].split(' ')
[care.remove('--') for i in xrange(care.count('--'))]

[care.remove('a') for i in xrange(care.count('a'))]

[care.remove('the') for i in xrange(care.count('the'))]

print len(care)
