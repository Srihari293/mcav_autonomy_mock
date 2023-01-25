# Libraries
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Range

# Class declaration
class Ebreak(Node):
    def __init__(self):
        super().__init__('laser_sensor')
        self.ebrake_publisher_ = self.create_publisher(Twist, "cmd_vel", 10)
        self.laserSensor_subscriber_ = self.create_subscription(Range, "laser/range", self.callback, 10)
        self.get_logger().info('E-breaking module initiated')
    
    def callback(self, msg: Range):        
        # Code for breaking when the distance is less than 5 meters
        threshold = 5
        if (msg.range <= threshold):
            # Both linear and angular velocity attributes are set to 0 in a message
            message = Twist(linear = Vector3(x=0.0, y=0.0, z=0.0),
                            angular = Vector3(x=0.0, y=0.0, z=0.0)
                            )
            # The above message is published by the ebrake_publisher_ publisher
            self.ebrake_publisher_.publish(message)
            self.get_logger().info("Object detected, applying Emergency break")
        
        else:
            self.get_logger().info("Distance to the nearest object is: {}".format(msg.range))


    
def main(args = None):
    rclpy.init(args=args)
    Ebreak_module = Ebreak()
    rclpy.spin(Ebreak_module)
    Ebreak_module.destroy_node()
    rclpy.shutdown()

if __name__ == "main":
    main()