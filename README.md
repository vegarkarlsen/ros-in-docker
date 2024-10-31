# Ros-In-Docker (RID)

This project aims to provide a simple interface for running different ros- and
ros2 distros in docker with gui support. 

## Prerequisites

- docker - Make sure your have a docker install with docker-compose

## Install

```bash
git clone https://github.com/vegarkarlsen/ros-in-docker.git
cd ros-in-docker
make install
```

This will install to /usr/local. If you want to install to another location
you can use `make install PREFIX=/path/to/install`.

### Running the container

To start the container run:

```bash
rid --start --distro DISTRO
```

Where DISTRO is the desired ros-distro to start.

To attach a new shell to the container:

```bash
rid --attach
```
