FROM alpine:3.6

MAINTAINER Deniau Antonin <deniau.antonin@protonmail.com>

RUN apk update && apk add \
        scapy python \
        && rm -rf /var/cache/apk/*

COPY ./hang.sh /opt/hang
COPY ./traceroute.py /opt/traceroute

RUN chmod 777 /opt/hang
RUN chmod 777 /opt/traceroute

ENTRYPOINT ["/opt/hang"]
