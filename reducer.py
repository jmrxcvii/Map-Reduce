#!/usr/bin/env python
import sys

wordCount = {}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    try:
        wordCount[word] = wordCount[word] + count
    except:
        wordCount[word] = count

    for word in wordCount.keys():
        #print '%s\t%s' % (word, wordCount[word])
        print(word, wordCount[word])