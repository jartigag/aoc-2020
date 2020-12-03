#!/usr/bin/env python3
import sys
if len(sys.argv)<2: print("usage: ./sol.py incr_x incr_y"); sys.exit()

input = [line.strip() for line in open("input").readlines()]
path = []

incr_x,incr_y = int(sys.argv[1]), int(sys.argv[2])

for i in range(incr_x,len(input),incr_x):
    path.append(input[i][ int(i/incr_x)*incr_y % len(input[i]) ])

print( path.count('#') )
