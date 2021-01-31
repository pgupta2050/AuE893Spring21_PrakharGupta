### Assignment 3 - Turtlebot3 and Gazebo

#### circle.py

Make the TurtleBot3 move in a circle with constant twist velocity

![Move in a circle](./videos/circle.gif)

#### square.py

Make the TurtleBot3 move in a square with 0.3 angular velocity and 0.3 linear velocity in open loop

![Move in a square](./videos/square.gif)

#### emergency_braking.py

Make the TurtleBot3 stop when it gets too close to the wall

![Emergency brake](./videos/emergency_brake.gif)

### Running

- Clone the project

```bash
$ git clone https://github.com/pgupta2050/AuE893Spring21_PrakharGupta.git
```

- Run the create package command:

```bash
$ cd ./AuE8930Spring21_PrakharGupta/git_ws/src/
$ catkin_create_pkg assignment3_turtlebot3 rospy std_msgs sensor_msgs
```

- Build code in a catkin workspace `git_ws`

```bash
$ cd ./AuE8930Spring21_PrakharGupta/git_ws
$ catkin_make
$ source ./git_ws/devel/setup.bash
```

- Make the node executable

```bash
$ cd ./AuE8930Spring21_PrakharGupta/git_ws/src/assignment3_turtlebot3/src/srcipts
$ chmod u+x *.py
```

- Launch ROS nodes in the `assignment3_turtlebot3` package

```bash
$ roslaunch assignment3_turtlebot3 move.launch code:=circle
$ roslaunch assignment3_turtlebot3 move.launch code:=square
$ roslaunch assignment3_turtlebot3 emergency_braking.launch
```

 ### Note

The launch files launch nodes for running Gazebo with the required .world file thats placed in the /src folder. Then it spwans a turtlebot3 Burger in the world. It then launches the .py files that execute the movement of the turtlebot3.

