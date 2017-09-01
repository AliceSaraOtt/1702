#coding:utf8
from tornado.options import options, define, parse_command_line
from django.core.wsgi import get_wsgi_application
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import os, sys
#from tornado.web import StaticFileHandler
#from django.conf import settings

SITE_ROOT = os.path.dirname(os.getcwd()) 
PROJECT_NAME = os.path.basename(os.getcwd()) #获取项目名称，也就上级目录名称

sys.path.append( SITE_ROOT )
os.environ['DJANGO_SETTINGS_MODULE'] = PROJECT_NAME + '.settings'

define('port', type=int, default=8080)

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello from tornado')

def main():
    parse_command_line()

    wsgi_app = tornado.wsgi.WSGIContainer(get_wsgi_application())

    tornado_app = tornado.web.Application(
        [
            ('/hello-tornado', HelloHandler),  # 把所有路由转交给django app
            #('/static/(.*)', StaticFileHandler,{'path':os.path.join(settings.BASE_DIR,'collectstatic')}),  # 把所有路由转交给django app
            ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
        ],
        # debug=True
    )

    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
        main()
