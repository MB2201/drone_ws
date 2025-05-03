cmake_minimum_required(VERSION 3.8)
project(my_drone)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(ros_gz_sim REQUIRED)
find_package(ros_gz_bridge REQUIRED)
find_package(sensor_msgs REQUIRED)

# Install launch and model files
install(
  DIRECTORY launch models
  DESTINATION share/${PROJECT_NAME}
)

ament_package()