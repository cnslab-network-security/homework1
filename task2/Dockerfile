FROM ubuntu:jammy
RUN apt update -y
RUN apt install openssh-server vsftpd apache2 net-tools -y
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT service ssh start && service vsftpd start && service apache2 start && bash
