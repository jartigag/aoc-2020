#!/usr/bin/env python3
import math

input = [line.strip() for line in open("input").readlines()]

nav_instructions = [ {'goto': l[0], 'units': int(l[1:])} for l in input ]

cardinal2deg = {
         'N': 0,
'W': 270,         'E': 90,
         'S': 180}

def move(obj, dir, units):
    #TODO: too much hacky?
    if str(dir).isnumeric(): # so direction is determined by degrees (a cardinal point)
        if dir==0:
            obj['y'] += units
        elif dir==180:
            obj['y'] -= units
        elif dir==90:
            obj['x'] += units
        elif dir==270:
            obj['x'] -= units
    elif len(dir)==2: # so direction is determined by x,y coords (the waypoint)
        obj['x'] += dir['x']*units
        obj['y'] += dir['y']*units
    return obj

def rotate_waypoint(w, deg):
    #TODO: generalize
    if deg==90:
        w['x'],w['y'] = w['y'],-w['x']
    elif deg==180:
        w['x'],w['y'] = -w['x'],-w['y']
    elif deg==270:
        w['x'],w['y'] = -w['y'],w['x']
    return w

def next_step(ship, instruction, waypoint=None):

    if instruction['goto'] in ('L','R'):
        s = -1 if instruction['goto']=='L' else 1
        if not waypoint:
            ship['dir'] = (ship['dir'] + s*instruction['units'])%360
        else:
            waypoint = rotate_waypoint(waypoint, (s*instruction['units'])%360)

    elif instruction['goto'] in cardinal2deg.keys():
        target = ship if not waypoint else waypoint
        target = move(target, cardinal2deg[instruction['goto']], instruction['units'])

    elif instruction['goto']=='F':
        ship = move(ship, ship['dir'] if not waypoint else waypoint, instruction['units'])

    if not waypoint:
        return ship
    else:
        return ship, waypoint

ship = {'dir': cardinal2deg['E'], 'x': 0, 'y': 0}

for instr in nav_instructions:
    ship = next_step(ship, instr)

print(f"ship={ship}. manhattan distance={abs(ship['x']) + abs(ship['y'])}" )

ship = {'dir': 'E', 'x': 0, 'y': 0}
waypoint = {'x': 10, 'y': 1}

for instr in nav_instructions:
    ship, waypoint = next_step(ship, instr, waypoint)

print(f"ship={ship}. manhattan distance={abs(ship['x']) + abs(ship['y'])}" )
