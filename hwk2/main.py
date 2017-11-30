from irlib import read_graph , pageRank

fname = 'graph.txt'
g = read_graph(fname)
pageRank(g)