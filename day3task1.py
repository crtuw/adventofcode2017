#!/usr/bin/env python3
# -*- coding: utf8 -*-

# 1. Comments on the derivation of the mapping from the spiral coordinates to the Manhatten distance:
# ---------------------------------------------------------------------------------------------------
#   The solution is based on the existence of a functional relation between the spiral coordinate iInput and the
# circle "radius" r (the circle "radius" takes the circle number idCircle for every last element of the circle)
# e.g. 	iInput = 9:  idCircle = 1
#		iInput = 25: idCircle = 2
#
#  The number of elements of each circle can be calculated from elements of the inner adjacent circle by
# (1) nElem(idCircle) = nElem(idCircle-1) + 8 valid for all i in (2,infinity)
#
# Recursively using eq. (1) with nElem(1) = 8 leads to
# (2) nElem(idCircle) = idCircle * 8
#
# e.g.  nElem(1) = 8
#       nElem(2) = 16
#       nElem(3) = 24
#
# The total number of elements including the idCircle-th circle is given by the algorithm
#
# (3) nElemAll(idCircle)    = nElem(idCircle) + nElem(idCircle-1) + ... + nElem(2) + nElem(1) + 1
#                           = 1 + SUM { nElem(i) } with i from 1 to nCircle
#
# which can also be expressed using (2) as
#
# (4) nElemAll(idCircle)    = 1 + SUM {idCircle * 8} with i from 1 to idCircle
#                           = 1 + 8 * SUM {idCircle} with i from 1 to idCircle.
#
# Now the sum can be identified as the algorithmic relation of the arithmetic series for which the functional relation
#
# (5) SUM {idCircle} with i from 1 to idCircle = idCircle * (idCircle + 1) / 2
#
# exists. Substituting the algorithmic relation in (4) by (5) leads to
#
# (6) nElemAll(idCircle)    = 1 + 8 * idCircle * (idCircle + 1) / 2
#
# a explicit functional relation between nElemAll and idCircle. Because the functional relation of the
# arithmetic series is only of second power, the reverse function exists as the solution of the quadratic equation
#
# (7) 0    = (nCircle ** 2) + 1 * nCircle + (1 - nElemAll) * (2 / 8)
#                            \_/            \______________________/
#                             p                         q
#
# with its solution
#
# (8) idCircle = -p/2 +- sqrt(p**2 / 4 - q)
#
# considering that for idCircle > 1, q < 1/2 and hence (p ** 2 /4 - q) > 0, only the positive squares
#
# (9) idCircle = -p/2 + sqrt(p**2 / 4 - q)
#
# are considered. Because (6) is a monotonous rising function, even if nElemAll is between two circles, (9) leads to
# a nCircle between that of two circles. Therefore, the circle number is finally evaluated from input number by
# rounding (9) with (Don't forget to account for numeric errors close to nElemAll(idCircle))
#
# (10) idCircle = ceil ( -1/2 + sqrt(1 / 4 - (1 - iInput) * (2 / 8)))
#
# With (3) and (6), the number of all elements including this circle as well as the number of elements in this circle
# can be evaluated and therefore the "angle" of the element, from which by application of modulus-function, the
# Manhatten-distance can be evaluated.
#
# The approach is very efficient for large spiral coordinates, because it doesn't require loops and the
# number of operations is therefore independent of the coordinate or spiral radius.
#
# ---------------------------------------------------
#					.	.	.
#		17	16	15	14	13	.
#		18	5	4	3	12	.
#		19	6	1	2	11	.
#		20	7	8	9	10	.
#		21	22	23	24	25	26
#			/		 	 \
#   e.g. iInput	= 22	nElemAll(idCircle = 2) = 25
#		 iLocal = 12  	   nElem(idCircle = 2) = 16
#
#
# ---------------------------------------------------
# | 		figure 1: Spiral coordinates
# ---------------------------------------------------
#
# ---------------------------------------------------
#
# Distance from center of a side length
#	A
# ..|.......o...............o.......................2
#   | 		  \	 		  	  \
#	|	o		o		o		o					1
# 	|  /				  /
# 	o---------------o-------------------------------0
#  	1	2	3	4	5	6	7	8	9 ... local coordinate in a circle
#  	0	1	0	1	0	1 	0	1 	0 ... floor of division over interval num1
#	1	1	-1	-1	1	1  -1	1  -1 ... (-1) ** modulus num2
#	0	1	2	1	0	1	2	1	0 ... distance from center calculated from num1,num2,side length
# ---------------------------------------------------
# |   figure 2: Evaluation of Manhatten index
# ---------------------------------------------------

import math


def spiralCoord2manhattenDist(iInput):
	""""returns manhatten distance from spiral coordinate"""
	idCircle = int(math.ceil(-1. / 2. + math.sqrt(1. / 4. - (1. - float(iInput)) * (2. / 8.))))  # see eq. (10)
	nElemAll = 1 + 8 * idCircle * (idCircle + 1) / 2  # see eq. (6)
	nElem = idCircle * 8

	iLocal = ((nElem - (nElemAll - iInput)) - idCircle ) % nElem  # interval is 1,1,...,nElem
	num1 = (-1) ** math.floor(iLocal / idCircle)
	num2 = float(iLocal) % float(idCircle)
	num3 = float(idCircle)/2 - float(idCircle)/2 * num1 + num1 * num2
	manhatten = num3 + idCircle
	return manhatten
