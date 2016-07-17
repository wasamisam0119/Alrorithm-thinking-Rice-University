EX_GRAPH0={0:set([1,2]),1:set([]),2:set([])}
EX_GRAPH1={0:set([1,4,5]),1:set([2,6]),2:set([3]),3:set([0]),4:set([1]),5:set([2]),6:set([])}
def make_complete_graph(num_nodes):
	graph={}
	if num_nodes<=0:
		graph={}
		return graph
	elif num_nodes==1:
		graph={0:set([])}
		return graph
	else:
		for node in range(0,num_nodes):
			graph[node]=set([x for x in range(0,num_nodes) if x!=node])	
		return graph
def compute_in_degrees(digraph):
	in_degrees={}
	for node in digraph:
		in_degrees[node]=0
	for node in digraph:
		for edge in digraph[node]:
			in_degrees[edge]+=1
	return in_degrees
def in_degree_distribution(digraph):
	in_degree=compute_in_degrees(digraph)
	degree_distribution={}
	for i in in_degree:
		degree_distribution[in_degree[i]]=0
	for i in in_degree:
		degree_distribution[in_degree[i]]+=1
	return degree_distribution