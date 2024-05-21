#!/bin/bash
docker network inspect cs3864_net | grep Subnet
docker compose up
