
SCRIPT_PATH=$(realpath "$0")
PROJECT_ROOT=$(dirname "$(dirname "$SCRIPT_PATH")")
VERSION_FILE=$PROJECT_ROOT/.ros-version


function set_container_name(){
    if [ -z $ROS_DOCKER_DISTRO ]; then

        if [ -f $VERSION_FILE ]; then
            ROS_DOCKER_DISTRO=$(cat ${PROJECT_ROOT}/.ros-version)
        else
            echo "Error: ROS_DOCKER_DISTRO is not set. Please set it and try again.";
            exit 1;
        fi 
    fi
    DOCKER_CONTAINER_NAME="ros-$(cat ${PROJECT_ROOT}/.ros-version)-container"
}
