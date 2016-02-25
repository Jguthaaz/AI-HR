# Here are the test scores of 10 students in physics and history:

# Physics Scores  15  12  8   8   7   7   7   6   5   3
# History Scores  10  25  17  11  13  17  20  13  9   15

# #1 Compute Karl Pearson’s coefficient of correlation between these scores. 
# #2 Compute the slope of the line of regression obtained while treating Physics as the independent variable. 
# Compute the answer correct to three decimal places.
# #3 When a student scores 10 in Physics, what is his probable score in History? Compute the answer correct to one decimal place.


from __future__ import division
from math import *

ps = [15,12,8,8,7,7,7,6,5,3]
hs = [10,25,17,11,13,17,20,13,9,15]

def COC(x,y): #Karl Pearson’s coefficient of correlation
	n = len(x)
	return ((n * sum(x[i] * y[i] for i in range(n)) - sum(x) * sum(y)) / sqrt((n * sum(v**2 for v in x) - sum(x) ** 2 ) * ( n * sum(v ** 2 for v in y) - sum(y) ** 2))) 

def PoLR(x,y): #parameter of linear regression
	n = len(x)
	b = ((n * sum(x[i] * y[i] for i in range(n)) - sum(x)*sum(y)) / ( n * sum(v**2 for v in x) - sum(x) ** 2))
	a = sum(y)/n - b * sum(x) / n
	return a,b

def RP(x,y,x0): #regression prediction
	(a,b) = PoLR(x,y)
	y0 = a + b*x0
	return y0

print '%.1f' % RP(ps,hs,10)