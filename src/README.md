Graph - create and analyze donor social network based on newyorksocialdiary.com, a public photo diary of charity events
    • Crawled through diary pages [requests] 100MB of text
    • Extracted captions [beautifulsoup, lxml]
    • Distinguished picture tags from narrative captions [nltk]
    • Parsed tags and extracted names [regex]
      	◦ John and Mary Smith -> John Smith and Mary Smith
	◦ Mayor Michael Bloomberg -> Michael Bloomberg
    • Built social graph with weights from name concurrence [networkx]
        ◦ Identified 100 most frequent names (most popular)
	◦ Identified 100 with highest page rank (most connected)
	◦ Identified the 100 edges with highest weight (best friends)