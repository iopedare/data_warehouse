#!/bin/bash

echo "Creating the database"
createdb -h localhost -U postgres -p 5432 billingDW

echo "Downloading the data files"
wget https://github.com/iopedare/data_warehouse/raw/main/billing-datawarehouse.tgz

echo "Extracting files"
tar -xvzf billing-datawarehouse.tgz

echo "Creating Star Schema"
psql -h localhost -U postgres -p 5432 billingDW < star-schema.sql

echo "Loading data"
psql -h localhost -U postgres -p 5432 billingDW < DimCustomer.sql
psql -h localhost -U postgres -p 5432 billingDW < DimMonth.sql
psql -h localhost -U postgres -p 5432 billingDW < FactBilling.sql

echo "Finished loading data"

echo "Verifying data"
psql -h localhost -U postgres -p 5432 billingDW < verify.sql

echo "Successfully setup the staging area"
