#vim: filetype=bash

function fix_ros2_autocomplete() {
    ros2_check="/opt/ros/$ROS_DISTRO/bin/ros2"
    if [[ -e "$ros2_check" ]]; then
        eval "$(register-python-argcomplete3 ros2)"
        eval "$(register-python-argcomplete3 colcon)"
        eval "$(register-python-argcomplete3 colcon_cd)"
    fi
}

function lsource (){
    local_source_file="install/setup.zsh"
    if [[ -e "$local_source_file" ]]; then
        source $local_source_file
        fix_ros2_autocomplete
    fi
}
