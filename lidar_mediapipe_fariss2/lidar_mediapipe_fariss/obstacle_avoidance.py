import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.qos import ReliabilityPolicy, QoSProfile

class ObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance')
        
        # Publisher for movement commands
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # Subscriber for LIDAR data
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.laser_callback,
            QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)
        )
        
        # Subscriber for hand gesture commands
        self.gesture_subscription = self.create_subscription(
            Twist,
            '/hand_gesture_cmd',
            self.gesture_callback,
            10
        )
        
        self.cmd = Twist()
        self.timer = self.create_timer(0.1, self.move_robot)
        self.laser_forward = float('inf')
        self.laser_left = float('inf')
        self.laser_right = float('inf')
        self.safety_distance = 0.5
        self.turning = False
        self.current_speed = 0.0  # Initialize current speed

    def laser_callback(self, msg):
        # Get the forward distance
        self.laser_forward = msg.ranges[0]  # Assuming the first range is forward
        
        # Get left and right distances
        self.laser_left = min([r for r in msg.ranges[0:45] if r != float('inf')], default=float('inf'))
        self.laser_right = min([r for r in msg.ranges[-45:] if r != float('inf')], default=float('inf'))

    def gesture_callback(self, msg):
        # Update current speed based on gesture command
        self.current_speed = msg.linear.x

    def avoid_obstacles(self):
        if self.laser_forward < self.safety_distance:
            self.turning = True
            self.cmd.linear.x = 0.0  # Stop moving forward
            # Choose turn direction based on side distances
            if self.laser_left > self.laser_right:
                self.cmd.angular.z = 0.5  # Turn left
            else:
                self.cmd.angular.z = -0.5  # Turn right
            return True
        elif self.turning:
            # Keep turning until we have a clear path
            if self.laser_forward > self.safety_distance * 1.5:
                self.turning = False
            return True
        return False

    def move_robot(self):
        if not self.avoid_obstacles():
            # Move forward with speed from gesture command
            self.cmd.linear.x = self.current_speed
            self.cmd.angular.z = 0.0
        else:
            # Stop if avoiding obstacles
            self.cmd.linear.x = 0.0

        # Publish the movement command
        self.publisher_.publish(self.cmd)

def main(args=None):
    rclpy.init(args=args)
    obstacle_avoidance = ObstacleAvoidance()
    
    try:
        rclpy.spin(obstacle_avoidance)
    except KeyboardInterrupt:
        pass
    finally:
        obstacle_avoidance.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


