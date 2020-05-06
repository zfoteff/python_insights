#!/usr/bin/env/ python3

import sys
import math

if len(sys.argv) < 3:
    print ("Usage: AE.py <avg val> <terms>")
    sys.exit(0)

args = map(float, sys.argv[:])

sum = 0.0
N = len(args)-1

for i in range(1, len(args)):
    new_val = math.pow((float(args[0])-float(args[i])), 2)
    sum += new_val

sum = sum/N

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("    N ="+str(N))
print("    AE ="+str(sum))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
