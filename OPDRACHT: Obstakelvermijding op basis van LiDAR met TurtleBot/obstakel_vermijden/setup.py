from setuptools import setup
from setuptools import find_packages

package_name = 'obstakel_vermijden'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jouw_naam',
    maintainer_email='jouw_email@example.com',
    description='Een simpele ROS2 package voor obstakelvermijding',
    license='MIT',
    entry_points={
        'console_scripts': [
            'obstakel_vermijden = obstakel_vermijden.obstakel_vermijden:main'
        ],
    },
)

