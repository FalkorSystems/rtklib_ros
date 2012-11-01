#!/usr/bin/env python
import roslib
roslib.load_manifest( 'rtk_node' )

from rtk_msgs.msg import *

import re
import sys

class RtkNode:
    def __init__( self ):
        self.fix_pub = rospy.Publisher( "rtk_fix", RtkFix )
        self.world_frame = rospy.get_param( "~world_frame", "/nav" )
        self.position_covariance = [0]*9
    
    def process_line( self, line ):
        info = re.match( line,
                         "(\d+)\w+" +       # week
                         "(\d+\.+\d+)\w+" + # tow
                         "([-+]?\d+\.+\d+)\w+" + # lat
                         "([-+]?\d+\.+\d+)\w+" + # long
                         "([-+]?\d+\.+\d+)\w+" + # height
                         "(\d+)\w+" + # fix_type
                         "(\d+)\w+" + # num satellites
                         "(\d+\.+\d+)\w+" + # sdn
                         "(\d+\.+\d+)\w+" + # sde
                         "(\d+\.+\d+)\w+" + # sdu
                         "(\d+\.+\d+)\w+" + # sdne
                         "(\d+\.+\d+)\w+" + # sdeu
                         "(\d+\.+\d+)\w+" + # sdun
                         "(\d+\.+\d+)\w+" + # age
                         "(\d+\.+\d+)\w+" + # ratio
                         ".*" )
        if info == None:
            raise Exception( "invalid line: " + line )

        msg = RtkFix( RtkFixType( info.group( 5 ) ),
                      RtkTime( info.group( 0 ), info.group( 1 ) ),
                      info.group( 6 ),
                      info.group( 2 ),
                      info.group( 3 ),
                      info.group( 4 ),
                      info.group( 7, 8, 9, 10, 11, 12 ),
                      info.group( 13 ),
                      info.group( 14 ) )
        self.fix_pub.publish( msg )

    def run( self ):
        while True:
            line = sys.stdin.readline()
            self.process_line( line )


        
