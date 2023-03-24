FROM ubuntu:jammy
RUN apt update -y
RUN apt install python3 vim tmux tcpdump iputils-ping traceroute nmap python3-pip net-tools -y 
RUN mkdir -p /root/homework1
COPY .vimrc /root/.vimrc
WORKDIR /homework1
