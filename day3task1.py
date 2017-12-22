#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Rekursion für konzentrische Kreise:
# n[i] = n[i-1] + 8
# n[i] = 8 + n[i-1] + 8 = (i-1)*8 + 8
#
# n[2] = 16
#
# N[i] = n[i]  + n[i-1]   + n[i-2] + ... + n[2] + n[1] + 1
#      = 1 * 8 + 2*n[i-1] + n[i-2] + ... + n[2] + n[1] + 1
#      =                  sum_1^(i-1)(k) * 8  +  (i-1) * n[1]  + n[1] + 1
# N[2] = sum(1) * 8 + 1*8 + 8 + 1 = 25
# N[3] = sum(1,2) * 8 + 2*8 + 8 + 1 = 49
#
# i:           1 2 3  4  5  6  7 ...
# sum_1^i (k): 1 3 6 10 15 21 28 ... = i*(i+1)/2 arithmethische Folge
#
# N[i] = sum_1^(i-1)(k) * 8  +  (i-1) * n[1]  + n[1] + 1
#      = (i*(i+1)/2 - i)  * 8     +  (i-1) * n[1]  + n[1] + 1
#      = (i*(i+1)/2 - i)  * 8     +  (i-1) * n[1]  + n[1] + 1
#      = (i^2/2-i/2)      * 8     +  (i-1) * n[1]  + n[1] + 1
#      = (i^2)*(1/2)*8 + i*(-(1/2)*8 + 8) + 1
# 0    = (i^2)*4 + i*4 + 1 - N[i]
# 0    = (i^2)   + i   + (1 - N[i])/4
# i = - p/2 +- sqrt(p^2/4 - q)
# i = -1/2 + sqrt(1/4 - 1/4 + N[i]/4)
import math

Ni = 10
# TODO: Toleranz für das runden
k = int(math.ceil(-1. / 2. + (1. / 4. - 1. / 4. + float(Ni) / 4.) ** (1. / 2.)))
nSchale = (k - 1) * 8 + 8
Nkm1 = (k * (k - 1) / 2 - k + 1) * 8 + (k - 2) * 8 + 8 + 1


# TODO: Hier ist noch einiges falsch
deltaN = Ni - Nkm1 -1
deltaN = range(24)
num1 = [i % (nSchale / 4) for i in deltaN]
num2 = [-(-1)**(i / (nSchale / 8)) for i in deltaN]
num3 = [nSchale/16+num1[i]*num2[i] for i in range(length(deltaN))]
num4 = num3 + nSchale/8
