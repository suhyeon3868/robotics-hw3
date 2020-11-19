#!/usr/bin/env python
import rospy
from common_msgs.msg import cmn

def callback(msg):
    print "subscribe:", msg.timestamp.secs%100, msg.point.x, msg.point.y, msg.point.z

rospy.init_node('algorithm_subscriber')
sub = rospy.Subscriber('sensor_msg', cmn, callback)
rospy.spin()