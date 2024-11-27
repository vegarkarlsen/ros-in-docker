
# Do nothing if $ROS_DISTRO is not set.
if [[ -z $ROS_DISTRO ]]; then
    return
fi

# Set Working Dir to home if not set
if [[ ! -z $ROS_DOCKER_HOME ]]; then
    ROS_DOCKER_WORKDIR="$HOME"
fi

# Soruce Ros-distro
source "/opt/ros/$ROS_DISTRO/setup.zsh"

# Fix TERM
export TERM=xterm-256color

# Set compiler to clang
export CC=clang
export CXX=clang++

# See: https://www.reddit.com/r/ROS/comments/15yr1zm/ros_c_coding_setup/
# export CLANG_BASE="--build-base build_clang --install-base install_clang"
# export BUILD_ARGS="--symlink-install ${CLANG_BASE} --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON"
# alias cb="colcon build ${BUILD_ARGS}"

# ROS2
alias cb="bear -- colcon build"
alias cbr="rm -r build install"

# ROS1
alias cm="bear catkin_make"
alias cmr="rm -r devel build"


# cd to Worcking directory
cd $ROS_DOCKER_WORKDIR
