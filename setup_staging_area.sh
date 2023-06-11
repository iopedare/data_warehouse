#!/bin/bash

echo "Creating the database"
createdb -h localhost -U postgres -p 5432 billingDW1

echo "Downloading the data files"
wget https://github.com/iopedare/data_warehouse/raw/main/billing-datawarehouse.tgz

echo "Extracting files"
tar -xvzf billing-datawarehouse.tgz

echo "Creating Star Schema"
psql -h localhost -U postgres -p 5432 billingDW1 < star-schema.sql

echo "Loading data"
psql -h localhost -U postgres -p 5432 billingDW1 < DimCustomer.sql
psql -h localhost -U postgres -p 5432 billingDW1 < DimMonth.sql
psql -h localhost -U postgres -p 5432 billingDW1 < FactBilling.sql

echo "Finished loading data"

echo "Verifying data"
psql -h localhost -U postgres -p 5432 billingDW1 < verify.sql

echo "Successfully setup the staging area"
