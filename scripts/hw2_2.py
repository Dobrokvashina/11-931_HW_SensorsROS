#!/usr/bin/env python
import rospy
import rosbag
from sensor_msgs.msg import Temperature, Range
import threading
import time
import math

temp_msgs = []
range_msgs = []

def waitForTime():
    time.sleep(300)
    rospy.signal_shutdown("Shutting down the node")
    print("writting")
    time.sleep(3)

    with rosbag.Bag("test.bag", 'w') as bag:

                for msg in temp_msgs:
                    bag.write('/temperature',msg, msg.header.stamp)

                for msg in range_msgs:
                    bag.write('/sound',msg, msg.header.stamp)

    print("finished")

def temp_callback(msg):
    temp_msgs.append(msg)

def range_callback(msg):
    range_msgs.append(msg)


def collect():
        rospy.Subscriber('/temperature', Temperature, temp_callback)
        rospy.Subscriber('/sound', Range, range_callback)
        rospy.spin()


if __name__ == '__main__':
        try:
                rospy.init_node('hw2_2', anonymous=False)
                wait_thread = threading.Thread(target=waitForTime)
                wait_thread.start()
                print("started")
                collect()
        except rospy.ROSInterruptException:
                pass
