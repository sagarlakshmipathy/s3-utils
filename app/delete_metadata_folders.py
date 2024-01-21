import os
import sys
import boto3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import table_formats
from utils.common import base_parse_args, get_folders


def parse_args_delete_metadata():
    required_args = ["--bucket-name", "--prefix", "--table-format-names"]
    optional_args = ["--folder-names"]
    args = base_parse_args(required_args, optional_args)

    try:
        if not args.bucket_name or not args.prefix or not args.table_format_names:
            raise AttributeError
    except AttributeError:
        print("""
        Usage: python delete_metadata_folders.py
        --bucket-name <bucket_name>
        --prefix <base_path>
        --table-format-names <comma_separated_table_format_names>
        [--folder-names <comma_separated_folder_names>]""")
        raise SystemExit

    return args


def get_metadata_folders_to_delete(args):
    table_format_names = args.table_format_names.split(",")
    return [table_formats.METADATA_FOLDER_NAMES[table_format] for table_format in table_format_names]


def delete_folders(s3, args, folders, metadata_folders_to_delete):
    for folder in folders:
        for metadata_folder_name in metadata_folders_to_delete:
            bucket = s3.Bucket(args.bucket_name)
            try:
                bucket.Object(f"{args.prefix}/{folder}/{metadata_folder_name}/").load()
                for obj in bucket.objects.filter(Prefix=f"{args.prefix}/{folder}/{metadata_folder_name}/"):
                    s3.Object(bucket.name, obj.key).delete()
                print(f"Deleted {metadata_folder_name} folder inside {args.prefix}/{folder}")
            except:
                print(f"{metadata_folder_name} folder not found inside {args.prefix}/{folder}")


def main():
    args = parse_args_delete_metadata()
    folders = get_folders(args)
    metadata_folders_to_delete = get_metadata_folders_to_delete(args)
    s3 = boto3.resource("s3")
    delete_folders(s3, args, folders, metadata_folders_to_delete)


if __name__ == "__main__":
    main()
