from setuptools import find_packages, setup

package_name = 'lidar_mediapipe_fariss'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/launch', ['launch/lafafa.launch.py']),  # Zorg ervoor dat het juiste bestand hier staat
],

    install_requires=['setuptools', 'rclpy', 'std_msgs', 'sensor_msgs', 'launch'],
    zip_safe=True,
    maintainer='fariss_bgh',
    maintainer_email='fariss_bgh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'camera_detection = lidar_mediapipe_fariss.camera_detection:main',
        'obstacle_avoidance = lidar_mediapipe_fariss.obstacle_avoidance:main',  # Oud pad
    ],
}
,
)
