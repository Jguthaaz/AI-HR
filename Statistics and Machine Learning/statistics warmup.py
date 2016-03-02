from __future__ import division
import sys
from math import *
import numpy as np
import scipy as sp
import scipy.stats

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return m, m-h, m+h

def chooseMost(List):
    temp=[]
    for i in List:
        temp+=[List.count(i)]
    return List[temp.index(max(temp))]

N = int(raw_input())

X = map(int,sys.stdin.readline().split())

mean = sum(X)/N

if N%2:
	Median = sorted(X)[N/2]
else:
	Median = (sorted(X)[int((N-2)/2)]+sorted(X)[int(N/2)])/2

mode = chooseMost(sorted(X))

SD = sqrt(sum((x-mean)**2 for x in X)/N) 

print mean
print Median
print mode
print SD
print mean_confidence_interval(X,confidence=0.95)