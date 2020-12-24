#!/usr/bin/env/ python3

import sys
import math

if len(sys.argv) < 3:
    print ("Usage: AE.py <avg val> <terms>")
    sys.exit(0)

args = map(float, sys.argv[1:])

sum = 0.0
# N = length - avgval
N = len(args)-1

for i in range(1, len(args)):
    new_val = math.pow((args[0]-args[i]), 2)
    sum += new_val

SE = sum/(N-1)
AE = SE*1.96

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("     N = "+str(N))
print("    AE = "+str(SE))
print("    SE = "+str(AE))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
