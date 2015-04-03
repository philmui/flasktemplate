import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1

# spew = True
debug = True
# pidfile = "/var/run/gunicorn.pid"
loglevel = "debug"
accesslog = "-"
errorlog = "-"
