#!/usr/bin/env python

input = open("input").read().split("\n\n")

sumA = 0
for i in input:
    sumA+=len(set(i.replace("\n","")))

print(sumA)

sumB = 0
for i in input:
    for a in set(i.replace("\n","")):
        if all(a in w for w in i.split()):
            sumB+=1

print(sumB)
