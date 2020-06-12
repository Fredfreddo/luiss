import random
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
          'P','Q','R','S','T','U','V','W','X','Y','Z']
created=[]
n=input('Please insert number of nodes:')
for i in range(int(n)):
	lettori=random.sample(alphabet,k=4)
	nome=''
	for lettore in lettori:
		nome+=lettore
	created.append(nome)
# k is 1/probability
def randomgraph(vertices,k):
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
	return graph
k=input('Please insert reciprocal of probability to have edges')
print(randomgraph(created,int(k)))
