import math
import random
import time
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
def bfs_shortest_path(graph, start, goal):
	# keep track of explored nodes
	explored = []
	# keep track of all the paths to be checked
	queue = deque([[start]])
    # return path if start is goal
	if start == goal:
		return [start] 
	# keeps looping until all possible paths have been checked
	while queue:
		# pop the first path from the queue
		path = queue.popleft()
		# get the last node from the path
		node = path[-1]
		if node not in explored:
			neighbours = graph[node]
			# go through all neighbour nodes, construct a new path and
			# push it into the queue
			for neighbour in neighbours:
				new_path = list(path)
				new_path.append(neighbour)
				queue.append(new_path)
				# return path if neighbour is goal
				if neighbour == goal:
					return new_path 
			# mark node as explored
			explored.append(node) 
	# in case there's no path between the 2 nodes
	return []
def short(graph,start,end):
	return len(bfs_shortest_path(graph, start, end))-1
def cube(graph):
	n=len(graph)
	vertices=[] # store vertices in a list
	for vertice in graph:
		vertices.append(vertice)
	C=[] # initiate the Cube
	i=0
	xry=[] # here we build the ZERO PIANO of C
	while i<n:
		j=0
		yry=[]
		while j<n:
			point=vertices[j]
			lst=graph[vertices[i]]
			if point==vertices[i]: # distance of A and A is 0
				yry.append(0)
			elif point in lst: # if A and B is connected, distance 1
				yry.append(1)
			else:yry.append(math.inf)
			# if not directly connected, distance infinite
			j+=1
		xry.append(yry)
		i+=1
	C.append(xry)
	#at this point, C has only one level, which means it is just a plane
	k=1
	while k<=n:
		i=0
		xy=[]
		while i<n:
			j=0
			yy=[]
			while j<n:
				d=min(C[k-1][i][j],(C[k-1][i][k-1]+C[k-1][k-1][j])) 
				# d is the value of the point in next level
				yy.append(d)
				j+=1
			xy.append(yy)
			i+=1
		C.append(xy)
		k+=1
	return C[n] # we only need the last level of C
vertices=[]
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
          'P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(100):
	lettori=random.sample(alphabet,k=4)
	nome=''
	for lettore in lettori:
		nome+=lettore
	vertices.append(nome)
n=len(vertices)
graph={}
for place in vertices:
	graph[place]=[]
i=0
while i<n:
	j=i+1
	while j<n:
		x=vertices[i]
		y=vertices[j]
		r=[True]+[False]*3
		d=random.choice(r)
		if d is True:
			graph[y].append(x)
			graph[x].append(y)
		j+=1
	i+=1
M=cube(graph)
while True:
	x=random.choice(vertices)
	y=random.choice(vertices)
	re1=short(graph,x,y)
	u=vertices.index(x)
	v=vertices.index(y)
	re2=M[u][v]
	if re1==-1: 
		if re2==math.inf: print('ok')
		else: print('no')
	else: 
		if re1==re2:
			print('ok')
		else: print('no')
