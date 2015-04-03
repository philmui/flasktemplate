# Dockerfile for a simple Flask application

FROM python:3-onbuild

EXPOSE 8000

CMD [ "gunicorn", "-c", "conf/gunicorn.conf", "app.hello:app" ]
