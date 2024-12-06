from setuptools import setup

package_name = 'obstacle_stop'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fariss',
    maintainer_email='your_email@example.com',
    description='A package to stop the robot when an obstacle is detected.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'obstacle_stop = obstacle_stop.obstacle_stop:main',
        ],
    },
)

