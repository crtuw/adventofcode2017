#!/usr/bin/env python3
# -*- coding: utf8 -*-

with open("day1task1.txt", "r") as myFile:
    myPuzzleInput = myFile.readline()

myList = [int(i) for i in myPuzzleInput]
myList.append(myList[0])

sum = 0
for i in range(len(myList) - 1):
    print i
    if myList[i] == myList[i + 1]:
        sum = myList[i] + sum
print sum
