#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Calculates evenly divisible values of cells of a row and sums over all rows.
# Spreadsheet data is read from ASCII file with tab separated values

with open("day2task2.txt", "r") as myFile:
    mySum = 0
    for line in myFile:
        myList = [int(i) for i in line.strip().split("\t")]
        boolFinish = False
        for i in range(len(myList)):
            for j in range(0, i) + range(i + 1, len(myList)):
                if myList[i] % myList[j] == 0:
                    mySum = mySum + myList[i] / myList[j]
                    boolFinish = True
                    break
            if boolFinish == True:
                break

    print mySum