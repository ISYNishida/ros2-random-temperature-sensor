from setuptools import find_packages, setup

package_name = 'random_temperature_sensor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'temperature_publisher = random_temperature_sensor.temperature_publisher:main',
            'temperature_publisher_b = random_temperature_sensor.temperature_publisher_b:main',
            'temperature_subscriber = random_temperature_sensor.temperature_subscriber:main'
        ],
    },
)
