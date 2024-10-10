#!/usr/bin/env python3
# vim: filetype=python

import argparse
from pathlib import Path
import subprocess
import os

# TODO: Add argcomplete - This needs to be pip installed so we need to handle this shomehow

BIN_DIR = Path(__file__).resolve().parent

def run_subbprocess(command, env):
    try:
        subprocess.run(command, env=env)
    except KeyboardInterrupt:
        pass

def main(args):
    env = os.environ.copy()

    env["ROS_DOCKER_DISTRO"] = "noetic"
    if args.distro:
        env["ROS_DOCKER_DISTRO"] = args.distro

    if args.option == "start":
        run_subbprocess(BIN_DIR / "start_ros", env=env)

    elif args.option == "attach":
        run_subbprocess(BIN_DIR / "attach_ros", env=env)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'option',
        help="",
        type=str,
        choices=['start','attach']
    )
    parser.add_argument(
        "-d" ,"--distro",
        type=str,
        help="Which ros distro to to choose. (default=noetic)",
        required=False
    )
    args = parser.parse_args()
    main(args)

