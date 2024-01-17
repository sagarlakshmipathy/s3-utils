# s3-utils

This repo is a collection of utilities for working with S3.

## find-num-parquet-files.sh 
This script will find the number of parquet files in a directory. This is especially geared towards using TPCDS datasets.

### Usage:
```shell
./find-num-parquet-files.sh --bucket-name <bucket-name> --prefix <prefix>
```

### Example:
```shell
./find-num-parquet-files.sh --bucket-name my-bucket-name --prefix path/to/tables-directory
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