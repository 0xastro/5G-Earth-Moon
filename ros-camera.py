#!/usr/bin/env python
# license removed for brevity
import rospy
from sensor_msgs.msg import CompressedImagebuffer_size = 15*5 #Camera fps is 15 so lqtency is 1sec zhen buffer size equal 15class Delayer():
    def __init__(self):
        self.frame=CompressedImage()
        rospy.init_node('image_delayer', anonymous=True)
        self.pub = rospy.Publisher('camera/color/image_raw_delayed/compressed',CompressedImage, queue_size=1)
        rospy.Subscriber('camera/color/image_raw/compressed',CompressedImage,self.callback)
        self.buffer = []
        for x in range(buffer_size):
            self.buffer.append(self.frame)    def callback(self,data):
        self.frame=data
        self.buffer.append(self.frame)
        self.pub.publish(self.buffer[0])
        self.buffer.pop(0)if __name__ == '__main__':
    try:
        d = Delayer()
    except rospy.ROSInterruptException:
        pass
    rospy.spin()
