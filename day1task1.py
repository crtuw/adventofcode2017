#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Sums all digits which have the same digit in subsequent position assuming the linear string is a closed loop
# The string is read from an ASCII file with the string in the first line.

with open("day1task1.txt", "r") as myFile:
    myPuzzleInput = myFile.readline()

myList = [int(i) for i in myPuzzleInput]
myList.append(myList[0])

sum = 0
for i in range(len(myList) - 1):
    if myList[i] == myList[i + 1]:
        sum = myList[i] + sum
print sum
