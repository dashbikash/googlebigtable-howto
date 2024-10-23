import datetime
import os
from google.cloud import bigtable
from google.cloud.bigtable import column_family
import csv

# Set the environment variable to connect to the Bigtable emulator
os.environ['BIGTABLE_EMULATOR_HOST'] = 'localhost:8086'  # Replace with your emulator host and port

# Initialize the Bigtable client
client = bigtable.Client(project="project-id", admin=True)
instance = client.instance('quickstart-instance')

# Define the table name
table = instance.table("my-table")

# Define the column families
column_families = {
    'cf1': column_family.MaxVersionsGCRule(2)
}

# Read CSV file and insert data into Bigtable
with open('/path/to/your/csvfile.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = []
    for row in reader:
        row_key = row['row_key']
        mutation = bigtable.RowMutation(row_key)
        for column, value in row.items():
            if column != 'row_key':
                mutation.set_cell('cf1', column, value, timestamp=datetime.datetime.utcnow())
        rows.append(mutation)

    table.mutate_rows(rows)


# Create the table
if not table.exists():
    table.create(column_families=column_families)
