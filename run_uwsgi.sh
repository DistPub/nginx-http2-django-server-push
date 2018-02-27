#!/bin/bash
uwsgi --socket=0.0.0.0:$@ --enable-threads --pidfile=uwsgi-$@.pid --logto=uwsgi-$@.log\
  --module=conf.wsgi:application\
  --master --vacuum --check-static .