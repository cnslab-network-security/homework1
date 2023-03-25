#!/bin/bash
docker image build -t cs3864 .
docker network create cs3864_net --subnet 10.0.100.0/24
