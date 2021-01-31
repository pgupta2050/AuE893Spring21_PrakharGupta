#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
PI = 3.1415926535897

def square_openloop():
    	# Starts a new node
    	rospy.init_node('robot_PG', anonymous=True)
    	velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    	vel_msg = Twist()

    	n_rotations=4
    	current_n=0
    	#Receiveing the user's input/defingin paramters
    	print("Let's move your robot")
    	length = 2.0
    	speed = 0.3
    	angular_speed = 0.3
    	while current_n< n_rotations:
    		st_line(speed, length, velocity_publisher, vel_msg)
    		rotate(angular_speed, velocity_publisher, vel_msg)
    		current_n=current_n+1

def st_line(speed, length,velocity_publisher,vel_msg):
	vel_msg.linear.x = speed
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	t0 = rospy.Time.now().to_sec()
	distance_current = 0
	while distance_current < length:
			velocity_publisher.publish(vel_msg)
			t1 = rospy.Time.now().to_sec()
			distance_current = speed*(t1-t0)

	vel_msg.linear.x = 0
	velocity_publisher.publish(vel_msg)

def rotate(angular_speed, velocity_publisher,vel_msg):
	vel_msg.angular.z = angular_speed
	t0= rospy.Time.now().to_sec()
	angle_current = 0

	while ( angle_current <= PI/2.0 ):
			velocity_publisher.publish(vel_msg)
			t1 = rospy.Time.now().to_sec()
			angle_current=angular_speed*(t1-t0)

	vel_msg.angular.z = 0
	velocity_publisher.publish(vel_msg) 

if __name__ == '__main__':
    try:
        #Testing our function
        square_openloop()
    except rospy.ROSInterruptException: pass
    
# - Prakhar Gupta
