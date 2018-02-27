FROM alpine:latest AS openssl
RUN apk add --update openssl
WORKDIR /tmp
RUN openssl req \
  -x509 \
  -nodes \
  -days 365 \
  -newkey rsa:2048 \
  -subj "/C=/ST=/L=/O=/CN=demo" \
  -keyout example.key \
  -out example.crt

FROM nginx:1.13.9
WORKDIR /etc/nginx
RUN mkdir certs
COPY --from=openssl /tmp/example.* /etc/nginx/certs/