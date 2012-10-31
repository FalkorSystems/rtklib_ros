#!/bin/sh
`rospack find rtklib`/bin/rtkrcv -o `rospack find rtk_node`/conf/rtkrcv.conf -s -p 3713