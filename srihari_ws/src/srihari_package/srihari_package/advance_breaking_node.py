# Libraries
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Range

# Class delcaration for advance emergency breaking (AEB)
class AEB(Node):
    def __init__(self):
        super().__init__('advance_breaking')
        self.ebrake_publisher_ = self.create_publisher(Twist, "cmd_vel", 10)
        self.velocity_subscriber_ = self.create_subscription(Twist, "cmd_vel", self.velocity_callback, 10)
        self.laserSensor_subscriber_ = self.create_subscription(Range, "laser/range", self.laser_callback, 10)
        self.get_logger().info('Advance E-breaking module active')
        self.threshold = 0
    
    def laser_callback(self, msg: Range):
        '''
        laser_callback function to measure the distance to the closest object
        '''
        if (msg.range <= self.threshold):
            # Both linear and angular velocity attributes are set to 0 in a message
            message = Twist(linear = Vector3(x=0.0, y=0.0, z=0.0),
                            angular = Vector3(x=0.0, y=0.0, z=0.0)
                            )
            # The above message is published by the ebrake_publisher_ publisher
            self.ebrake_publisher_.publish(message)
            self.get_logger().info("Object detected, applying Emergency break")
        
        else:
            self.get_logger().info("Distance to the nearest object is: {}".format(msg.range))

    def velocity_callback(self, msg:Twist):
        '''
        velocity_callback function to find the stopping distance based on the linear velocity in the x axis
        '''
        self.threshold = ((msg.linear.x ** 2) / 20) + 5
        self.get_logger().info('Stopping distance: {}'.format(self.threshold))
    
def main(args=None):
    rclpy.init(args=args)
    AEB_module =  AEB()
    rclpy.spin(AEB_module)
    AEB_module.destroy_node()
    rclpy.shutdown()

if __name__ == "main":
    main()