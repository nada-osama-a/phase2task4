#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
class add(Node):
    def __init__(self):
        super().__init__("add")
        self.get_logger().info("server Node Started!!")
        self.server=self.create_service(AddTwoInts,'add_two_inits',self.add_callback)
        
    def add_callback(self, request: AddTwoInts.Request, response: AddTwoInts.Response):
        response.sum = request.a + request.b
        self.get_logger().info(f"Incoming request\na:{request.a} b:{request.b}")
        return response
       
def main(args=None):
    rclpy.init(args=args)
    node = add()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()