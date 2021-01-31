#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from math import pow, atan2, sqrt

class TurtleBot:

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)

        self.scan_subscriber = rospy.Subscriber('/scan', LaserScan, self.update_scan)

        self.rate = rospy.Rate(10)

        self.scan = LaserScan() #not updated or used here

        self.current_distance=1e3
    
    def update_scan(self,incoming_data):
        # update current_distance with the value for 0 deg angle of the scan array "ranges"
        # uipdate only if the incoming range data is within the limits
        if incoming_data.ranges[0]>incoming_data.range_min and incoming_data.ranges[0]<incoming_data.range_max:
            self.current_distance = incoming_data.ranges[0]
        else:
            self.current_distance=self.current_distance


    def move(self):
        """Moves the turtle to the goal."""
        
        # Defining the input paramters
        speed = 0.3
        distance_tolerance = 0.1
        distance_safe = 0.4
        vel_msg = Twist()
                             	
        # Keep moving till the robot sees an obstacle at less than safe distancce
        while self.current_distance > distance_safe:
            vel_msg.linear.x = speed
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            	
            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
         	 # Publish at the desired rate.
            self.rate.sleep()
	        

        # Stopping our robot
        vel_msg.linear.x = 0
        self.velocity_publisher.publish(vel_msg)

        # If we press control + C, the node will stop.
        rospy.spin()

if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.move()
   
    except rospy.ROSInterruptException:
        pass    

# - Prakhar Gupta
