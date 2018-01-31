#!/usr/bin/env python

import json
import time
import datetime
from dateutil import parser
import random

programs = []
users = []
breaks = []
data_flot = '['

now = int(time.time())

def utc_2_ts(utc):
    timestr = utc.replace(' UTC', ':00.00000Z').replace(' ', 'T')
    return int(parser.parse(timestr).strftime('%s'))


def get_strawberries(program):
        strawberries = {}
        running_val = 0
        running_val_diff = 0

        time_published = utc_2_ts(program['datetime_published'])
        time_first_break = utc_2_ts(program['datetime_first_break'])

        for running_timestamp in range(time_published, time_first_break, 86400):
            running_val += running_val_diff
            running_val_diff += 1
            strawberries[running_timestamp] = running_val
        running_val = max(running_val - 1, 0)
        for running_timestamp in range(time_first_break, 1506254400+1, 86400):
            strawberries[running_timestamp] = running_val
            running_val_diff = max(running_val_diff - 1, 0)
            running_val = max(running_val - running_val_diff, 0)

        return strawberries

def plot_data_for_program(program, now):
    data_flot = '['
    strawberries = get_strawberries(program)
    if len(strawberries) > 0:
        for key, val in sorted(strawberries.items()):
            data_flot += '[%d, %d], '%(key*1000, val)
        data_flot = data_flot[:-2]
    data_flot += ']'

    series = '{'
    series += 'color: "%s",'%program['hsl_color']
    series += 'label: "%s",'%program['_id']
    series += 'data: ' + data_flot + '}'
    return series


with open('programs.txt') as f:
    for line in f:
        vals = line.strip()[1:-1].split(',')
        vals = map(lambda x: x[3:-1].replace('\\xa0', ' '), vals)
        program = {
            "strawberries_ranking": vals[0],
            "_id": vals[1],
            "funny_name": vals[2],
            "strawberries_peak": vals[3][:-11],
            "username": vals[4],
            "is_break": vals[5],
            "datetime_published": vals[6],
            "datetime_first_break": vals[7],
            "strawberries_last": vals[8][:-11]
        }
        published_time = utc_2_ts(program['datetime_published'])
        program["hsl_color"] = 'hsl(%d, 100%%, %d%%)' % ((published_time-random.randint(10,1000))%360, published_time%47 + 20)
        data_flot += plot_data_for_program(program, now) + ', '
        programs.append(program)


with open('programs.json', 'w+') as f:
    json.dump(programs, f)

with open('plot.json', 'w+') as f:
    data_flot = data_flot[:-2]+']'
    f.write( data_flot)
    # json.dump(programs, f)



with open('users.txt') as f:
    for line in f:
        vals = line.strip()[1:-1].split(',')
        vals = map(lambda x: x[3:-1].replace('\\xa0', ' '), vals)
        user = {
            "bananas_ranking": vals[0],
            "username": vals[1],
            "bananas": vals[2][:-11],
        }
        users.append(user)

with open('users.json', 'w+') as f:
    json.dump(users, f)


with open('breaks.txt') as f:
    for line in f:
        vals = line.strip()[1:-1].split(',')
        vals = map(lambda x: x[3:-1].replace('\\xa0', ' '), vals)
        break_ = {
            "datetime_broken": vals[0],
            "username": vals[1],
            "strawberries": vals[2][:-11],
            "program": vals[3],
        }
        breaks.append(break_)

with open('breaks.json', 'w+') as f:
    json.dump(breaks, f)
