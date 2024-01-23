import logging
import os
import sys
import boto3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.utils.common import get_folders
from list_metadata_json_files import parse_args_list_metadata_json_files

# set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


# get the json files
def get_json_files(client, bucket_name, prefix, folders):
    json_files = []
    for folder in folders:
        response = client.list_objects_v2(Bucket=bucket_name, Prefix=f"{prefix}/{folder}/metadata/")
        try:
            contents = response["Contents"]
            for obj in contents:
                if obj["Key"].endswith(".json"):
                    logging.info(f"{folder.ljust(25)} : {os.path.basename(obj['Key'])}")
                if obj["Key"].endswith("version-hint.text"):
                    # json_files.append(os.path.basename(obj["Key"]))
                    # check if version-hint.text file is present,
                    # if yes, then open and grab the last line which is the version number
                    # append v{number}.metadata.json to the json_files list
                    # if no, throw error
                    response = client.get_object(Bucket=bucket_name, Key=f"{prefix}/{folder}/metadata/version-hint.text")
                    version_hint_content = response["Body"].read().decode("utf-8")
                    version = version_hint_content.split("\n")[-1]
                    json_files.append(f"v{version}.metadata.json")
        except KeyError:
            logging.error(f"No json files in {prefix}/{folder} or the folder does not exist.", exc_info=True)
    return json_files


def get_next_version(json_file):
    # check if current json file is timestamp based
    # if yes, name the file as v2.metadata.json
    # if not, add +1 to the file name
    # return the new file name

    # strip v and .json from the file name
    stripped_json_file_name = json_file.split(".")[0][1:]
    # check if the file name is timestamp based
    if int(len(stripped_json_file_name)) == 19:
        return 2
    else:
        return int(stripped_json_file_name) + 1


# create a copy of the json file in place and rename it to v2.metadata.json
def copy_update_json_files(client, bucket_name, prefix, folders, json_files):
    for index, folder in enumerate(folders):
        # copy the file and rename it in place to v2.metadata.json
        copy_source = f"{bucket_name}/{prefix}/{folder}/metadata/{json_files[index]}"
        next_file_version = get_next_version(json_files[index])
        future_file_name = f"v{next_file_version}.metadata.json"
        client.copy_object(
            Bucket=bucket_name,
            CopySource=copy_source,
            Key=f"{prefix}/{folder}/metadata/{future_file_name}")
        logging.info(f"Copied {json_files[index]} to {future_file_name}")
        version_hint_content = client.get_object(
            Bucket=bucket_name,
            Key=f"{prefix}/{folder}/metadata/version-hint.text"
        )["Body"].read().decode("utf-8")
        # add the new file name to the version-hint.text file
        version_hint_content += f"\n{next_file_version}"
        client.put_object(
            Body=version_hint_content,
            Bucket=bucket_name,
            Key=f"{prefix}/{folder}/metadata/version-hint.text"
        )
        logging.info(f"Updated version-hint.text file with {next_file_version}")


def main():
    args = parse_args_list_metadata_json_files()
    folders = get_folders(args)
    s3_client = boto3.client("s3")
    if args.prefix[-1] == "/":
        args.prefix = args.prefix[:-1]
    json_files = get_json_files(s3_client, args.bucket_name, args.prefix, folders)
    copy_update_json_files(s3_client, args.bucket_name, args.prefix, folders, json_files)


if __name__ == "__main__":
    main()
