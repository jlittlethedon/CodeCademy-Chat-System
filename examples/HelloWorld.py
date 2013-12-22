###
# How to run this example:
# Install python: sudo apt-get install python
# Install the python package manager: sudo apt-get install python-pip
# Install the tornado web server: sudo pip install tornado
# Run this file: python HelloWorld.py
# Point your web browser at this server: http://localhost:8888 (If you aren't running python on localhost, replace localhost with the IP address of the server.)
###

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()