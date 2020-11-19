#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point
from common_msgs.msg import cmn

rospy.init_node('sensor_publisher')
pub = rospy.Publisher('sensor_msg', cmn, queue_size=1)
msg = cmn()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.point = Point(x=second%4, y=second%7, z=second%5)
    pub.publish(msg)
    print "publish:", msg.timestamp.secs%100, msg.point.x, msg.point.y, msg.point.z
    rate.sleep()
