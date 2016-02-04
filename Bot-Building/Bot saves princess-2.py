#!/bin/python
def nextMove(n,r,c,grid):
	move = ""
	x,y = 0,0
	for i in range(len(grid)):
		if 'p' in grid[i]:
			(x,y)=i,grid[i].index('p')
	
	if x!=r:
		if x>r:
			move="DOWN"
		elif x<r:
			move="UP"
	elif x==r:
		if y>c:
			move="RIGHT"
		elif y<c:
			move="LEFT"	
	return move
n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
	grid.append(raw_input())

print nextMove(n,r,c,grid)
