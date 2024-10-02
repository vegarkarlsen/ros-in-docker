# ROS noetic docker template

This project is a template for running a general ros noetic image in a docker container, with gui support. It is ment to be a quick template to easy set up a ros noetic environment for testing puposes.

### Prerequisites
 - todo

### Running the container

To run the container, make sure you are in the project root folder, and use the following command:
```bash
./ros-noetic
```

This will start the container, aswell as start a roscore.

To open a new terminal inside the container:

```bash
docker exec -it ros-noetic-container bash
```

