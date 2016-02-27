import numpy as np

F,N = [int(i) for i in raw_input().split()]
l = []
l0 = []

for _ in xrange(N):
	l.append([float(i) for i in raw_input().split()])

T = int(raw_input())
for _ in xrange(T):
	l0.append([float(i) for i in raw_input().split()])

X = np.array(l)
X0 = np.array(l0)
one = [[1]]*N
one0 = [[1]]*T

Y=X[0:T,F:F+1]
X=np.c_[one,X][0:T,0:F+1]
X0 = np.c_[one0,X0]

B = np.dot( np.linalg.inv(np.dot(X.transpose(),X)) , np.dot(X.transpose(),Y) )

Y0 = np.dot(X0,B)

for line in Y0:
	for item in line:
		print item