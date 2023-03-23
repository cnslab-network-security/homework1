FROM ubuntu:jammy
RUN apt update -y
RUN apt install python3 vim tmux tcpdump -y
RUN mkdir -p /root/homework1
COPY .vimrc /root/.vimrc
WORKDIR /homework1
