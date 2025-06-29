import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="israelaidoo",
    password="Kobbie@2025.",
    database="PROJECT_TUTORIAL"
)

# Create a cursor to interact with the database
cursor = connection.cursor()

# Example query to fetch data
cursor.execute("SELECT * FROM your_table_name")
result = cursor.fetchall()

# Print the results
for row in result:
    print(row)

# Close the connection
cursor.close()
connection.close()

import pandas as pd

# Read Excel file
df = pd.read_excel('/mnt/c/Users/Kobbie/Desktop/yourfile.xlsx')

# Print the data
print(df.head())

df.to_excel('/mnt/c/Users/Kobbie/Desktop/output.xlsx', index=False)

