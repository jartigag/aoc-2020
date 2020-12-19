#!/usr/bin/env python

# mem usage:
# /usr/bin/time -v ./sol.py 2>&1 | grep Maximum
# from guppy import hpy

input = [line.strip() for line in open("input").readlines()]

def apply_mask_v1(num, mask):
    """num: str, mask: tuple (str, str)"""
    return ( int(num) | int(mask[0],2) ) &  int(mask[1],2)
    #            (num OR mask_ones)     AND mask_zeros
    #           (masking bits to 1)   (masking bits to 0)

def apply_mask_v2(addr, mask=None):
    """https://github.com/mebeim/aoc/tree/master/2020#part-2-13"""
    if mask is not None:
        addr = ''.join(a if m == '0' else m for a, m in zip(addr, mask))

    if 'X' in addr:
        yield from apply_mask_v2(addr.replace('X', '0', 1))
        yield from apply_mask_v2(addr.replace('X', '1', 1))
    else:
        yield int(addr, 2)

# initialize mem to a list of 2^16=65536 zeros? it would take too much memory..
# mem_v1 = [0]*2**16 # sys.getsizeof([0]*2**16) = 0,524352MB
# ..and 2^36=68719476736 even throws a MemError..
# mem_v2 = [0]*2**36 # sys.getsizeof([0]*2**36) = 1099.511661GB
# ..so a dict is better:
mem_v1, mem_v2 = {}, {}

for line in input:
    k,val = line.split(' = ')
    if 'mem' in k:
        addr = int(k[4:-1]) #example: k="mem[57319]" -> addr=57319

        mem_v1[addr] = apply_mask_v1(val,mask_v1)

        affected_addr = apply_mask_v2('{:036b}'.format(addr),mask_v2)
        for a in affected_addr:
            mem_v2[a] = int(val)

    elif k=='mask':
        #example: line="mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        mask_v1 =         ( "".join("1" if m=="1" else "0" for m in val),  "".join("0" if m=="0" else "1" for m in val) )
        #example: mask_v1=(   '000000000000000000000000000001000000'    ,    '000000000000000000000000000000000010'     )
        #                              mask for ones,                                 mask for zeros
        mask_v2 = val

print(sum(mem_v1.values()))
print(sum(mem_v2.values()))

# print(hpy().heap())
