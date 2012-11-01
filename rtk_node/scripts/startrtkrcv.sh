#!/bin/sh
PIPEFILENAME=${ROS_WORKSPACE}/sol1_pipe.pos
if [ ! -p $PIPEFILENAME ]; then
    mkfifo $PIPEFILENAME
fi

RTKCONFTEMP=`mktemp /tmp/rtkconf.XXX`
RTKCONF=`rospack find rtk_node`/conf/rtkrcv.conf
sed -e "s#ROS_WORKSPACE#${ROS_WORKSPACE}#" < $RTKCONF > $RTKCONFTEMP
`rospack find rtklib`/bin/rtkrcv -o $RTKCONFTEMP -s -p 3713 
