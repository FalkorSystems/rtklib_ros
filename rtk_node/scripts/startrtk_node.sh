#!/bin/sh
PIPEFILENAME=${ROS_WORKSPACE}/sol1_pipe.pos
if [ ! -p $PIPEFILENAME ]; then
    mkfifo $PIPEFILENAME
fi

`rospack find rtk_node`/nodes/rtk_node.py $* < $PIPEFILENAME
