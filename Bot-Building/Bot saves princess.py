#!/bin/python
def displayPathtoPrincess(n,grid):
	moves=[]
	botPos=()
	princessPos=()
	for i in range(len(grid)):
		if 'm' in grid[i]:
			(y1,x1)= i,grid[i].index('m')
		if 'p' in grid[i]:
			(y2,x2)=i,grid[i].index('p')
	if y1-y2>0:
		moves.extend(['UP']*abs(y1-y2))
	else:
		moves.extend(['DOWN']*abs(y1-y2))

	if x1-x2>0:
		moves.extend(['LEFT']*abs(x1-x2))
	else:
		moves.extend(['RIGHT']*abs(x1-x2))

	for m in moves:
		print m
#print all the moves here
N = input()

grid = []
for i in xrange(0, N):
    grid.append(raw_input().strip())

displayPathtoPrincess(N,grid)
