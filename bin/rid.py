#!/usr/bin/env python3
# vim: filetype=python

import argparse
from pathlib import Path
import os

# TODO: Add argcomplete - This needs to be pip installed so we need to handle this shomehow

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
    

