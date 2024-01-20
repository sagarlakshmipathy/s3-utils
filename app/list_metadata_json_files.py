import argparse
import boto3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data import folders

# Parse command-line options
parser = argparse.ArgumentParser()
parser.add_argument("--bucket-name", required=True)
parser.add_argument("--prefix", required=True)
parser.add_argument("--folder-names", required=False, default='tpcds')
args = parser.parse_args()

# Check if required options are provided
if not args.bucket_name or not args.prefix:
    print("Usage: python delete_metadata_folders.py --bucket-name <bucket_name> --prefix <base_path> [--folder-names <comma_separated_folder_names>]")
    exit(1)

# Define folders
if args.folder_names == 'tpcds':
    folders = folders.TPCDS_FOLDER_NAMES
else:
    folders = args.folder_names.split(',')

# Create a session using your AWS credentials
s3 = boto3.client('s3')

# Print json file names in each folder
for folder in folders:
    response = s3.list_objects_v2(Bucket=args.bucket_name, Prefix=f"{args.prefix}/{folder}/metadata/")
    try:
        contents = response['Contents']
        for obj in contents:
            if obj['Key'].endswith('.json'):
                print(f"{folder.ljust(25)} : {os.path.basename(obj['Key'])}")
    except KeyError:
        print(f"No json files in {folder} or the folder does not exist.")
