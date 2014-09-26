import uuid
from json import loads, dumps
from tempfile import NamedTemporaryFile

from tornado.web import authenticated, asynchronous

from greengenes.web import r_server
from greengenes.web.handlers.base import BaseHandler


class ValidateHandler(BaseHandler):
    @authenticated
    def get(self):
        self.render("validate.html", user=self.current_user)

    @authenticated
    def post(self):
        data = self.request.files['tree_file'][0]['body']

        filename = None
        with NamedTemporaryFile(delete=False) as f:
            f.write(data)
            filename = f.name

        job_id = str(uuid.uuid4())
        job_details = {'type': 'validate',
                       'status': 'creating',
                       'msg': None,
                       'job_id': job_id,
                       'user': self.current_user,
                       'data': filename}

        user_msg = {'user': self.current_user,
                    'job_id': job_id,
                    'msg': 'creating'}

        r_server.rpush(self.current_user + ':messages', dumps(user_msg))
        r_server.publish(self.current_user, dumps(user_msg))

        r_server.hset('job', job_id, dumps(job_details))
        r_server.publish('compute', job_id)

        self.render("waiting.html", user=self.current_user, job_id=job_id,
                    job_status='creating')


class ValidateResultsHandler(BaseHandler):
    @authenticated
    def get(self, job_id):
        user = self.current_user

        job_details = r_server.hget('job', job_id)

        if job_details is None:
            raise ValueError("No data for job %s!" % job_id)

        job_details = loads(job_details)

        if 'results' not in job_details:
            raise ValueError("Results not found for job %s!" % job_id)

        self.render('validate_results.html', user=user, job_id=job_id,
                    results=job_details['results'])
