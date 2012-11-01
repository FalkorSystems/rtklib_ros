#!/bin/sh
PIPEFILENAME=/tmp/rtk-pipe
if [ ! -p $PIPEFILENAME ]; then
    /usr/bin/mkfifo $PIPEFILENAME
fi

RTKCONFTEMP=`mktemp /tmp/rtkconf.XXX`
RTKCONF=`rospack find rtk_node`/conf/rtkrcv.conf
sed -e "s|PIPEFILENAME|$PIPEFILENAME|" < $RTKCONF > $RTKCONFTEMP
`rospack find rtklib`/bin/rtkrcv -o $RTKCONFTEMP -s -p 3713 &

