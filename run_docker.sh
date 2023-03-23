#!/bin/bash

name="cs3864"
output=`docker ps -aq --filter name=$name`

if [ -z "$output" ]
then
  docker run --name $name -it -v $(pwd):/homework1/ cs3864
else
  docker start $name
  docker exec -it $name /bin/bash
fi

