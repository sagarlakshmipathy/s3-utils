import argparse
import os
import sys
import boto3

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
    print("Usage: python find_num_parquets.py --bucket-name <bucket_name> --prefix <base_path> [--folder-names <comma_separated_folder_names>]")
    exit(1)

# Define folders
if args.folder_names == 'tpcds':
    folders = folders.TPCDS_FOLDER_NAMES
else:
    folders = args.folder_names.split(',')

# Create a session using your AWS credentials
s3 = boto3.client('s3')

# remove trailing slash from prefix if provided
if args.prefix[-1] == '/':
    args.prefix = args.prefix[:-1]

# Count .parquet files in each folder and align the numbers
for folder in folders:
    response = s3.list_objects_v2(Bucket=args.bucket_name, Prefix=f"{args.prefix}/{folder}/")
    try:
        contents = response['Contents']
        count = sum(1 for obj in contents if obj['Key'].endswith('.parquet'))
        print(f"Number of .parquet files in {folder.ljust(25)}: {count:8}")
    except KeyError:
        print(f"No .parquet files in {args.prefix}/{folder} or the folder does not exist.")
        continue

