# Network Security Lab #1

In this lab, we will implement basic network programs (especially TCP client-server model) and some well-known network scanners, such as UDP scanner and traceroute. As previously mentioned, we will use Python 3 in order to quickly build and run network applications.

[Prerequisite: Installing and Running Docker] (#Prerequisite:-Installing-and-Running-Docker)
[Prerequisite: Some Useful Tools] (#Prerequisite:-Some-Useful-Tools)

## Due Date: April XX

## Prerequisite: Installing and Running Docker

To run the same environment across different OSes (i.e., Windows, macOS), we'll use Docker, a lightweight virtualization platform. For this, you first need to install Docker. The easiest way is to install Docker Desktop, which can be downloaded from [here](https://www.docker.com/products/docker-desktop/). You will need to choose a suitable binary according to your OS and hardware architecture. For example, I need to install the Docker Desktop built for Apple Chip because my laptop is m1 MacBook. 

Once you install Docker Desktop and run it, you will be able to use Docker commands. You can check this by openning terminal and type `docker -v`. For example, in Windows, you can use PowerShell. In macOS, you can use the terminal app or iTerm2. If you see that the terminal prints a Docker version, you're now prepared to run our Dockerfile.

This directory contains a shell script file, `run_docker.sh`. Open the terminal and type `bash run_docker.sh`. You should see the following output:

```
jinwoo@MacBook-Pro homework1 % bash run_docker.sh
root@9f963f7291fd:/homework1#
```

What just happened? Your Docker engine built a Docker image through reading Dockerfile, ran a container, and finally entered it. You can check this by seeing that the username (i.e., root) and hostname (9f963f7291fd) are different from that of your host's.

It's important to note that a container is an isolated environment similar to a virtual machine (VM), so writing/removing a certain file won't affect your host directory. However, we often want to write a program from a host-side using IDEs, such as Pycharm and VSCode. For this, I made this directory transparent to the container, so if you make a change from the host side, it will be reflected from the container-side immediately. You can check this by typing the `ls` command as follows:

```
root@a95a45a58379:/homework1# ls
Dockerfile  README.md  run_docker.sh  init_docker.sh  task1  task2  task3
```

As noted, you can see the same files of this directory at the container-side as well.

## Prerequisite: Some Useful Tools

### tmux

When you do network programming, you may want to split a terminal into several windows to run programs there individually. For this purpose, you can simply type `tmux` after running a Docker container, and then you will see a new tmux terminal. There are many useful tmux commands, but it's enough to use the followings:

```
ctrl+b, "       Vertical split
ctrl+b, %       Horizontal Split
ctrl+b, arrow   Move to the pane 
ctrl+b, x       Kill pane   
```

For more information, please refer to [here](https://gist.github.com/MohamedAlaa/2961058).

### tcpdump

While doing this lab, you may want to see how packets are exchanged. `tcpdump` is a popular command line utility for capturing packets. You can simply type:

```
$ tcpdump -i lo -n
```

The above command will capture and display all packets involved the interface `lo` whose IP address is "127.0.0.1".

## Task 1: Implementing Echo Client-Server

In our class, we have learned that a basic TCP client-server model can be easily implemented with Python. This is the good starting point for learning how to implement socket programs. The `task1` directory has `echo_server.py` and `echo_client.py` where some code snippets are already written. Fill the rest of the code where the `TODO:` is commented in order to make them working properly.

If you write a code properly, the programs will be working as follows:

1. Run `echo_server.py`
2. Run `echo_client.py`
3. Type any string you want to send to server from a client side.
4. Check that the string is printed out from the server side.


## Task 2: Implementing Toy Honeypot

## Task 3: Implementing Port Scanner
