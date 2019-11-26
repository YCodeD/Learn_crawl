from wsgiref.simple_server import make_server

def application(environ, start_response):
    #通过environ封装成一个所有请求信息的对象
    #start_responsr可以很方便的设置响应头
    start_response('200 OK',[('Content_Type', 'text/html')])
    return [b'<h1>hello world</h1>']

#封装socket对象以及准备过程（socket, bind, listen）
httpd = make_server('', 8001, application)
print('Server HTTP on port 8001...')

httpd.serve_forever()

'''
wsgi服务器帮我们做了两件事情
1.帮我们把socket准备的过程简化了
2.帮我们完成了HTTP的解析过程

所有发过来的内容都放在environ，这是一个请求对象
想要请求的路径，请求信息
'''