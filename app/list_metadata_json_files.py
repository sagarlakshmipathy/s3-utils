import logging
import os
import sys
import boto3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.common import base_parse_args, get_folders

# set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


def parse_args_list_metadata_json_files():
    required_args = ["--bucket-name", "--prefix"]
    optional_args = ["--folder-names"]
    return base_parse_args(required_args, optional_args)


def list_json_files(s3, args, folders):
    for folder in folders:
        response = s3.list_objects_v2(Bucket=args.bucket_name, Prefix=f"{args.prefix}/{folder}/metadata/")
        try:
            contents = response["Contents"]
            for obj in contents:
                if obj["Key"].endswith(".json"):
                    logging.info(f"{folder.ljust(25)} : {os.path.basename(obj['Key'])}")
        except KeyError:
            logging.error(f"No json files in {args.prefix}/{folder} or the folder does not exist.", exc_info=True)


def main():
    args = parse_args_list_metadata_json_files()
    folders = get_folders(args)
    s3 = boto3.client("s3")
    if args.prefix[-1] == "/":
        args.prefix = args.prefix[:-1]
    list_json_files(s3, args, folders)


if __name__ == "__main__":
    main()
