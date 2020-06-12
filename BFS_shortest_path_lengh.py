from collections import deque
# bfs function 
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
# lengh function
def short(graph,start,end):
	return len(bfs_shortest_path(graph, start, end))-1
# please create a graph and the nodes you want to find, 
# use function "short" to return length
# here is an exmaple
graph={'TLKN': ['SADE'], 'AEQB': [], 'SADE': ['TLKN'], 'FZBJ': [], 
       'MAGK': ['QTGC'], 'BEGA': ['NUVZ'], 'WJOR': ['NUVZ'], 'IJUY': [],
       'QTGC': ['MAGK'], 'NUVZ': ['BEGA', 'WJOR']}
print(short(graph,'BEGA', 'WJOR'))
