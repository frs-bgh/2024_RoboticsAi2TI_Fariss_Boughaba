import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class ObstacleStop(Node):
    def __init__(self):
        super().__init__('obstacle_stop')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscriber_ = self.create_subscription(LaserScan, '/scan', self.laser_callback, 10)
        self.cmd = Twist()
        self.obstacle_distance = 0.5  # Stopafstand in meters

    def laser_callback(self, msg):
        if min(msg.ranges) < self.obstacle_distance:
            self.get_logger().info('Obstacle detected! Stopping the robot.')
            self.cmd.linear.x = 0.0
        else:
            self.cmd.linear.x = 0.2  # Beweeg vooruit
        self.cmd.angular.z = 0.0
        self.publisher_.publish(self.cmd)


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleStop()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

