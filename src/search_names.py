from operator import itemgetter
import nltk
from sets import Set
import re
import pickle
import networkx as nx
H=nx.Graph()
captions    = pickle.load(open( "captions.p", "rb" ))

sal_set     = Set(['Mr','Mrs','Ms','Miss','Mayor','President','Governor','Dr','Member','University','Foundation','Award','Associates'])
lcnameset   = Set(['von','de','la', 'du', 'van', 'di'])
onewdnames  = Set([])
names       = Set([])
preword     = ''
for caption in captions:
    firstflag = 0
    name      = []
    if len(caption) < 250:
        namebool = False
        words = re.split('[^\w\'-,]+', caption)
        capnames = []
        for word in words:
            if (re.match('^[A-Z]',word)) or (word in lcnameset) or (re.match('^d\'[A-Z]',word)):
                if namebool:
                    name.append(preword)
                namebool = True
                if word.endswith(','):
                    namebool = False
                    name.append(word[:-1])
                    if len(name) > 1 and len(name) < 6 and 'The' not in name:
                        names.add(' '.join(name))
                        capnames.append(' '.join(name))
                    name = []
                if word.endswith('\'s') or preword in sal_set:
                    name = []
            else:
                if namebool:
                    name.append(preword)
                    if len(name) > 1 and len(name) < 6 and 'The' not in name and preword not in sal_set:
                        names.add(' '.join(name))
                        capnames.append(' '.join(name))
                        if firstflag:
                            name = firstflag + ' ' + name[-1]
                            names.add(name)
                            capnames.append(name)
                            #print name
                firstflag = 0
                if namebool:
                    if len(name) == 1 and word == 'and':
                        firstflag = preword
                    name = []
                namebool = False
            preword = word
        if namebool:
            name.append(preword)
            if len(name) > 1 and 'The' not in name:
                names.add(' '.join(name))
                capnames.append(' '.join(name))
                if firstflag:
                    name = firstflag + ' ' + name[-1]
                    names.add(name)
                    capnames.append(name)
        
        for iind in range(len(capnames)):
            iname = capnames[iind]
            for jind in range(iind+1,len(capnames)):
                jname = capnames[jind]
                if iname != jname:
                    if not H.has_edge(iname, jname):
                        H.add_edge(iname, jname, weight=0)
                    H[iname][jname]['weight'] += 1
nx.write_gpickle(H,'H1.p')
#print sorted(G.degree_iter(),key=itemgetter(1),reverse=True).head()
print len(names)
#print names
