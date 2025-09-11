#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import termios
import tty

class TurtleTeleop(Node):
    def __init__(self):
        super().__init__('turtle_teleop')
        self.pub1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.settings = termios.tcgetattr(sys.stdin)
        self.get_logger().info("Use arrow keys for turtle1, WASD for turtle2")

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

    def run(self):
        try:
            while True:
                key = self.get_key()
                twist1 = Twist()
                twist2 = Twist()
                if key == '\x1b': 
                    key2 = sys.stdin.read(2)
                    if key2 == '[A':  
                        twist1.linear.x = 2.0
                    elif key2 == '[B':  
                        twist1.linear.x = -2.0
                    elif key2 == '[C':  
                        twist1.angular.z = -2.0
                    elif key2 == '[D': 
                        twist1.angular.z = 2.0
              
                elif key.lower() == 'w':
                    twist2.linear.x = 2.0
                elif key.lower() == 's':
                    twist2.linear.x = -2.0
                elif key.lower() == 'a':
                    twist2.angular.z = 2.0
                elif key.lower() == 'd':
                    twist2.angular.z = -2.0
                else:
                    twist1.linear.x = twist1.angular.z = 0.0
                    twist2.linear.x = twist2.angular.z = 0.0

                self.pub1.publish(twist1)
                self.pub2.publish(twist2)
        except Exception as e:
            print(e)
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleTeleop()
    node.run()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()