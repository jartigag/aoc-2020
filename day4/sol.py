#!/usr/bin/env python3

input=open("input").read().split("\n\n")

def validate_minmax(val,min,max,digits=0):
    base=16 if any(c in val for c in 'abcdef') else 10
    if min<=int(val,base)<=max:
        if digits:
            if len(val)==digits:
                return True
        else:
            return True
    return False

def get_val(field,line):
    return line.split(field)[1].split()[0]

valid=0

for passport in input:

    if all(f in passport for f in ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']):

        #valid+=1; continue #solution1

        if      validate_minmax(get_val('byr:',passport),1920,2002,4) \
            and validate_minmax(get_val('iyr:',passport),2010,2020,4) \
            and validate_minmax(get_val('eyr:',passport),2020,2030,4):

            if         ( 'cm'==get_val('hgt:',passport)[-2:] and validate_minmax(get_val('hgt:',passport)[:-2],150,193) ) \
                    or ( 'in'==get_val('hgt:',passport)[-2:] and validate_minmax(get_val('hgt:',passport)[:-2],59,76) ):

                if '#'==get_val('hcl:',passport)[0] and validate_minmax(get_val('hcl:',passport)[1:],0x000000,0xffffff,6):

                    if any(c in get_val('ecl:',passport) for c in ['amb','blu','brn','gry','grn','hzl','oth']):

                        if get_val('pid:',passport).isnumeric() and validate_minmax(get_val('pid:',passport),0,999999999,9):

                            valid+=1

print(valid)
