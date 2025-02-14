#!/usr/bin/env python
import sys

special = ("~`!@#$%^&*()_-+={[]}|\\:;'\",<.>/?0123456789")

for line in sys.stdin:
    line = line.strip()
    line = line.strip("~`!@#$%^&*()_-+={[]}|\\:;'\",<.>/?0123456789")
    for c in special:
        line = line.replace(c, ' ')

    words = line.split()

    for word in words:
        #print '%s\t%s' % (word, "1")
        print(word, "1")
