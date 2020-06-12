import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt
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
	M=cube(graph)
	t1=time.time()
	for i in range(1000):
		x=random.choice(vertices)
		y=random.choice(vertices)
		u=vertices.index(x)
		v=vertices.index(y)
		re=M[u][v]
	t2=time.time()
	return [(t1-t0),(t2-t1)]
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
          'P','Q','R','S','T','U','V','W','X','Y','Z']
created=[]
for i in range(100):
	lettori=random.sample(alphabet,k=4)
	nome=''
	for lettore in lettori:
		nome+=lettore
	created.append(nome)
T=[]
t=[]
for k in range(1,101):
	T.append(simtest(created,k)[0])
	t.append(simtest(created,k)[1])
plt.plot(range(1,101),T,label='Total time Creating M')
plt.plot(range(1,101),t,label='Total time of accessing M 1000 times')
plt.xlabel('1/Probabilities of edges')
plt.ylabel('Running time(s)')
plt.yticks(np.arange(0,max(T),max(T)/10))
plt.legend(loc='best')
plt.show()
