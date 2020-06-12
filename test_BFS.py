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
def simtest(vertices,k):
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
			r=[True]+[False]*(k-1)
			d=random.choice(r)
			if d is True:
				graph[y].append(x)
				graph[x].append(y)
			j+=1
		i+=1
	t0=time.time()
	for i in range(1000):
		x=random.choice(vertices)
		y=random.choice(vertices)
		re=short(graph,x,y)
	t1=time.time()
	return (t1-t0)
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
          'P','Q','R','S','T','U','V','W','X','Y','Z']
created=[]
for i in range(200):
	lettori=random.sample(alphabet,k=4)
	nome=''
	for lettore in lettori:
		nome+=lettore
	created.append(nome)
print(created)
t=[]
ks=[1,2,4,8,16,32,64]
for k in range(1,201):
	t.append(simtest(created,k))
plt.plot(range(1,201),t,label='Total time of running BFS 1000 times')
plt.xlabel('1/Probabilities of edges')
plt.ylabel('Running time(s)')
plt.yticks(np.arange(0,max(t),max(t)/10))
plt.legend(loc='best')
plt.show()
