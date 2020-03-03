#!/usr/bin/env python3
import os
import sys

logfile = 'fuck.log'
lf = open(logfile, 'w')

for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    for file in files:
        if 'txt' not in file:
            continue
        f = open(file, 'r')
        yuans = []
        for l in f:
            if '元' in l:
                yuans.append(l)
        if len(yuans) != 10:
            lf.write(file + '\n')
            print("skipping {}".format(file))
            continue
        df = open(file.replace('txt', 'csv'), 'w')
        df.write('order,value\n')
        i = 0
        total_val = 0
        for l in yuans[::-1]:
            val = l.replace('元', '').replace('\n', '')
            val = ''.join(c for c in val if c.isdigit() or c == '.') # remove non digits/.
            if val[0] == '.': # .1.2
                val = val[1:]
            total_val += float(val)
            if float(val) > 60:
                print(float(val), file)
                assert(False)
            df.write('{},{}\n'.format(i, val))
            i += 1
        import numpy as np
        if not np.allclose(total_val, 66): # total value of a red bag should be 66
            print(file, total_val)
            assert(False)
        df.close()
lf.close()
