#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def circle():
    # Starts a new node
    rospy.init_node('robot_PG', anonymous=True)

    # publish to /cmd_vel topic
    velocity_publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    vel_msg = Twist()
    
    #Receiveing the user's input/ defining inputs
    print("Let's move your robot")
    speed = .5
    #speed = rospy.get_param('~speed')
    angular_speed = 36
    #angular_speed = rospy.get_param('~angular_speed')
    angle = 360
    #angle = rospy.get_param('~angle')
    isClockwise = 1
    isForward = 1
    
    #Converting from angles to radians
    angular_speed = angular_speed*2*PI/360
    relative_angle = angle*2*PI/360
    
    #Checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
        
    if isClockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
        
    #Since we are moving in 2D circle
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    
    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        t0 = float(rospy.Time.now().to_sec())
        current_angle = 0
        
        while(current_angle < relative_angle):
        	velocity_publisher.publish(vel_msg)
        	t1 = rospy.Time.now().to_sec()
        	current_angle = angular_speed*(t1-t0)

        #Forcing our robot to stop
        vel_msg.angular.z = 0
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
        rospy.spin()

if __name__ == '__main__':
    try:
        #Testing our function
        circle()
    except rospy.ROSInterruptException: pass
    
# - Prakhar Gupta
