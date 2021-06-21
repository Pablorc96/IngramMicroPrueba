FROM alpine:3.14

RUN apk add --no-cache python3 py3-pip
RUN apk add --no-cache geoip

WORKDIR /etc
CMD ["python3 /etc/dns_script.py"]
