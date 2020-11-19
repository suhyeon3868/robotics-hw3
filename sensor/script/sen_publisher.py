#!/usr/bin/env python

import rospy
import random
from common_msgs.msg import cmn
from common_msgs.srv import AddTwoNum, AddTwoNumRequest

rospy.init_node('service_client')
rospy.wait_for_service('add_two_number')
requester = rospy.ServiceProxy('add_two_number', AddTwoNum)
pub = rospy.Publisher('cmn', cmn, queue_size=1)
print "requester type:", type(requester), ", callable?", callable(requester)
msg=cmn()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp=rospy.get_rostime()
    sec=msg.timestamp.secs%100
    pub.publish(msg)
    if sec % 10 == 0:
        req = AddTwoNumRequest(a=random.randint(1,50),b=random.randint(1,50))
        res = requester(req)
        print sec, "request:", req.a, req.b, "response:", res.sum
    rate.sleep()

