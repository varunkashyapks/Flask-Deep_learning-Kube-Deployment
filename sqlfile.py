import sqlite3
import csv

# Replace 'your_database_name.db' with your desired SQLite database name
database_name = 'your_database_name.db'
table_name = 'your_table_name'

# Replace 'your_csv_file.csv' with your actual CSV file name
csv_file = 'your_csv_file.csv'

# Connect to SQLite database (this will create the database file if it doesn't exist)
connection = sqlite3.connect(database_name)
cursor = connection.cursor()

# Read the CSV file and create a table in the database
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Assumes the first row contains column names

    # Generate CREATE TABLE statement
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col} TEXT' for col in header])});"
    
    # Create the table
    cursor.execute(create_table_sql)
    
    # Insert data into the table
    for row in csv_reader:
        insert_sql = f"INSERT INTO {table_name} VALUES ({', '.join(['?' for _ in row])});"
        cursor.execute(insert_sql, row)

# Commit the changes and close the connection
connection.commit()
connection.close()

print(f"Data from {csv_file} successfully imported into the {table_name} table in {database_name}.")
