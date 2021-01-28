Assignment2 - Git and turtle sim
28 Jan 2021
Prakhar Gupta

Task 1: Circle
circle.py - Makes the turtlebot go in a circle
To Run:
in the command line, enter: rosrun turtlesim turtlesim_node
in a new terminal, enter: rosrun assignment2 circle.py
When prompted, enter the forward speed, angular speed and the angle you want the bot to cover. In this case, we cover 360 degrees
The sample trajectory is as shown-
(Please see the trajectory snapshot in the ~Assignment2/trajectory_snapshots/)


Task2: square_openloop
square_openloop.py - Makes the turtlebot go in a square of user defined side length
To Run:
in the command line, enter: rosrun turtlesim turtlesim_node
in a new terminal, enter: rosrun assignment2 square_openloop.py
When prompted, enter the length of th square, forward speed, angular speed you want the bot to cover. In this case, we use 2 units, .2unit/sec, .2read/sec
The sample trajectory is as shown-
(Please see the trajectory snapshot in the ~Assignment2/trajectory_snapshots/)


Task 3: square_closedloop
square_closedloop.py - Makes the turtlebot go in a square of user defined side length
To Run:
in the command line, enter: rosrun turtlesim turtlesim_node
in a new terminal, enter: rosrun assignment2 square_closedloop.py
The bot will traverse the predifnied coordinates of the square.
The sample trajectory is as shown-
(Please see the trajectory snapshot in the ~Assignment2/trajectory_snapshots/)


Video: To view demo, play the video in ~src/Assignment2/videos/
(The video consists of all three scripts being run, in the same order as above)
