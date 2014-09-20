from json import loads

from toredis import Client
from tornado.websocket import WebSocketHandler
from tornado.gen import engine, Task

from greengenes.web import r_server
from greengenes.web.handlers.base import BaseHandler


class MessageHandler(WebSocketHandler):
    def __init__(self, *args, **kwargs):
        super(MessageHandler, self).__init__(*args, **kwargs)
        self.redis = Client()
        self.redis.connect()

    def open(self):
        print "websocket opened"

    def get_current_user(self):
        user = self.get_secure_cookie("user")
        if user is None:
            return ''
        else:
            return user.strip('" ')

    def on_message(self, msg):
        msginfo = loads(msg)
        self.channel = msginfo['user']
        self.listen()

    def listen(self):
        self.redis.subscribe(self.channel, callback=self.callback)
        oldmessages = r_server.lrange('%s:messages' % self.channel, 0, -1)
        if oldmessages is not None:
            for message in oldmessages:
                self.write_message(message)

    def callback(self, msg):
        if msg[0] == 'message':
            self.write_message(msg[2])

    @engine
    def on_close(self):
        yield Task(self.redis.unsubscribe, self.channel)
        self.redis.disconnect()


class WaitingRedirect(BaseHandler):
    #@authenticated
    def get(self, job_id):
        job_details = r_server.hget('job', job_id)

        if job_details is None:
            raise ValueError("No job details for %s!" % job_id)

        job_details = loads(job_details)
        self.render(job_details['type'] + '_results.html', job_id=job_id, msg=job_details['msg'])
