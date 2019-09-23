from gevent.monkey import patch_all;
patch_all()

import random
import socket
from urllib import request
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from werkzeug.routing import Map, Rule
from werkzeug.utils import redirect


import json


addr_proxy = [
        {"http": "127.0.0.1:10081"},
    ]


def proxy_urlib(addr_proxy, addr_target):
    proxy_list = addr_proxy
    # 随机选择一个代理
    proxy = random.choice(proxy_list)
    # 使用选择的代理构建代理处理器对象
    httpproxy_handler = request.ProxyHandler(proxy)

    opener = request.build_opener(httpproxy_handler)
    r = request.Request(addr_target)
    print(addr_target)
    try:
        resp = opener.open(r, timeout=3)
        return resp
    except Exception as e:
        raise Exception("{}: {}".format(proxy, str(e)))


def forward_socket(host_forward, port_forward, data_forward):
    buffer = 1024
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host_forward, port_forward))
        sock.sendall(data_forward)
        data_recv = sock.recv(buffer)
        print(data_recv)
        return data_recv


def index(req):
    path = req.path
    print(path)
    print("请求方式:{}".format(req.method))

    # 测试redirect
    # if path == "/redirect":
    #     return redirect("http://127.0.0.1:10090/baidu", 302)

    # 测试代理转发
    if path == "/proxy":
        try:
            print("begin to proxy: {}".format(addr_proxy))

            # post请求
            post_str = b'POST /post/test HTTP/1.1\r\nHost: %s\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36\r\n\r\n%s\r\n\r\n'

            # get请求
            get_str = b'GET /get/test?hugo=boss HTTP/1.1\r\nHost: %s\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36\r\nAccept: */*\r\n\r\n'

            data_recv = forward_socket("127.0.0.1", 10090, get_str)
            return Response("代理转发结果:{}".format(str(data_recv, encoding="utf-8")), status='200 OK', content_type ='application/json', mimetype='application/json')

        except Exception as e:
            return Response("代理转发异常:{}".format(str(e)), status='200 OK', content_type='application/json', mimetype='application/json')

    return Response(json.dumps({"path": 302}), status='200 OK', content_type='application/json', mimetype='application/json')


def proxy_redirect(url, code=302, response=None):
    redirect(url,code, response)


url_map = Map([
    Rule('/', endpoint=index),
Rule('/<any(help,admin,doc):any>',endpoint=index),
    Rule('/<int:day>', endpoint=index),
    Rule('/<int:year>/<int:month>/<int:day>', endpoint=index),
    Rule('/<int:year>/<int:month>', endpoint=index),
    Rule('/<string:title>', endpoint=index)
])

views = {'index': index}


@Request.application
def application(req):
    adapter = url_map.bind_to_environ(req.environ)
    endpoint, args = adapter.match()
    return endpoint(req)


if __name__ == "__main__":
    run_simple("0.0.0.0", 10080, application)