#!/bin/bash

if [ -z $1 ];
then
    echo "usage $0 <foundationPose root dir>"
    exit 1
fi

export PYTHONPATH=$PYTHONPATH:$1
