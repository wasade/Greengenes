from json import loads

from IPython.parallel import Client

from greengenes.web import config
from greengenes.web import r_server


def fetch_and_validate(job_details):
    import t2t.cli as t2tcli  # noqa
    import traceback

    filename = job_details['data']

    try:
        res, error = t2tcli.fetch(filename)
    except Exception:
        job_details['msg'] = traceback.format_exc()
        job_details['status'] = 'error'
        return job_details

    if error:
        job_details['msg'] = res
        job_details['status'] = 'completed'
        return job_details

    try:
        res, error = t2tcli.validate(res, 10, True, True)
    except Exception:
        job_details['msg'] = traceback.format_exc()
        job_details['status'] = 'error'
        return job_details

    job_details['status'] = 'completed'
    if error:
        job_details['msg'] = res
    else:
        job_details['msg'] = ["Tree looks good!"]

    return job_details


def compute_wrapper(job_details):
    r_server = Redis()
    user_msg = {'user': job_details['user'],
                'job_id': job_details['job_id'],
                'msg': 'running'}

    job_details['status'] = 'running'
    r_server.rpush(job_details['user'] + ':messages', dumps(user_msg))
    r_server.publish(job_details['user'], dumps(user_msg))
    r_server.hset('job', job_details['job_id'], dumps(job_details))

    job_details = method_lookup[job_details['type']](job_details)

    if job_details['status'] == 'error':
        user_msg['msg'] = 'error'
    else:
        user_msg['msg'] = 'completed'

    job_details['status'] = 'completed'
    r_server.rpush(job_details['user'] + ':messages', dumps(user_msg))
    r_server.publish(job_details['user'], dumps(user_msg))
    r_server.hset('job', job_details['job_id'], dumps(job_details))


def compute(bv):
    pubsub = r_server.pubsub()
    pubsub.subscribe('compute')
    listener = pubsub.listen()

    while True:
        msg = next(listener)

        try:
            job_details = loads(r_server.hget('job', msg['data']))
            print "success: %s" % repr(job_details)
        except:
            print msg
            continue

        print "starting..."
        res = bv.apply_async(compute_wrapper, job_details)
        print "returned"
        print res.result

method_lookup = {'validate': fetch_and_validate}


if __name__ == '__main__':
    try:
        parallel_client = Client(profile=config.compute_profile)
        parallel_view = parallel_client.load_balanced_view()
        parallel_dview = parallel_client[:]
    except IOError:
        raise IOError("It doesn't look like a cluster is running!")

    with parallel_client[:].sync_imports(quiet=True):
        from json import dumps
        from redis import Redis
    parallel_dview['fetch_and_validate'] = fetch_and_validate
    parallel_dview['method_lookup'] = method_lookup

    compute(parallel_view)
