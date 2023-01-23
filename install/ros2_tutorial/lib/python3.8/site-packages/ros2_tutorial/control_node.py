import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Control(Node):

    def __init__(self):
        super().__init__('control')
        '''
        - Task 1: Create a publisher for /cmd_vel
        - Task 2: Create a timer_callback where you will publish velocity
        '''
        # Solutions
        # Task 1.
        # Declared a node named drive_publisher_ that publishes messages of type Twist, over a topic named cmd_vel and in a queue of size 10. 
        # Queue size is a required QoS (quality of service) setting that limits the amount of queued messages if a subscriber is not receiving them fast enough.
        self.drive_publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)     

        # Task 2. 
        timer_period = 0.5  # seconds
        self.drive_timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('I am publishing drive commands.')
        self.t = 0

    def timer_callback(self):
        '''
        - Task 3: Create empty Twist message
        - Task 4: Change linear velocity
        - Task 5: Publish message
        '''
        # Task 3.
        message = Twist()
        
        # Task 4: Moving straight
        message.linear.x = 1.0

        # Uncomment code below to execute task 6
        # # Task 6: Donuts
        # message.angular.z = 1.0

        # Task 5.
        self.drive_publisher_.publish(message)
        
        self.get_logger().info('Publishing drive command: %d' % self.t)
        self.get_logger().info('Linear Velocity: %d' % message.linear.x)
        self.get_logger().info('Angular Velocity: %d' % message.angular.z)
        self.t += 1
    
def main(args=None):
    rclpy.init(args=args)
    control = Control()
    rclpy.spin(control)
    control.destroy_node()
    rclpy.shutdown()

if __name__=="main":
    main()

# Useful links:
# 1. Creating a publisher node:  https://docs.ros.org/en/dashing/Tutorials/Writing-A-Simple-Py-Publisher-And-Subscriber.html#write-the-publisher-node

# Next step: 
# 1. Once you have written the control node, go to your root workspace (~/(your_ws)) and build the workspace with the command (colcon build)
# 2. You will see build, log and an install folder along side your src folder
# 3. Additionally, in your ros2_tutorial path (/home/(USER))/(your_ws)/src/ros2_tutorial), you will find package.xml, setup.py, setup.cfg files and 
#    resources and test folders.
# 4. These are files that get created when we build a python workspace