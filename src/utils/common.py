import logging
import os
import sys
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.data import folders

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def base_parse_args(required_args, optional_args):
    # base parser for all scripts
    parser = argparse.ArgumentParser()
    for arg in required_args:
        parser.add_argument(arg, required=True)
    for arg in optional_args:
        parser.add_argument(arg, required=False)
    try:
        args = parser.parse_args()
        if not args.bucket_name or not args.prefix:
            raise argparse.ArgumentError(None, "Both --bucket-name and --prefix arguments are required.")
    except (SystemExit, argparse.ArgumentError) as e:
        logging.error(e, exc_info=True)
        logging.info(f"""
        Usage: python {os.path.basename(__file__)}
        --bucket-name <bucket_name>
        --prefix <base_path>
        [--folder-names <comma_separated_folder_names>]""")
        raise SystemExit
    return args


def get_folders(args):
    # Return the appropriate folder names based on the provided arguments
    # tpcds is default
    if args.folder_names == "tpcds" or args.folder_names is None:
        return folders.TPCDS_FOLDER_NAMES
    else:
        return args.folder_names.split(",")
