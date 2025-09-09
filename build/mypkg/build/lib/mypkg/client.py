#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial
class add_c(Node):
    def __init__(self):
        super().__init__("add_client")
        self.get_logger().info("Client Node Started!!")
        self.client=self.create_client(
            AddTwoInts,'add_two_inits'
            )

    def send_request(self,a,b):
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = self.client.call_async(request)
        future.add_done_callback(partial(self.callback_future, request=request))  

    def callback_future(self, future,request):
            response = future.result()
            self.get_logger().info(f"Result of add : {response.sum}")
        
def main(args=None):
    rclpy.init(args=args)
    node = add_c()
    node.send_request(5,6)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()