from math import * 

def CDF(x,mu,sigma,percentage=False):
	result = (1.0+erf((x-mu)/(sigma*sqrt(2.0))))/2.0

	if percentage:
		return 100*result
	else:
		return result

print '%.3f' %CDF(40,30,4)
print '%.3f' %(1-CDF(21,30,4))
print '%.3f' %(CDF(35,30,4)-CDF(30,30,4))