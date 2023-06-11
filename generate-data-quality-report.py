from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
from tabulate import tabulate

import mytests

from dataqualitychecks import check_for_nulls
from dataqualitychecks import check_for_min_max
from dataqualitychecks import check_for_valid_values
from dataqualitychecks import run_data_quality_check

load_dotenv()

# connect to database
pguser = os.environ.get('POSTGRES_USER')
pgpassword = os.environ.get('POSTGRES_PASSWORD')
pgdatabase = os.environ.get('POSTGRES_DATABASE')
conn = psycopg2.connect(
	user = pguser,
	password = pgpassword,
	host = "localhost",
	port = "5432",
	database = pgdatabase
)

print("Connected to Data Warehouse")


# start of data quuality checks
results = []
tests = {key : value for key, value in mytests.__dict__.items() if key.startswith('test')}
for testname, test in tests.items():
	test['conn'] = conn
	results.append(run_data_quality_check(**test))

# print(results)
df = pd.DataFrame(results)
df.index += 1
df.columns = ['Test Name', 'Table', 'Column', 'Test Passed']
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
# End of data quality checks
print("Disconnected from data warehouse")
