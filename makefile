
IMAGE_FOLDER = ros-images
DOCKERFILE_TEMPLATE = $(IMAGE_FOLDER)/Dockerfile.template
DOCKERFILE_OUTPUT = $(IMAGE_FOLDER)/$(ROS_DOCKER_DISTRO)/Dockerfile

generate-dockerfile:
	@if [ -z $(ROS_DOCKER_DISTRO) ]; then \
		echo "Error: ROS_DOCKER_DISTRO is not set."; Please set it and try again.\
		exit 1; \
	fi
	@if [ ! -d "$(IMAGE_FOLDER)/$(ROS_DOCKER_DISTRO)" ]; then \
		mkdir -p $(IMAGE_FOLDER)/$(ROS_DOCKER_DISTRO); \
	fi
	@sed -e 's/{{ROS_VERSION}}/$(ROS_DOCKER_DISTRO)/g' $(DOCKERFILE_TEMPLATE) > $(DOCKERFILE_OUTPUT)
	@echo "Generated a ros-$(ROS_DOCKER_DISTRO) dockerfile in $(DOCKERFILE_OUTPUT)"

PREFIX ?= /usr/local
TARGET_DIR = $(PREFIX)/bin

install:
	ln -s $(CURDIR)/bin/rid $(TARGET_DIR)/rid
