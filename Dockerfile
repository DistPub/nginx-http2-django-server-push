FROM python:3.5
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple && ./manage.py collectstatic --noinput
CMD ./run_uwsgi.sh 8000