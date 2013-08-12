#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2,urllib
import simplejson
import time
import random

seachstr = '123'
user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0', \
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0', \
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \
        (KHTML, like Gecko) Element Browser 5.0', \
        'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)', \
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', \
        'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', \
        'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
        Version/6.0 Mobile/10A5355d Safari/8536.25', \
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/28.0.1468.0 Safari/537.36', \
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']
for x in range(200):
    
    print "page:%s"%(x+1)
    page = x*8
    time.sleep(1)
    url = ('https://ajax.googleapis.com/ajax/services/search/web'
                  '?v=1.0&q=%s&rsz=8&start=%s') % (urllib.quote(seachstr),page)
    try:
        request = urllib2.Request(
        url,{'Connection': 'keep-alive'},{'Connection': 'keep-alive'})
        index = random.randint(0, 9)
        user_agent = user_agents[index]
        request.add_header('User-agent', user_agent)
        response = urllib2.urlopen(request)

    # Process the JSON string.
        results = simplejson.load(response)
        infoaaa = results['responseData']['results']
    except Exception,e:
        print e
    else:
        for minfo in infoaaa:
            print minfo['url']

    

