#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def axisMove():

    print("Mover ejes")
    xCoord = float(input("Ingrese la posición de x: "))-0.255
    yCoord = float(input("Ingrese la posición de y: "))+0.175
    zCoord = float(input("Ingrese la posición de z: "))

    x_message.data = xCoord
    y_message.data = yCoord
    z_message.data = zCoord

    x_axis.publish(x_message)
    y_axis.publish(y_message)
    z_axis.publish(z_message)

# try-catch
if __name__ == '__main__':
    # start node 
    rospy.init_node('cnc_move', anonymous=True)

    # publishers
    x_axis = rospy.Publisher('/x_axis_position_controller/command', Float64, queue_size=10)
    y_axis = rospy.Publisher('/y_axis_position_controller/command', Float64, queue_size=10)
    z_axis = rospy.Publisher('/z_axis_position_controller/command', Float64, queue_size=10)

    # messages
    x_message = Float64()
    y_message = Float64()
    z_message = Float64()

    while True:
        axisMove()
