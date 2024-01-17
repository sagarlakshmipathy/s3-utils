#!/bin/bash

bucket="s3-calls-log-bucket"
base_path="benchmarks/1TB/hudi-onetable"

folders=("call_center" "catalog_page" "catalog_returns" "catalog_sales" "customer_address" "customer_demographics" "customer" "date_dim" "household_demographics" "income_band" "inventory" "item" "promotion" "reason" "ship_mode" "store_returns" "store_sales" "store" "time_dim" "warehouse" "web_page" "web_returns" "web_sales" "web_site")

for folder in "${folders[@]}"; do
    count=$(aws s3 ls "s3://${bucket}/${base_path}/${folder}/" --recursive | grep ".parquet$" | wc -l)
    echo "Number of .parquet files in ${folder}: ${count}"
done
