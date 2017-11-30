from numpy import matrix, asarray, zeros
import numpy as np

#return an adjacency matrix
def read_graph(fname):
	with open(fname,'r') as f:
		lines = f.readlines()

	# read in adjacency list
	Nodes = {}
	ADJ_LST = []
	n = 0
	for t in lines:
		src, dst, k = t.strip().split(' ')
		if not src in Nodes.keys():
			Nodes[src]=n
			n+=1
			ADJ_LST.append([])
		if not dst in Nodes.keys():
			Nodes[dst]=n
			n+=1
			ADJ_LST.append([])
		ADJ_LST[Nodes[src]].append(dst)

	#convert to matrix
	n_nodes = len(Nodes.keys())
	g =np.zeros((n_nodes,n_nodes))
	
	for i in range(len(ADJ_LST)):
		t = ADJ_LST[i]
		for j in t:
			g[Nodes[j]][i] = 1

	#print (matrix(g))
	return matrix(g)

def getTransitionMatrix(g):
	s = asarray(g.sum(0)).reshape(-1)
	s[s == 0] = 1
	return g / s

def initRank(n):
	return matrix([1.0/n]*n).transpose()

def isNotConverge(a,b, d):
	if max( abs(a-b) ) >= d:
		return True
	else:
		return False

def pageRank(g , delta = 0.0001, beta = 0.85):
	n = g.shape[0]
	M = getTransitionMatrix(g)
	print("Trasition Matrix:")
	print(M)

	p = (1-beta)/n
	iter_cnt = 0
	r = initRank(n)
	print ('initRank:')
	print (r)
	prev_r = zeros(r.shape)

	while isNotConverge(r, prev_r, delta):
		prev_r = r
		iter_cnt+=1
		r = (beta * M * r) + p

	print('Number of iterations: %d'%iter_cnt)
	print("Rankings:")
	print(r)
	return r , iter_cnt






