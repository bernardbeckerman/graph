import codecs
import random 
import sys
import pdb
from sets import Set
import sys
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
imgtag = False
startbool = False
captions = []
for url, date in datedict.iteritems():
    if date > last_date:
        continue
    fname    = "../data/" + '_'.join(url.split('/'))[1:] + ".html"
    f        = open(fname, 'r')
    sp       = BeautifulSoup(f.read())
    print ""
    print fname
    print ""
    for child in sp.recursiveChildGenerator():
        name = getattr(child, "name", None)
        if name is not None:
            if name == 'img':
                #print "Name:" + name
                imgtag = True
        elif imgtag and not (child.isspace() or child.encode('ascii', 'ignore').strip().startswith('CAPTION')): # leaf node, don't print spaces
            if child.strip().startswith('Photographs by') or child.strip() == 'EMAIL':
                startbool = False
            if startbool and not child.strip().startswith('<'):
                captions.append(child.encode('ascii', 'ignore').strip())
            if child.strip().startswith('Social Diary'):
                startbool = True
            imgtag = False
    f.close()
print len(captions)
pickle.dump(captions, open("captions.p", "wb"))
