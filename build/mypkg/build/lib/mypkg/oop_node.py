#! /usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("oop_node")
        self.get_logger().info("OOP Node Started!!")
        self.counter=0
        self.create_timer(1,self.timer_callback)

    def timer_callback(self):
        self.get_logger().info(f"Hello {self.counter}")
        self.counter+=1

def main():
    rclpy.init()
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()