FROM ubuntu:jammy
RUN apt update -y
RUN apt install python3 vim tmux -y
RUN mkdir -p /homework1
WORKDIR /homework1
