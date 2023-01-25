from setuptools import setup

package_name = 'srihari_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='srihari',
    maintainer_email='ssrihari2002@gmail.com',
    description='This is the Emergency breaking system module created by Srihari',
    license="MCAV's intellectual property maybe? License 20.23",
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'control_node = srihari_package.control_node:main',
            'laser_sensor_node = srihari_package.laser_sensor_node:main',
            'advance_breaking_node = srihari_package.advance_breaking_node:main'
        ],
    },
)