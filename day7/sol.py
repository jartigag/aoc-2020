#!/usr/bin/env python

input = [line.strip() for line in open("input").readlines()]

rules = {}

for line in input:
    k,v = line.split(' contain ')
    rules[k] = v.replace('.','').split(', ')

eventually_shiny_gold_bag_containers = set()

def find_containers(target):
    for bag in rules:
        if any(target in bagrules for bagrules in rules[bag]):
            eventually_shiny_gold_bag_containers.add(
                    bag.rstrip('s') # pluralsssss
            )
            find_containers(bag.rstrip('s')) # recursion!

find_containers('shiny gold')

print( len(eventually_shiny_gold_bag_containers) )
