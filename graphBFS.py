from collections import deque
from random import choice
def bfs_visited(ugraph, start_node):
	Q=deque()
	visit=set([start_node])
	Q.append(start_node)
	while len(Q)!=0:
		j=Q.pop()
		for neighbor in ugraph[j]:
			if neighbor not in visit:
				visit.add(neighbor)
				Q.append(neighbor)
	return visit
def cc_visited(ugraph):
	remianing_nodes=set([])
	cc=[]
	while remianing_nodes!=set([]):
		i=choice(ugraph.keys())
		w=bfs_visited(ugraph,i)
		cc.append(w)
		remianing_nodes=remianing_nodes-w
	return cc

				





