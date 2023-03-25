#!/bin/bash

name="cs3864"
output=`docker ps -aq --filter name=$name`

if [ -z "$output" ]
then
  docker run --name $name -itd --network cs3864_net -v $(pwd):/homework1/ cs3864
fi

docker exec -it $name /bin/bash

