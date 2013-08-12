
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import sys
import urllib2,urllib
import simplejson

reload(sys)
sys.setdefaultencoding('utf-8') 

class searchGoogle:
def searchKey(self,keyword):
url = ('https://www.googleapis.com/customsearch/v1?'
'key=AIzaSyA0cs_DMaY1KVNUC716e3Oiiz56lWjSpUo'
'&cx=013036536707430787589:_pqjad5hr1a&alt=json'
'&q=%s&num=1')%(urllib.quote(keyword))
try:
request = urllib2.Request(url, None)
response = urllib2.urlopen(request)
# Process the JSON string.
results = simplejson.load(response)
info = results['items']
return info
except Exception,e:
print e
