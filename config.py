#!/usr/bin/python
#encoding: utf-8

isdebug = True
cookie = '__permanent_id=20140224174105141104428769799210350; ASP.NET_SessionId=d3xu2wsbv2fahd5diehn4lgw; ddscreen=2; LOGIN_TIME=1393235067669; USERNUM=lle5MFu2Eb5Xtu1jampNNw==; login.dangdang.com=.AYH=20140224181524022420810&.ASPXAUTH=+DLrnVptC0thCtNW6e/kuA==; dangdang.com=email=Z3VvbWVpQDEuY29t&nickname=Z3VvbWVpMQ==&display_id=4571695608214&customerid=Xe5ehJ3FM22KnnSyUaBwFQ==&viptype=GgJTzxIr4bA=&show_name=guomei1; ddoy=email=guomei%401.com&nickname=guomei1&agree_date=1&validatedflag=0&uname=guomei%401.com&utype=0&.ALFG=off&.ALTM=1393235414; sessionID=fcc1e2fe03c4c962010d57bdb7e8a1ee; __ddclick_visit=0000000001.6; __trace_id=20140224174449067313303944247313690; out_refer=http%253A%2F%2Fwww.dangdang.com%2F%7C; cart_id=88654274042965906; cart_items_count=1'
append_header = {}#{"authorization": "Basic Y2hlbnhpYW93dToxMTExMTE="}
auth_header = {'Cookie' : cookie} 
set_cookie = [##name, value, expires, domain, secure, httponly, path
('LOGIN_TIME', '1393235067669', '', '.dangdang.com', False, False, '/'),
('USERNUM', 'lle5MFu2Eb5Xtu1jampNNw==', '', '.dangdang.com', False, False, '/'),
('__ddclick_visit', '0000000001.6; __trace_id=20140224174449067313303944247313690', '', '.dangdang.com', False, False, '/'),
('__permanent_id', '20140224174105141104428769799210350', '', '.dangdang.com', False, False, '/'),
('__trace_id', '20140225102831272187908584659123043', '', '.dangdang.com', False, False, '/'),
('cart_id', '88654274042965906', '', '.dangdang.com', False, False, '/'),
('cart_items_count', '1', '', '.dangdang.com', False, False, '/'),
('dangdang.com', 'email=Z3VvbWVpQDEuY29t&nickname=Z3VvbWVpMQ==&display_id=4571695608214&customerid=Xe5ehJ3FM22KnnSyUaBwFQ==&viptype=GgJTzxIr4bA=&show_name=guomei1', '', '.dangdang.com', False, False, '/'),
('ddoy', 'email=guomei%401.com&nickname=guomei1&agree_date=1&validatedflag=0&uname=guomei%401.com&utype=0&.ALFG=off&.ALTM=1393235414', '', '.dangdang.com', False, False, '/'),
('ddscreen', '2', '', '.dangdang.com', False, False, '/'),
('ddscreen', '2', '', '.dangdang.com', False, False, '/shoppingcart'),
('login.dangdang.com', '.AYH=20140224181524022420810&.ASPXAUTH=+DLrnVptC0thCtNW6e/kuA==', '', '.dangdang.com', False, False, '/'),
('out_refer', 'http%253A%2F%2Fwww.dangdang.com%2F%7C', '', '.dangdang.com', False, False, '/'),
('sessionID', 'fcc1e2fe03c4c962010d57bdb7e8a1ee', '', '.dangdang.com', False, False, '/'),
             ]
set_cookie_head = (
'__permanent_id=20140224174105141104428769799210350; Domain=.dangdang.com; Path=/',
'ddscreen=2; Domain=.dangdang.com; Path=/',
'ddscreen=2; Domain=.dangdang.com; Path=/shoppingcart',
'LOGIN_TIME=1393235067669; Domain=.dangdang.com; Path=/',
'USERNUM=lle5MFu2Eb5Xtu1jampNNw==; Domain=.dangdang.com; Path=/',
'login.dangdang.com=.AYH=20140224181524022420810&.ASPXAUTH=+DLrnVptC0thCtNW6e/kuA==; Domain=.dangdang.com; Path=/',
'dangdang.com=email=Z3VvbWVpQDEuY29t&nickname=Z3VvbWVpMQ==&display_id=4571695608214&customerid=Xe5ehJ3FM22KnnSyUaBwFQ==&viptype=GgJTzxIr4bA=&show_name=guomei1; Domain=.dangdang.com; Path=/',
'ddoy=email=guomei%401.com&nickname=guomei1&agree_date=1&validatedflag=0&uname=guomei%401.com&utype=0&.ALFG=off&.ALTM=1393235414; Domain=.dangdang.com; Path=/',
'sessionID=fcc1e2fe03c4c962010d57bdb7e8a1ee; Domain=.dangdang.com; Path=/',
'__ddclick_visit=0000000001.6; Domain=.dangdang.com; Path=/',
'__trace_id=20140224174449067313303944247313690; Domain=.dangdang.com; Path=/',
'out_refer=http%253A%2F%2Fwww.dangdang.com%2F%7C; Domain=.dangdang.com; Path=/',
'cart_id=88654274042965906; Domain=.dangdang.com; Path=/',
'cart_items_count=1; Domain=.dangdang.com; Path=/',                   
                   )

goal_host = "checkout.dangdang.com"


