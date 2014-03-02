#!/usr/bin/python
#encoding: utf-8
from web import HTTPError
import web

class InternalError(HTTPError):
    """500 Internal Server Error`."""
    message = "internal server error"
    
    def __init__(self, status, message=None):
        headers = {'Content-Type': 'text/html'}
        HTTPError.__init__(self, status, headers, message or self.message)
        
internalerror = InternalError    

class DefaultError(HTTPError):
    """default Error`."""
    message = "default server error"
    def __init__(self, status, message=None):
        headers = {'Content-Type': 'text/html'}
        HTTPError.__init__(self, status, headers, message or self.message)
            
defaulterror = DefaultError
httpstatus = {
              200 : web.ok, 
              201 : web.created, 
              202 : web.accepted, 
              
              301 : web.redirect, 
              302 : web.found, 
              303 : web.seeother, 
              304 : web.notmodified, 
              307 : web.tempredirect, 
              
              400 : web.badrequest, 
              401 : web.unauthorized,  
              403 : web.forbidden, 
              404 : web.notfound, 
              405 : web.nomethod, 
              406 : web.notacceptable, 
              409 : web.conflict, 
              410 : web.gone, 
              412 : web.preconditionfailed, 
              
              500 : internalerror, 
              501 : internalerror,
              502 : internalerror,
              503 : internalerror,
              504 : internalerror,
              505 : internalerror,
}

