#!/usr/bin/env python3
# -*- coding: utf8 -*-

with open("day1task2.txt", "r") as myFile:
    myPuzzleInput = myFile.readline()

myList = [int(i) for i in myPuzzleInput.strip()]

sum = 0
for i in range(len(myList) - 1):
    if myList[i] == myList[(i + len(myList) / 2) % len(myList)]:
        sum = myList[i] + sum
print sum
