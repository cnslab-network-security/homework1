FROM ubuntu:jammy
RUN apt update -y
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul
RUN apt install python3 vim tmux tcpdump iputils-ping traceroute nmap python3-pip net-tools tzdata -y 
RUN mkdir -p /root/homework1
RUN pip3 install scapy
COPY .vimrc /root/.vimrc
WORKDIR /homework1

