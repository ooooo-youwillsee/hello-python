# coding:utf-8
import json

from tornado import httpserver, options
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.web import RequestHandler

options.define("port", default=8080, type=int)


class MainPageHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello tornado")


class PythonHandler(RequestHandler):

    def post(self, *args, **kwargs):
        stu = {
            "name": "zhangsan",
            "age": 22
        }
        # json 数据
        body = self.request.body
        print(body)
        self.write(json.dumps(stu))


if __name__ == '__main__':
    application = Application([
        (r"/", MainPageHandler),
        (r'/python', PythonHandler),
    ])
    http_server = httpserver.HTTPServer(application)
    # http_server.listen(8000)
    http_server.bind(options.options.port)
    http_server.start(1)
    IOLoop.current().start()
