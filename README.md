# s3-utils

This repo is a collection of utilities for working with S3.

## Pre-requisites
Install required packages:
- `pip install -r requirements.txt`

## fin_num_parquets.py 
This script will find the number of parquet files in a directory. This is especially geared towards using TPCDS datasets.

### Usage:
```shell
python3 find-num-parquets.py --bucket-name <bucket-name> --prefix <prefix> [--folder-names <comma_separated_folder_names>]
```

### Example:
```shell
python3 find-num-parquets.py --bucket-name my-bucket-name --prefix path/to/tables-directory
```

will count the number of parquet files in

```shell
s3://my-bucket-name/path/to/tables-directory/call_center/
s3://my-bucket-name/path/to/tables-directory/catalog_page/
s3://my-bucket-name/path/to/tables-directory/catalog_returns/
...
```

and print the result to stdout like below:
```
Number of .parquet files in call_center              :        1
Number of .parquet files in catalog_page             :        1
Number of .parquet files in catalog_returns          :     2104
Number of .parquet files in catalog_sales            :     1836
Number of .parquet files in customer_address         :       20
Number of .parquet files in customer_demographics    :        1
Number of .parquet files in customer                 :       40
Number of .parquet files in date_dim                 :        1
Number of .parquet files in household_demographics   :        1
Number of .parquet files in income_band              :        1
Number of .parquet files in inventory                :      261
Number of .parquet files in item                     :        2
Number of .parquet files in promotion                :        1
Number of .parquet files in reason                   :        1
Number of .parquet files in ship_mode                :        1
Number of .parquet files in store_returns            :     2003
Number of .parquet files in store_sales              :     1826
Number of .parquet files in store                    :        1
Number of .parquet files in time_dim                 :        1
Number of .parquet files in warehouse                :        1
Number of .parquet files in web_page                 :        1
Number of .parquet files in web_returns              :     2184
Number of .parquet files in web_sales                :     1823
Number of .parquet files in web_site                 :        1
```

## delete_metadata_folders.py
This script will delete the `.hoodie/`, `metadata/` and `_delta_log` folders in a directory. This is especially geared towards using TPCDS datasets.

### Usage:
```shell
python3 delete_metadata_folders.py --bucket-name <bucket-name> --prefix <prefix> [--folder-names <comma_separated_folder_names>] --table-format-names <comma_separated_table_format_names>
```

### Example:
```shell
python3 delete_metadata_folders.py --bucket-name my-bucket-name --prefix path/to/tables-directory --table-format-names iceberg,delta
```

will delete the `metadata/`, `_delta_log` folders in

```shell
s3://my-bucket-name/path/to/tables-directory/call_center/
s3://my-bucket-name/path/to/tables-directory/catalog_page/
s3://my-bucket-name/path/to/tables-directory/catalog_returns/
...
```

## list_metadata_json_files.py
This script will list the names of the metadata json files in a directory. This is especially geared towards using TPCDS datasets.

### Usage:
```shell
python3 list_metadata_json_files.py --bucket-name <bucket-name> --prefix <prefix> [--folder-names <comma_separated_folder_names>]
```

### Example:
```shell
python3 list_metadata_json_files.py --bucket-name my-bucket-name --prefix path/to/tables-directory
```

will list the names of the metadata json files in

```shell
s3://my-bucket-name/path/to/tables-directory/call_center/
s3://my-bucket-name/path/to/tables-directory/catalog_page/
s3://my-bucket-name/path/to/tables-directory/catalog_returns/
...
```

and print the result to stdout like below:
```
call_center               : v1705521231728000000.metadata.json
catalog_page              : v1705521233209000000.metadata.json
catalog_returns           : v1705521234945000000.metadata.json
catalog_sales             : v1705521248373000000.metadata.json
customer                  : v1705521349291000000.metadata.json
customer_address          : v1705521356285000000.metadata.json
customer_demographics     : v1705521362710000000.metadata.json
date_dim                  : v1705521369541000000.metadata.json
household_demographics    : v1705521371661000000.metadata.json
income_band               : v1705521373269000000.metadata.json
inventory                 : v1705521374770000000.metadata.json
item                      : v1705521386968000000.metadata.json
promotion                 : v1705521392043000000.metadata.json
reason                    : v1705521393886000000.metadata.json
ship_mode                 : v1705521395325000000.metadata.json
store                     : v1705521396878000000.metadata.json
store_returns             : v1705521398509000000.metadata.json
store_sales               : v1705521414320000000.metadata.json
time_dim                  : v1705521545548000000.metadata.json
warehouse                 : v1705521547403000000.metadata.json
web_page                  : v1705521548976000000.metadata.json
web_returns               : v1705521550774000000.metadata.json
web_sales                 : v1705521561415000000.metadata.json
web_site                  : v1705521612385000000.metadata.json
```
