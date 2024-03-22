import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

# Connect to your PostgreSQL database
conn = psycopg2.connect(host='localhost', dbname='test', user='root', password='root')
cur = conn.cursor()

# Define the file path of the CSV file
csv_file_path = os.path.join(os.getcwd(), "fashion_products.csv")
df = pd.read_csv(csv_file_path)
table_name = "fashion_product"


def create_table(cursor, df, table_name):
    """
    Create a table in PostgreSQL based on DataFrame columns.
    """
    # Define the SQL query to create the table
    columns = ", ".join(f'"{col}" VARCHAR' for col in df.columns)
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
    
    # Execute the create table query
    cursor.execute(create_table_query)

def import_data(cursor, df, table_name):
    """
    Import data from DataFrame into PostgreSQL table.
    """
    # Generate the INSERT INTO query
    columns = ", ".join(f'"{col}"' for col in df.columns)
    placeholders = ", ".join("%s" for _ in df.columns)
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
     
    # Insert data row by row
    for _, row in df.iterrows():
        cursor.execute(insert_query, row)


# Create the table & Import data into the table
create_table(cur, df, table_name)
import_data(cur, df, table_name)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Data inserted successfully into the 'fashion_product' table.")
