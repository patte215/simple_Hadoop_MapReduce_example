#!/usr/bin/env python
import sys
import re


# get all lines from stdin
for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()
    
    # make lower case
    line = line.lower()

    # split the line into words; splits on any whitespace
    words = line.split()
    
    # remove punctuation
    s = "string. With. Punctuation?"
    s = re.sub(r'[^\w\s]','',s)

    # output tuples (word, 1) in tab-delimited format
    stopwords = set(['the', 'i', 'and', 'to', 'of', 'you', 'a', 'my', 'in', 'is'])

    for word in words:
        if word not in stopwords:
         print '%s\t%s' % (word, "1")
