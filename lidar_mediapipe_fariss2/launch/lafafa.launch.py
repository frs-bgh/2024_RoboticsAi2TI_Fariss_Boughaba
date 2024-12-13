from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lidar_mediapipe_fariss',
            executable='camera_detection',
            output='screen'),
        Node(
    package='lidar_mediapipe_fariss',
    executable='obstacle_avoidance',  # Oude naam
    output='screen',
),


    ])
