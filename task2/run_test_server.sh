#!/bin/bash
docker build -t task2-tester .
docker run -itd --name task2 --network cs3864_net task2-tester
docker inspect task2 | grep IPAddress
