# Capybot
Capybot is a platform for learning ROS by manipulating a robot in a maze in gazebo.

## Usage
    roslaunch capybot_launch capybot_gazebo.launch [diff_drive:=false|true]

* `diff_drive` Specifies if the robot should be controlled by `Twist` messages or if the wheels should
  be controlled directly

