import pdb
from sets import Set
import datetime
from bs4 import BeautifulSoup
import os
import pickle
import re

datedict = pickle.load(open( "datedict.p", "rb" ))
#files = os.listdir('../data')
#files = [file for file in os.listdir('../data') if file.endswith('.html')]
caplist = []
ccount_all = 0
txt_last = ""
last_date = datetime.datetime(2014,12,1)
base_url = u"http://www.newyorksocialdiary.com"
regex = re.compile('/i/(.*?)/')
folders = Set([])
for url, date in datedict.iteritems():
    fname    = "../data/" + '_'.join(url.split('/'))[1:] + ".html"
    if date > last_date:
        continue
    f        = open(fname, 'r')
    sp       = BeautifulSoup(f.read())
    ccount   = 0
#    captions = sp.findAll(attrs={"class" : lambda x: x and x.startswith('photocaption')})
#    for caption in captions:
#        txt = caption.text.strip()
#        if txt != "" and txt != txt_last:
#            caplist.append(txt)
#            ccount     += 1
#            ccount_all += 1
#        txt_last = txt
    #images = sp.findAll('img', {'src' : lambda x: x and x.startswith('/i/') and not x.endswith('.gif')})
    tables = sp.findAll('tables')
    for table in tables:

    for image in images:
        pdb.set_trace()
        
        #srcstr = image['src']
        #m = regex.match(srcstr)
        #if m and m.groups()[0] not in folders:
        #    print m.groups()[0]
        #    folders.add(m.groups()[0])
        #else:
        #    "nothin"
    ccount_all += len(images)
    print "file:" + url + "\tccount:" + str(len(images)) + "\tccount_all:" + str(ccount_all)
#    print "file:" + url + "\tccount:" + str(ccount) + "\tccount_all:" + str(ccount_all)
    f.close()
