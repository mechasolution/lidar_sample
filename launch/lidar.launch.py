import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    sample_file = os.path.join(get_package_share_directory("lidar_sample"), "sample")

    lidar_sample = ExecuteProcess(
        cmd=["ros2 bag play ", sample_file, " --loop"], shell=True
    )

    tf2_node = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="static_tf_pub_laser",
        arguments=["0", "0", "0.02", "0", "0", "0", "1", "base_link", "laser_frame"],
    )

    return LaunchDescription([lidar_sample, tf2_node])
