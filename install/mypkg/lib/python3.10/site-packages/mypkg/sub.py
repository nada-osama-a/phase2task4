#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int16

class sub (Node):
    def __init__(self):
        super().__init__("sub")
        self.get_logger().info("sub Node Started!!")
        self.sub=self.create_subscription(Int16,'test_topic',self.sub_callback,10)

    def sub_callback(self,msg):
        self.get_logger().info(f"I heard : {msg.data}")
        if msg.data%2==0:
            self.get_logger().info("Even Number")
        else:
            self.get_logger().info("Odd Number")
            
def main():
    rclpy.init()
    node = sub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()    