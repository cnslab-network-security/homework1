# Network Security Lab #1

## Due Date: 2023 April 15

In this lab, we will implement simple network scanners and NIDS to understand how they work more intuitively. As previously mentioned, we will use Python 3 in order to quickly build and run network applications.

This repository has four subdirectories, each of which corresponds to an individual task. Please read the following descriptions carefully before you get started.

## Installing and Running Docker

To run the same environment across different OSes (i.e., Windows, macOS), we'll implement and test our programs on a Docker container, a lightweight virtualization platform. The easiest way of using Docker at any OS is to install Docker Desktop, which can be downloaded from [here](https://www.docker.com/products/docker-desktop/). You will need to choose a suitable binary according to your OS and hardware architecture. For example, I installed the Docker Desktop built for Apple Chip because my laptop is m1 MacBook. 

**!!Important**: if you use Windows, you must install **Git Bash** to make the provided bash script work well. Please click [this link](https://git-scm.com/download/win) and install the Git Desktop.

Once you install Docker Desktop and run it, you will be able to use Docker commands. You can check this by opening terminal (i.e., Git Bash if you use Windows) and type `docker -v`. For example, in Windows, you should use Git Bash (I strongly recommend it because PowerShell didn't work well from my experience.). In macOS, you can use the terminal app or iTerm2. If you see that the terminal prints a Docker version, you're now prepared to run our Dockerfile.

This directory contains some useful shell script files, such as `build_docker.sh` and `run_docker.sh`. Open the terminal and type `bash build_docker.sh`. It builds a Docker container image by reading `Dockerfile`.

Now type `bash run_docker.sh`. You should see the following output:

```
jinwoo@MacBook-Pro homework1 % bash run_docker.sh
root@9f963f7291fd:/homework1#
```

What just happened? Your Docker engine built a Docker image through reading Dockerfile, ran a container, and finally entered it. You can check this by seeing that the username (i.e., root) and hostname (9f963f7291fd) are different from that of your host's.

It's important to note that a container is an isolated environment similar to a virtual machine (VM), so writing/removing a certain file won't affect your host directory. However, we often want to write a program from a host-side using IDEs, such as [Pycharm](https://www.jetbrains.com/ko-kr/pycharm/) and [VSCode](https://code.visualstudio.com/). For this, I made this directory transparent to the container, so if you make a change from the host side, it will be reflected from the container-side immediately. You can check this by typing the `ls` command as follows:

```
root@a95a45a58379:/homework1# ls
Dockerfile  README.md  run_docker.sh  init_docker.sh  task1  task2  task3
```

You can see the same files of this directory at the container-side as well.

**Note**: I strongly recommend that you implement and test your programs in the given Docker container. If you do so in your OS (e.g., Windows), some unexpected problems may occur when running your program in the container.

## Some Useful Tools

In this lab, I assume that you're familiar with Linux systems. But, those who're NOT familiar with Linux systems can refer to [here](https://www.guru99.com/linux-commands-cheat-sheet.html) to look at some important commands.

Also, you may need to utilize following tools for this lab:

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

When testing network programs, you may want to see how actual packets look like and how they are exchanged. You can use `tcpdump`, a popular command line utility for capturing packets in Linux. You can simply type:

```
$ tcpdump -i lo -n
```

The above command will capture and display all packets involved in the interface `lo` whose IP address is "127.0.0.1".

### vi

`vi` is a popular editor included by default on Linux operating systems. For example, you can simply type:

```
$ vi server.py
```

to create a python file named `server.py` and start editing.

If you feel that `vi` is inconvenient, you can use other editors and IDEs as well, such as [Sublime Text](https://www.sublimetext.com/), VSCode, and pyCharm.

## Writing-up

You need to write a report to describe how you implement and resolve challenges. Each task has some required questions you need to answer in your report.
You can use any tool for writing, such as Word and 아래아한글, but you must submit a `.pdf` file, whose name should be `lab1_your_student_number.pdf`.

## Submission

After finishing this lab, you need to compress the **contents** of this directory with your **report** before submission.
The compressed file should be `lab1_your_student_number.zip`.
You must submit your file to KLAS.
