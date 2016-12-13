import requests
from bs4 import BeautifulSoup
import datetime
import pickle

def getresp(url_str):
    MAX_TRIES = 10
    tries = 0
    resp = None
    cont = True
    while cont:
        resp = requests.get(url_str)
        if resp.status_code >= 400 and tries < MAX_TRIES:
                tries += 1
        elif resp.status_code >= 400 and tries == MAX_TRIES:
            print "url " + url_str + " failed with status " + str(resp.status_code) + " after " + str(MAX_TRIES) + "tries."
            cont = False
        else:
            print "Successful download of " + url_str
            cont = False
    return resp

base_url = u"http://www.newyorksocialdiary.com/party-pictures?page="

#npages = 1
npages = 28

dates = []
urls  = []
for page in range(npages):
    url      = base_url + str(page)
    a        = getresp(url)
    sp       = BeautifulSoup(a.text)
    parties  = sp.findAll('div', {"class" : lambda x: x and x.startswith('views-row')})
    datestrs = [i.find('span', {"class" : 'views-field views-field-created'}).find('span').getText() for i in parties]
    urlstrs  = [i.find('span', {"class" : 'views-field views-field-title'}).find('a', href=True)['href'] for i in parties]
    for datestr in datestrs:
        dates.append(datetime.datetime.strptime(datestr, "%A, %B %d, %Y"))
    for urlstr in urlstrs:
        urls.append(urlstr)
#print urls
#print dates
#import re
#regex = re.compile("(.*_.*)")
#for url in urls:
#    m = regex.match(url)
#    if m:
#        print m.groups()
# previous shows that there are no _ in the urls, so that _ and / can be substituted for one another

datedict = dict(zip(urls,dates))
pickle.dump(datedict, open("datedict.p", "wb"))
last_date = datetime.datetime(2014,12,1)
base_url = u"http://www.newyorksocialdiary.com"
enddate = datetime.datetime
for url, date in datedict.iteritems():
    full_url = base_url + url
    a        = getresp(full_url)
    fname    = "../data/" + '_'.join(url.split('/'))[1:]
    f        = open(fname, 'w')
    f.write(a.text.encode('utf8'))
    f.close()

