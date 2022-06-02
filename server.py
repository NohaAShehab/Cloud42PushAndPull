import os
import time
from typing import Optional, Awaitable
from datetime import date


import tornado.ioloop
import tornado.web
from tornado import gen


@gen.coroutine
def async_sleep(timeout):
    """ Sleep without blocking the IOLoop. """
    yield gen.coroutine(tornado.ioloop.IOLoop.current().add_timeout)


class MainHandler(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    @gen.coroutine
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        # clienttime = float(self.get_query_argument('lastmod'))

        self.write("Cloud42")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()