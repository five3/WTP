#!/usr/bin/python
#encoding: utf-8
import web
import httplib, urllib

import sys
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

urls = (
    '/', 'hello',
    '/(.*)', 'seeother',
)

from config import *
from hosts import hosts
web.config.debug = isdebug
app = web.application(urls, globals())

def do_proxy(method, host, path, data=None, headers={}):
    print 'request header: %s' % headers
    h, p = host.split(':')
    host = '%s:%s' % (hosts.get(h, h), p)
    conn = httplib.HTTPConnection(host)
    conn.request(method, path, body=data, headers=headers)
    response = conn.getresponse()
    r = [response.status, response.reason, response.read(), response.getheaders()]
    print 'response result: %s' % r[:2]
#    print 'reseponse body: %s' % r[2]
    conn.close()
    return r  

#import re  
#hrefpat = re.compile(r'''href="(/.*?)"''', re.M)
#srcpat = re.compile(r'''src="(/.*?)"''', re.M)
#def replace_short_url(r): 
#
#    data = r[2]
#    if hrefpat.search(data): 
#        for n in hrefpat.finditer(data):
#            nn = 'href="http://%s%s"' % (goal_host, n.group(1))
#            data = data.replace(n.group(), nn)                    
#    if srcpat.search(data): 
#        for n in srcpat.finditer(data): 
#            nn = 'src="http://%s%s"' % (goal_host, n.group(1))
#            data = data.replace(n.group(), nn)  
#    r[2] = data    
#    return r

def get_http_request_info(headerappend):
    env = web.ctx.env
#    print env
    request_method = env['REQUEST_METHOD']
    request_path = env['REQUEST_URI']  
    postdata = urllib.urlencode(web.input())
    headers = {}
    httpkeys = [i for i in env.keys() if i.startswith("HTTP_")]
    for k in httpkeys:
        headers[k[5:].replace('_', '-').lower()] = env[k]        
    headers['host'] = goal_host
    headers['referer'] = 'http://%s/' % goal_host
    headers['accept-encoding'] = 'identity'
    if headerappend:
        for k,v in headerappend.items():
            headers[k] = v    
    return (request_method, '%s:%s' % (goal_host, env['SERVER_PORT']), request_path, postdata, headers)

from httpstatus import httpstatus

def set_http_response_info(r):
    for h in r[3]:
        if h[0] != 'cnotent-encoding':
            web.header(h[0], h[1])  
        if h[0] == 'location':
            location = h[1]
    status = httpstatus.get(r[0])
    if r[0] == 200:   
        return r[2]  
    elif r[0] == 301:
        return status(location) 
    elif r[0] == 302:
        return status(location) 
    elif r[0] == 303:
        return status(location)  
    elif r[0] == 307:
        return status(location) 
    elif r[0] == 404:
        return status(r[2]) 
    elif r[0] >= 500:
        return status('%s %s' % r[:2], r[1])
    else:
        return status()
            
class seeother:
    def GET(self, par):    
        print 'see other'
        http_request_info = get_http_request_info(auth_header)
        r = do_proxy(*http_request_info)
        return set_http_response_info(r)
    def POST(self, par):
        return self.GET(par)
    
class hello:        
    def GET(self):
        http_request_info = get_http_request_info(auth_header)
        headers = http_request_info[4]
        r = do_proxy("GET", "%s:%s" % (goal_host, 80), "/", "", headers)
        return set_http_response_info(r)

if __name__ == "__main__":
    app.run()
    