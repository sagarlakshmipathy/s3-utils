import argparse
import boto3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data import folders, table_formats

# Parse command-line options
parser = argparse.ArgumentParser()
parser.add_argument("--bucket-name", required=True)
parser.add_argument("--prefix", required=True)
parser.add_argument("--folder-names", required=False, default='tpcds')
parser.add_argument("--table-format-names", required=True)
args = parser.parse_args()

# Check if required options are provided
if not args.bucket_name or not args.prefix:
    print("Usage: python delete_metadata_folders.py --bucket-name <bucket_name> --prefix <base_path> [--folder-names <comma_separated_folder_names>] --table-format-names <comma_separated_table_format_names>")
    exit(1)

# Define folders
if args.folder_names == 'tpcds':
    folders = folders.TPCDS_FOLDER_NAMES
else:
    folders = args.folder_names.split(',')

# Define subfolders to delete
table_format_names = args.table_format_names.split(',')

metadata_folders_to_delete = []
for table_format in table_format_names:
    metadata_folders_to_delete.append(table_formats.METADATA_FOLDER_NAMES[table_format])

# Create a session using your AWS credentials
s3 = boto3.resource('s3')

# Delete specified subfolders inside each folder
for folder in folders:
    for metadata_folder_name in metadata_folders_to_delete:
        bucket = s3.Bucket(args.bucket_name)
        # try finding the metadata folder
        try:
            bucket.Object(f"{args.prefix}/{folder}/{metadata_folder_name}/").load()
            for obj in bucket.objects.filter(Prefix=f"{args.prefix}/{folder}/{metadata_folder_name}/"):
                s3.Object(bucket.name, obj.key).delete()
            print(f"Deleted {metadata_folder_name} folder inside {args.prefix}/{folder}")
        except:
            print(f"{metadata_folder_name} folder not found inside {args.prefix}/{folder}")
            continue

