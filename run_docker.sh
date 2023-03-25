#!/bin/bash

name="cs3864"
output=`docker ps -aq --filter name=$name`

if [ -z "$output" ]
then
  if [[ "$OSTYPE" == "msys" ]]; then
    docker run --name $name -itd --network cs3864_net -v /$(pwd):/homework1/ cs3864
  else
    docker run --name $name -itd --network cs3864_net -v $(pwd):/homework1/ cs3864
  fi
fi

if [[ "$OSTYPE" == "msys" ]]; then
  winpty docker exec -it $name bash
else
  docker exec -it $name /bin/bash
fi
