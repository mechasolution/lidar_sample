import os
from glob import glob

from setuptools import find_packages, setup

package_name = "lidar_sample"

setup(
    name=package_name,
    version="1.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (
            os.path.join("share", package_name, "launch"),
            glob(os.path.join("launch", "*launch.py")),
        ),
        (
            os.path.join("share", package_name, "sample"),
            glob(os.path.join("sample", "*")),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Mechasolution",
    maintainer_email="techms5499@gmail.com",
    description="ROS 2 Package to play LiDAR sample",
    license="Apache 2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [],
    },
)
