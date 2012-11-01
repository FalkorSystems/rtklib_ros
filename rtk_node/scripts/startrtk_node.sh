#!/bin/sh
PIPEFILENAME=/tmp/rtk-pipe
if [ ! -p $PIPEFILENAME ]; then
    mkfifo $PIPEFILENAME
fi

`rospack find rtk_node`/nodes/rtk_node.py $* < $PIPEFILENAME
