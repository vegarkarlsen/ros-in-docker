#!/usr/bin/env python3
# vim: filetype=python

import argparse
# import pathlib
from pathlib import Path
import os

BIN_DIR = Path(__file__).resolve().parent

def main(args):

    if args.option == "start":
        os.system(BIN_DIR / "start_ros")

    elif args.option == "attach":
        os.system(BIN_DIR / "attach_ros")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'option',
        help="",
        choices=['start','attach']
    )
    args = parser.parse_args()
    main(args)
    

