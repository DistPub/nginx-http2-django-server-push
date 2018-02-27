FROM python:3.5
WORKDIR /code
ADD requirements.txt /code
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
ADD . /code
RUN ./manage.py collectstatic --noinput
CMD ./run_uwsgi.sh 8000