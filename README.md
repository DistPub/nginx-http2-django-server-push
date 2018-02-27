### Demo

demo for integration nginx http2 server push feature with django

![demo](https://user-images.githubusercontent.com/2248369/36716748-5d1aca3c-1bd6-11e8-945e-05944576a250.png)

### How to use

> docker-compose up

### NGINX Solution

1. nginx v1.13.9 support server push (see https://www.nginx.com/blog/nginx-1-13-9-http2-server-push/)
2. enable server push in upstream (see dockerfile/nginx/conf/default.conf)

### Django Solution

1. mark resource which need to be server push in template (see applications/demo/templates/index.html)
1. add link header through middleware (see applications/demo/middlewares.py)
