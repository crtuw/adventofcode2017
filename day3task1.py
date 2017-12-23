#!/usr/bin/env python3
# -*- coding: utf8 -*-

# 1. Comments on the derivation of the mapping from the spiral coordinates to the Manhatten distance:
# ---------------------------------------------------------------------------------------------------
#   The solution is based on the existence of a functional relation between the spiral coordinate iInput and the
# circle "radius" r (the circle "radius" takes the circle number idCircle for every last element of the circle)
#
#  The number of elements of each spiral can be calculated from elements of the inner adjacent spiral by
# (1) nElem(idCircle) = nElem(idCircle-1) + 8 valid for all i in (1,infinity)
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
# which can also be expressed using (2) as
# (4) nElemAll(idCircle)    = 1 + SUM {idCircle * 8} with i from 1 to idCircle
#                           = 1 + 8 * SUM {idCircle} with i from 1 to idCircle.
#
# Now the sum can be identified as the algorithmic relation of the arithmetic series for which the functional relation
#
# (5) SUM {idCircle} with i from 1 to idCircle = idCircle * (idCircle + 1) / 2
# which leads to
#
# (6) nElemAll(idCircle)    = 1 + 8 * idCircle * (idCircle + 1) / 2
#
# Because the functional relation of the arithmetic series is only of second power, the reverse function exists as the
# solution of the quadratic equation
#
# (7) 0    = (nCircle ** 2) + 1 * nCircle + (1 - nElemAll) * (2 / 8)
#                            \_/            \______________________/
#                             p                         q
#
# with the solution
#
# (8) nCircle = -p/2 +- sqrt(p**2 / 4 - q)
#
# considering that for ifCircle > 1, q < 1/2 and hence (p**2 / 2 - q) > 0, only the positive squares
#
# (9) nCircle = -p/2 + sqrt(p**2 / 4 - q)
#
# are considered. Because (6) is monotonous rising function, even if nElemAll is between two circles, (9) leads to
# a nCircle between that of two circles. Therefore, the circle number is finally evaluated from input number by
# rounding (9) with (Don't forget to account for numeric errors close to nElemAll(nCircle))
#
# (10) nCircle = ceil ( -1/2 + sqrt(((1 - iInput) * (2 / 8))**2 / 4 - q))
#
# With (3) and (6), the number of all elements including this circle as well as the number of elements in this circle
# can be evaluated and therefore the "angle" of the element, from which by application of modulus, the
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
#				/		 \
#     e.g. iInput		nElemAll(idCircle = 2) = 25
#						nElem(idCircle = 2) = 16
#
# ---------------------------------------------------
# | 		figure 1: Spiral coordinates
# ---------------------------------------------------


import math

Ni = 10
# TODO: tolerance for rounding, revise variable names and simplify code
k = int(math.ceil(-1. / 2. + (1. / 4. - 1. / 4. + float(Ni) / 4.) ** (1. / 2.)))
nSchale = (k - 1) * 8 + 8
Nkm1 = (k * (k - 1) / 2 - k + 1) * 8 + (k - 2) * 8 + 8 + 1

# TODO: evaluate "angle" and Manhatten radius by mapping to periodic function and application of modulus operator
# deltaN = Ni - Nkm1 - 1
# deltaN = range(24)
# num1 = [i % (nSchale / 4) for i in deltaN]
# vnum2 = [-(-1) ** (i / (nSchale / 8)) for i in deltaN]
# num3 = [nSchale / 16 + num1[i] * num2[i] for i in range(length(deltaN))]
# num4 = num3 + nSchale / 8
