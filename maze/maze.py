import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
def handleNewData(data):
	print(data)

def drive(left, right):
	flw_pub.publish(left)
	frw_pub.publish(right)
	blw_pub.publish(left)
	brw_pub.publish(right)

def callback(data):
	midpoint = len(data.ranges)/2
	distance = data.ranges[midpoint]
	while(distance > 0):
		if distance < 0.25:
			drive(1.0, 1.0)
		else:
			sleep(1)
			drive(-2.0, -2.0)


rospy.init_node("maze")
flw_pub = rospy.Publisher("/front_left_wheel_controller/command", Float64, queue_size=0)
frw_pub = rospy.Publisher("/front_right_wheel_controller/command", Float64, queue_size=0)
blw_pub = rospy.Publisher("/back_left_wheel_controller/command", Float64, queue_size=0)
brw_pub = rospy.Publisher("/back_right_wheel_controller/command", Float64, queue_size=0)
laser = rospy.Subscriber("/scan", LaserScan, handleNewData)



rospy.spin()
