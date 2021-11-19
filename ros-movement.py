# license removed for brevity

import rospy

from geometry_msgs.msg import Twistfrequency = 5

delay = 12*5 # the latency is equal to 1sec when delqy equals 12 (to send the command)class Delayer():

    def __init__(self):

        self.last_data = None

        self.pub = rospy.Publisher('cmd_vel',Twist, queue_size=1) # Change msg and topic etc

        rospy.Subscriber('cmd_vel_undelayed',Twist,self.callback)

        self.buffer = [Twist()]*delay #buffer introduce lstency such as latency = frequency * delay.    def callback(self,data):

        self.last_data=data    def make_delay(self):

        if self.last_data is not None:

            new_message = self.last_data

            self.last_data = None

        else:

            print("data is none!")

            new_message = Twist()        self.buffer.pop(0)

        self.buffer.append(new_message)

        self.pub.publish(self.buffer[0])if __name__ == '__main__':

    rospy.init_node('mouvement_delayer', anonymous=True)

    rate = rospy.Rate(frequency)

    d = Delayer()

    while not rospy.is_shutdown():

        try:

            d.make_delay()

            rate.sleep()

        except rospy.ROSInterruptException:

            pass

    rospy.spin()
