import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Define the name of the URDF file and the package
    urdf_file_name = 'robot.urdf'
    package_name = "diff_bot"

    # Get the path to the URDF file
    urdf_file_path = os.path.join(get_package_share_directory(package_name), "urdf", urdf_file_name)

    # Read the URDF file content
    with open(urdf_file_path, 'r') as urdf_file:
        urdf_content = urdf_file.read()

    # Create the Robot State Publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': True, 'robot_description': urdf_content}]
    )

    # Create and return the LaunchDescription object
    return LaunchDescription([robot_state_publisher_node])

