#! /usr/bin/env python3

import rclpy
from rclpy.node import Node


def main(args=None):
    rclpy.init(args=args)
    node = Node("my_node")
    node.get_logger().info("Hello From My 1st Node")
    # rclpy.spin(node)
    # node.destroy_node()
    rclpy.shutdown()


if __name__=="__main__":
    main()