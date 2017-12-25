#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Considering spiral coordinates greater than 10, the new value is gained from the following algorithm
# (1) add the value of the previous element (spiral coordinate -1)
# (2) add the values of the elements of spiral coordinates difference of add=[-delta+1 -delta -delta-1]
# (3) after the direction changed
# 		(3a) add value from spiral coordinate [-2]
#		(3b) add -2 to delta, hence delta -= 1
#		(3c) omit value from -delta-1
#		(3d) add lower element of triad
# (4) if 1 from boundary, omit lower element of triad
# (5) if 0 from boundary, omit lower 2 elements of triad
#

# TODO: Management of number of stored elements in 'values'; pop elements of inner circles

valueMax = 312051
values = [1, 1, 2, 4, 5, 10, 11, 23, 25, 26, 54, 57, 59, 122, 133, 142, 147, 304, 330, 351, 362, 747, 806]
walk = 2
boundary = 5
add = [-16, -15, -14]
direction = [1, 0]
# while True:								# Loop until value > valueRef
while True:
	walk += 1
	newValue = values[-1]  # (1)
	if (boundary - walk) == 1:
		add.pop(-1) # (4)
	elif (boundary - walk) == 0:
		add.pop(-1) # (5)
		walk = 0
		direction = direction[::-1]  # Turn direction by 90 degree
		direction[1] *= -1
		if abs(direction[0]) == 1:  # new direction in x -> change boundary
			boundary += 1
	elif walk == 1:
		add = [i - 2 for i in add]
		add.append(add[-1] + 1)
		add.append(add[-1] + 1)
		add.pop(0)
		newValue += values[-2]
	elif walk == 2:
		add.insert(0, add[0] - 1)

	newValue += sum([values[i] for i in add])
	values.append(newValue)

	if newValue >= valueMax:
		print len(values)
		break
