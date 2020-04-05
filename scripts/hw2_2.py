#!/usr/bin/env python
import rospy
import rosbag
from sensor_msgs.msg import Temperature, Range
import threading
import time
import math

bag = rosbag.Bag("test.bag", 'w')

def waitForTime():
    time.sleep(900)
    rospy.signal_shutdown("Shutting down the node")
    bag.close()

def temp_callback(msg):
    try:
        bag.write('/temperature', msg, rospy.Time.now())
    except Exception:
        print("error temp")

def range_callback(msg):
    try:
        bag.write('/sound', msg, rospy.Time.now())
    except Exception:
        print("error range")


def collect():
        rospy.Subscriber('/temperature', Temperature, temp_callback)
        rospy.Subscriber('/sound', Range, range_callback)
        rospy.spin()


if __name__ == '__main__':
        try:
                rospy.init_node('hw2_2', anonymous=False)
                wait_thread = threading.Thread(target=waitForTime)
                wait_thread.start()
                collect()
        except rospy.ROSInterruptException:
                pass
