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

def get_http_request_info(headerappend): 
    '''for proxy request only'''
    env = web.ctx.env
    request_method = env['REQUEST_METHOD']
    request_path = env['REQUEST_URI']  
    postdata = web.input()
    postdata = urllib.urlencode(postdata)
    headers = {}
    httpkeys = [i for i in env.keys() if i.startswith("HTTP_")]
    for k in httpkeys:
        headers[k[5:].replace('_', '-').lower()] = env[k]        
    headers['host'] = goal_host
    headers['referer'] = 'http://%s/' % goal_host
    headers['accept-encoding'] = 'identity'
    if request_method=='POST':
        headers['content-length'] = len(postdata)
    if headerappend:
        for k,v in headerappend.items():
            headers[k] = v    
    return (request_method, '%s:%s' % (goal_host, env['SERVER_PORT']), request_path, postdata, headers)

from httpstatus import httpstatus, defaulterror
def set_http_response_info(r):
    '''for all response'''
    for h in r[3]:
        if h[0] != 'cnotent-encoding':
            web.header(h[0], h[1])  
        if h[0] == 'location':
            location = h[1]
    status = httpstatus.get(r[0], defaulterror)
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
    elif r[0] not in httpstatus.keys():
        return status('%s %s' % r[:2])
    else:
        return status()
    
def warp_proxy():
    print 'see other'
    http_request_info = get_http_request_info(append_header)
    r = do_proxy(*http_request_info)
    return set_http_response_info(r)  

def walk_step(steps):
    r = None
    if steps:        
        r = do_proxy("GET", "%s:%s" % (goal_host, 80), "/checkout.aspx", "", auth_header)
        for cookie in set_cookie_head:
            web.header('Set-Cookie', cookie)        
    return set_http_response_info(r)
              
class seeother:
    def GET(self, par):    
        return warp_proxy()
    def POST(self, par):
        return self.GET(par)

from proxy import *    
class hello:        
    def GET(self):
        postdata = web.input()
        if 'httpproxyexec' in postdata:  ##执行
            print 'home'
            exec_id = postdata.pop('httpproxyexec', '')
            steps = get_proxy_steps(exec_id)   
            return walk_step(steps)                         
        elif 'httpproxystep' in postdata: ##新增、加载、保存、查询
            print 'step'
            step_id = postdata.pop('httpproxystep', '')
            if step_id:
                steps = get_proxy_steps(step_id)
            return steps
        elif 'httpproxysetting' in postdata: ##配置hosts等
            print 'set'
            set_id = postdata.pop('httpproxysetting', '')
            if set_id:
                setting = get_proxy_set(set_id)           
            return setting           
        else:  ##普通代理 
            return warp_proxy()    
    def POST(self):
        return self.GET()

if __name__ == "__main__":
    app.run()
    