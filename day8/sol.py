#!/usr/bin/env python

input = [line.strip() for line in open("input").readlines()]

def run_boot_code(print_lines=False):
    already_read = []
    pos = 0
    counter = 0

    while pos not in already_read:
        i,n = input[pos].split()
        already_read.append(pos)
        if i=="acc":
            counter+=int(n)
        if print_lines:
            print(pos,"\t",input[pos],"\t",counter)
        if i=="jmp":
            pos+=int(n)
        else:
            pos+=1

    print(counter)

run_boot_code()
