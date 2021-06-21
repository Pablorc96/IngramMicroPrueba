FROM alpine:3.14

RUN apk add --no-cache python3 py3-pip
RUN apk add --no-cache geoip

COPY ./domains.txt /etc/domains.txt
COPY ./dns_script.py /etc/dns_script.py

WORKDIR /etc
CMD ["python3 ./dns_script.py"]
