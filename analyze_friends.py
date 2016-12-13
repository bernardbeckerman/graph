import pdb
import networkx as nx
H = nx.read_gpickle('H1.p')
bflist = []
for a, b, data in sorted(H.edges(data=True), key=lambda (a, b, data): data['weight'], reverse=True):
    bflist.append(((a, b), data['weight']))
pdb.set_trace()
