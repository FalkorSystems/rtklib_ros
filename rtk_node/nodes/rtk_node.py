#!/usr/bin/env python
import roslib
roslib.load_manifest( 'rtk_node' )

import rospy
from rtk_msgs.msg import *

import string
import sys

class RtkNode:
    def __init__( self ):
        self.fix_pub = rospy.Publisher( "rtk_fix", RtkFix )
        self.position_covariance = [0]*9
    
    def process_line( self, line ):
        split = string.split( line )
        if len( split ) == 15 and split[0] != '%':
            to_num = [float(a) for a in split]
            msg = RtkFix( RtkFixType( to_num[5] ),
                          RtkTime( to_num[0], to_num[1] ),
                          to_num[6],
                          to_num[2],
                          to_num[3],
                          to_num[4],
                          to_num[7:13],
                          to_num[13],
                          to_num[14] )
            self.fix_pub.publish( msg )

    def run( self ):
        while not rospy.is_shutdown():
            line = sys.stdin.readline()
            self.process_line( line )

def main():
    rospy.init_node('rtk_node')
    node = RtkNode()
    node.run()

if __name__  == '__main__':
    main()
