import numpy as np

F,N = [int(i) for i in raw_input().split()]
l = []
l_ = []

for _ in xrange(N):
	l.append([float(i) for i in raw_input().split()])

T = int(raw_input())
for _ in xrange(T):
	l_.append([float(i) for i in raw_input().split()])

X = np.array(l)
X_ = np.array(l_)
one = [[1]]*N
one_ = [[1]]*T

Y=X[0:T,F:F+1]
X=np.c_[one,X][0:T,_:F+1]
X_ = np.c_[one_,X_]

B = np.dot( np.linalg.inv(np.dot(X.transpose(),X)) , np.dot(X.transpose(),Y) )

Y_ = np.dot(X_,B)

for line in Y_:
	for item in line:
		print item