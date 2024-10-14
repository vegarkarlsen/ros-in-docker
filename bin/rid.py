#!/usr/bin/env python3
# vim: filetype=python

import argparse
from pathlib import Path
import subprocess
import os

# TODO: Add argcomplete - This needs to be pip installed so we need to handle this shomehow

BIN_DIR = Path(__file__).resolve().parent
VERSION = "v1.0.0"

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

    if args.start:
        run_subbprocess(BIN_DIR / "start_ros", env=env)
        return

    elif args.attach:
        run_subbprocess(BIN_DIR / "attach_ros", env=env)
        return

    elif args.version:
        print(VERSION)
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v", "--version",
        help="Get current version of RID.",
        action="store_true"
    )
    parser.add_argument(
        "-s", "--start",
        help="Starts the ros container. Defualt distro is noetic.",
        action="store_true"
    )
    parser.add_argument(
        "-a", "--attach",
        help="Attaches a shell to the ros container.",
        action="store_true"
    )
    parser.add_argument(
        "-d" ,"--distro",
        type=str,
        help="Which ros distro to to choose. (default=noetic)",
        required=False
    )

    args = parser.parse_args()
    main(args)

