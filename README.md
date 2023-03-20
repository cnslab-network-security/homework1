# Network Security Lab #1

In this lab, we will implement basic network programs (especially TCP client-server model) and some well-known network scanners, such as UDP scanner and traceroute. As previously mentioned, we will use Python 3 in order to quickly build and run network applications.

## Due Date: April XX

## Task 0: Installing and Running Docker

To run the same environment across different OSes (i.e., Windows, macOS), we'll use Docker, a lightweight virtualization platform. For this, you first need to install Docker. The easiest way is to install Docker Desktop, which can be downloaded from [here](https://www.docker.com/products/docker-desktop/). You will need to choose a suitible binary according to your OS and hardware architecture. For example, I need to install the Docker Desktop built for Apple Chip because my laptop is m1 MacBook. 

Once you install Docker Desktop and run it, you will be able to use Docker commands. You can check this by openning terminal and type `docker -v`. For example, in Windows, you can open 'PowerShell' and type it. In macOS, you can use the terminal app or iTerm3. If you see that the terminal prints a Docker version, you're now prepared to run our Dockerfile.

This directory contains a shell script file, `run_docker.sh`. Open the terminal and type `bash run_docker.sh`. You should see the following output:

```
jinwoo@MacBook-Pro homework1 % bash run_docker.sh
root@9f963f7291fd:/homework1#
```

Do you know what happened? Your Docker engine builds our Dockerfile, runs our container, and finally enters the contianer. You can check this by seeing that the username and hostnames are different from that of your original host.


## Task1: Implementing Basic TCP Client-Server

- In our class, we have learned that 
