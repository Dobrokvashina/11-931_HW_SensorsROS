#!/usr/bin/env python
import rospy
from std_msgs.msg import String


class WaitForInput:

        def __init__(self):
                pass

        def wait(self):
                rospy.init_node('hw2_1', anonymous=False)
                pub = rospy.Publisher('keyCode', String, queue_size=10)
                vel = String()
                while not rospy.is_shutdown():
                        char = str(raw_input())
                        char = char.lower()
                        vel.data = char
                        pub.publish(vel)

if __name__ == '__main__':
        try:
                st = WaitForInput()
                st.wait()
        except rospy.ROSInterruptException:
                pass
