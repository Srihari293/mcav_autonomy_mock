from setuptools import setup

package_name = 'ros2_tutorial'

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
    maintainer_email='srihari2002@gmail.com',
    description='Control node',
    license='License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'control_node = ros2_tutorial.control_node:main',
        ],
    },
)