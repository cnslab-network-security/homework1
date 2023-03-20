# Network Security Lab1

In this lab, we will implement basic network programs (especially TCP client-server model) and some well-known network scanners, such as UDP scanner and traceroute. As previously mentioned, we will use Python 3 in order to quickly build and run network applications.

## Task 0: Installing and Running Docker

- To run the same environment across different OSes (i.e., Windows, macOS), we'll use Docker, a lightweight virtualization platform. For this, you first need to install Docker. The easiest way is to install Docker Desktop, which can be downloaded from https://www.docker.com/products/docker-desktop/. You will need to choose a suitible binary according to your OS and hardware architecture. For example, I need to install the Docker Desktop built for Apple Chip because my laptop is macOS m1. 

Once you install Docker Desktop and run it, you will be able to use Docker commands. You can check this by openning terminal and type `docker -v`. For example, in Windows, you can open '명령프롬프트' or 'PowerShell' and type it. If you see that the terminal prints a Docker version, you're now prepared to run our Dockerfile.

This directory contains a shell script file, `run_docker.sh`.


## Task1: Implementing Basic TCP Client-Server

- In our class, we have learned that 
