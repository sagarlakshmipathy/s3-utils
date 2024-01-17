#!/bin/bash

# Parse command-line options
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --bucket-name)
            bucket="$2"
            shift 2
            ;;
        --prefix)
            base_path="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Check if required options are provided
if [ -z "$bucket" ] || [ -z "$base_path" ]; then
    echo "Usage: $0 --bucket-name <bucket_name> --prefix <base_path>"
    exit 1
fi

# Define folders
folders=("call_center" "catalog_page" "catalog_returns" "catalog_sales" "customer_address" "customer_demographics" "customer" "date_dim" "household_demographics" "income_band" "inventory" "item" "promotion" "reason" "ship_mode" "store_returns" "store_sales" "store" "time_dim" "warehouse" "web_page" "web_returns" "web_sales" "web_site")

# Define subfolders to delete
subfolders_to_delete=("metadata" "_delta_log")

# Delete specified subfolders inside each folder
for folder in "${folders[@]}"; do
    for subfolder in "${subfolders_to_delete[@]}"; do
        aws s3 rm "s3://${bucket}/${base_path}/${folder}/${subfolder}/" --recursive
        echo "Deleted ${subfolder} folder inside ${folder}."
    done
done