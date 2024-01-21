import os
import sys
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import folders


def base_parse_args(required_args, optional_args):
    parser = argparse.ArgumentParser()
    for arg in required_args:
        parser.add_argument(arg, required=True)
    for arg in optional_args:
        parser.add_argument(arg, required=False)
    try:
        args = parser.parse_args()
    except SystemExit:
        args = None
    return args


def get_folders(args):
    if args.folder_names == "tpcds" or args.folder_names is None:
        return folders.TPCDS_FOLDER_NAMES
    else:
        return args.folder_names.split(",")
