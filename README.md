### Demo

demo for integration nginx http2 server push feature with django

### How to use

> docker-compose up

### NGINX Solution

1. nginx v1.13.9 support server push (see https://www.nginx.com/blog/nginx-1-13-9-http2-server-push/)
2. enable server push in upstream (see dockerfile/nginx/conf/default.conf)

### Django Solution

1. mark resource which need to be server push in template (see applications/demo/templates/index.html)
1. add link header through middleware (see applications/demo/middlewares.py)
