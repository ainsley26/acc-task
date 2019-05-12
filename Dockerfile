FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update python py-pip
RUN pip install -r requirements.txt
