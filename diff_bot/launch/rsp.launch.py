import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # Define the URDF and package name
    urdf_file_name = 'robot.urdf.xacro'
    package_name = "diff_bot"

    # Fetch the URDF file path
    robot_desc_path = os.path.join(get_package_share_directory(package_name), "urdf", urdf_file_name)
    
    # Process the xacro file
    xacro_file = xacro.process_file(robot_desc_path)
    
    # Robot State Publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher_node',
        parameters=[{'use_sim_time': True, 'robot_description': xacro_file.toxml()}],
        output="screen"
    )
    
    # Joint State Publisher
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher_node',
        output="screen"
    )

    # Create and return launch description object
    return LaunchDescription(
        [            
            robot_state_publisher_node,
            joint_state_publisher_node,
        ]
    )
