#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Calculates the maximum difference of cell values in each row and sums over rows.
# Spreadsheet data is read from ASCII file with tab separated values

with open("day2task1.txt", "r") as myFile:
    mySum = 0
    for line in myFile:
        myList = [int(i) for i in line.strip().split("\t")]
        smallest = myList[0]
        largest = myList[0]
        for i in myList[1:]:
            if i < smallest:
                smallest = i
            if i > largest:
                largest = i
        mySum += largest - smallest
    print mySum
