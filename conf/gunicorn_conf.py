import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1

# spew = True
debug = True
pidfile = /var/run/gunicorn.pid
loglevel = debug
accesslog = /var/log/gunicorn_access.log
errorlog = /var/log/gunicorn_error.log
