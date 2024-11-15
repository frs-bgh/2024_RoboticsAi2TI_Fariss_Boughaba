import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class ObstakelVermijden(Node):#Klassenaam
    def __init__(self):
        super().__init__('obstakel_vermijden')
        self.publiceer = self.create_publisher(Twist, '/cmd_vel', 10)
        self.abonneer = self.create_subscription(LaserScan, '/scan', self.laser_callback, 10)
        self.twist = Twist()

    def laser_callback(self, msg):#Functienaam
        # Lees de afstanden voor en aan de zijkanten van de robot
        # Variabelen creëren "voor, links, rechts"
        voor = min(min(msg.ranges[0:10]), min(msg.ranges[-10:])) #Variabelen
        links = min(msg.ranges[60:120]) #Variabelen
        rechts = min(msg.ranges[240:300]) #Variabelen

        # Drempelwaarde voor obstakels (0.5 meter)
        if voor < 0.5:
            # Als er iets voor de robot is, draai dan weg
            if links > rechts:
                self.draai_links()
            else:
                self.draai_rechts()
        elif links < 0.5:
            # Als er iets links is, draai dan rechts
            self.draai_rechts()
        elif rechts < 0.5:
            # Als er iets rechts is, draai dan links
            self.draai_links()
        else:
            # Anders blijf vooruit bewegen
            self.vooruit()

        # Publiceer de snelheid van de robot
        self.publiceer.publish(self.twist)

    def draai_links(self):#Functienaam
        self.twist.linear.x = 0.0  # Stop met vooruit bewegen
        self.twist.angular.z = 0.5  # Draai naar links

    def draai_rechts(self):#Functienaam
        self.twist.linear.x = 0.0  # Stop met vooruit bewegen
        self.twist.angular.z = -0.5  # Draai naar rechts

    def vooruit(self):#Functienaam
        self.twist.linear.x = 0.2  # Beweeg vooruit
        self.twist.angular.z = 0.0  # niet draaien 

def main(args=None):
    rclpy.init(args=args)
    node = ObstakelVermijden()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
