# Verify Data Quaity

### Clone the repo

### Set Up
1. create a virtual environment
```
$ python -m venv venv
```
2. activate the virtual environment
```
$ source venv/bin/activate
```
3. Install the requirements.txt
```
$ pip install -r requirements.txt
```

### Create the database on the data warehouse
```
$ chmod +x setup_staging_area.sh
$ ./setup_staging_area.sh
```

### create a new file ".env" and type in the following:
POSTGRES_USER=[Enter your user here]
POSTGRES_PASSWORD=[Enter your password here]
POSTGRES_DATABASE=[Enter your database here]

### Run the Python script
1. ```$ python dbconnect.py```
2. ```$ python generate-data-quality-report.py```
