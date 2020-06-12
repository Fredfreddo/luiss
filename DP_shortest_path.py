import math
# create the table with cube
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
# store vetices in a list
def nodes(graph):
	vertices=[]
	for vertice in graph:
		vertices.append(vertice)
	return vertices
# access the table
# create a graph, use 'cube' and 'nodes' functions build M and vertices
# then find the shortest path using the following function
def short(graph,u,v):
	x=vertices.index(u)
	y=vertices.index(v)
	return M[x][y]
# here is an exmaple
graph={'TLKN': ['SADE'], 'AEQB': [], 'SADE': ['TLKN'], 'FZBJ': [], 
       'MAGK': ['QTGC'], 'BEGA': ['NUVZ'], 'WJOR': ['NUVZ'], 'IJUY': [],
       'QTGC': ['MAGK'], 'NUVZ': ['BEGA', 'WJOR']}
M=cube(graph)
vertices=nodes(graph)
print(short(graph,'BEGA', 'WJOR'))
