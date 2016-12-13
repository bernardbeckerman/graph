import networkx as nx
#G = nx.read_gpickle('G.p')
##print sorted(G.degree_iter(),key=lambda x: x[1],reverse=True)
#H = nx.Graph()
#for (u,v) in G.edges():
#    if H.has_edge(u,v):
#        H[u][v]['weight'] += 1
#    else:
#        H.add_edge(u,v,weight=1)
#nx.write_gpickle(H,'H.p')
H = nx.read_gpickle('H.p')
prlist = nx.pagerank(H)

