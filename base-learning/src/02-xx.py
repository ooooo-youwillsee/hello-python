# coding:utf-8

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import json
from tornado.web import RequestHandler
from tornado.httpserver import HTTPServer
from tornado.options import define,options
from tornado.ioloop import IOLoop

define("port", default=8000, type=int, help="xxx")


class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        hello = self.get_argument("hello")
        print(hello)
        jsonData = json.dumps({
            "hello": "hello"
        })
        self.write(jsonData)



def main():
    options.parse_command_line()
    application = tornado.web.Application(
        [(r"/", IndexHandler)],debug=True
    )
    http_server = HTTPServer(application)
    http_server.listen(options.port)
    IOLoop.current().start()


if __name__ == '__main__':
    main()
