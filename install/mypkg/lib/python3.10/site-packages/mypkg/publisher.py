#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int16
import random
class publisher_Node(Node):
    def __init__(self):
        super().__init__("publisher")
        self.get_logger().info("publisher Node Started!!")
        self.publisher_Node=self.create_publisher(Int16,'test_topic',10)
        self.counter=0
        self.num=0
        self.create_timer(1,self.publisher_callback)
    def publisher_callback(self):
        msg=Int16()
        self.num=random.randint(0,100)
        msg.data=self.num
        self.publisher_Node.publish(msg)
    #def timer_callback(self):
    #    self.get_logger().info(f"Hello {self.counter}")
    #    self.counter+=1
def main():
    rclpy.init()
    node = publisher_Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()    

if __name__ == '__main__':
    main()