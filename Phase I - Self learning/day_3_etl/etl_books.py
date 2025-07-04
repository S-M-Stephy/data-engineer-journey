import pandas as pd
import sqlite3

# Extract 
df = pd.read_csv('D:/Stephy/data-engineer-journey/day_3_etl/book.csv') 
print(df.head())

# Transform
df.columns = df.columns.str.strip()  # Clean column names

# Load to SQLite database
conn = sqlite3.connect('books.db')
df.to_sql("books", conn, if_exists='replace')

# Verify the data in the SQLite database
query = "SELECT * FROM books LIMIT 5;"
df_loaded = pd.read_sql_query(query, conn)
print(df_loaded)

# Close the database connection
conn.close()

