from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Get path to your SDF file
    sdf_path = os.path.join(
        get_package_share_directory('my_drone'),
        'models',
        'my_drone',
        'model.sdf'
    )
    
    # Launch Gazebo with your world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('ros_gz_sim'), 
            'launch', 'gz_sim.launch.py')
        ]),
        launch_arguments={
            'gz_args': ['-r ', sdf_path]
        }.items()
    )
    
    # Bridge for LIDAR data
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='bridge',
        arguments=['/lidar@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan'],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        bridge
    ])