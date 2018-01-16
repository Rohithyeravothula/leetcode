#!/usr/bin/env python2
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor



def preidctTemperature(startDate, endDate, temperature, n):
    month = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
    inverse_month = ['January','February','March','April','May','June','July','August','September','October','November','December']
    lines = []
    for i in range(0, 24):
        lines.append(startDate[4], inverse_month[i%13], temperature[i], temperature[i])
    for i in [2, 3]:
        x, y, xx = [], [], []
        for t in lines:
            yy = int(t[0])
            mm = [0]*12
            mm[month[t[1]]-1] = 1
            if t[5-i][0] != 'M':
                xl = mm+[yy*12+month[t[1]]-1, float(t[5-i])]
            if t[2][0] != 'M' and t[3][0] != 'M':
                x.append(xl)
                y.append(float(t[i]))
            if t[i][0] == 'M':
                xx.append(xl)
        gbr = GradientBoostingRegressor(n_estimators=5000, learning_rate=0.0015)
        gbr.fit(x, y)
        yy = gbr.predict(xx)
        if i == 2:
            maxp = yy
        else:
            minp = yy

    maxi, mini = 0, 0
    for t in lines:
        if t[2][0] == 'M':
            print('{:.1f}'.format(float(maxp[maxi])))
            maxi += 1
        elif t[3][0] == 'M':
            print('{:.1f}'.format(float(minp[mini])))
            mini += 1

