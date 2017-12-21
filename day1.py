#!/usr/bin/env python3
# -*- coding: utf8 -*-

# [int(1000*random.random())] for i in xrange(100)]
myPuzzleInput = "1122"
myList = [int(i) for i in myPuzzleInput]
myList.append(myList[0])

sum = 0
for i in range(len(myList)-1):
	if myList[i] == myList[i+1]:
		sum = myList[i] + sum
print sum

