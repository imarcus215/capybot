import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan

def handleNewData(data):
	callback(data)

def drive(left, right):
	flw_pub.publish(left)
	frw_pub.publish(right)
	blw_pub.publish(left)
	brw_pub.publish(right)

def callback(data):
	midpoint = len(data.ranges)/2
	distance = data.ranges[midpoint]
	left = len(data.ranges) * (2/3)
	right = len(data.ranges) * (1/3)
	leftDistance = data.ranges[left]
	rightDistance = data.ranges[right]
	if distance > .4:
		drive(2, 2)
	else:
		if leftDistance < rightDistance:
			drive(2, -2)
		elif rightDistance < leftDistance:
			drive(-2, 2)
		else:
			drive(-2, 2)
		


rospy.init_node("maze")
flw_pub = rospy.Publisher("/front_left_wheel_controller/command", Float64, queue_size=0)
frw_pub = rospy.Publisher("/front_right_wheel_controller/command", Float64, queue_size=0)
blw_pub = rospy.Publisher("/back_left_wheel_controller/command", Float64, queue_size=0)
brw_pub = rospy.Publisher("/back_right_wheel_controller/command", Float64, queue_size=0)
laser = rospy.Subscriber("/scan", LaserScan, handleNewData)


rospy.spin()

