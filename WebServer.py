# -*- coding: utf-8 -*-
import os
import sys
import getopt
from os.path import abspath

sys.path.insert(0, os.path.split(abspath(__file__))[0])
sys.path.insert(1, os.path.split(sys.path[0])[0])

import traceback
import tornado.httpserver
import tornado.ioloop
import tornado.iostream
import tornado.web
import tornado.gen
import tornado.httpclient

import config
from Environment import Environment

from NaixPetitions import Petitions
from NaixMonitor import NaixMonitor


class Handler(tornado.web.RequestHandler):

    def get(self, func, *args, **kwargs):
        Environment().reset()

        try:
            responseBody = str(getattr(Petitions, func)(self))
        except:
            responseBody = str({'status':'error', 'msg':traceback.format_exc()})

        self.write(responseBody)
        self.finish()

    post = get


if __name__ == '__main__':

    args = {'-p':config.port}
    options, operands = getopt.getopt(sys.argv[1:], 'p:s')
    args.update(dict(options))

    if operands:
        args['-p'] = operands[0]

    for arg in ('-p',):
        if arg in args:
            args[arg] = int(args[arg])


    app = tornado.web.Application([
        (r'/favicon.ico', tornado.web.ErrorHandler, dict(status_code=404)),
        (r'/(.*)', Handler),
    ])

    if '-s' in args:
        server = tornado.httpserver.HTTPServer(app, xheaders=True, ssl_options=config.ssl_options)
    else:
        server = tornado.httpserver.HTTPServer(app, xheaders=True)

    server.bind(args['-p'], address=config.listenAddress)
    server.start(config.processes)
    monitor = NaixMonitor()

    tornado.ioloop.PeriodicCallback(monitor.main, 1000).start()
    tornado.ioloop.IOLoop.instance().start()
