import mysql.connector  # type: ignore
import pandas as pd

db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Dev@n$h!@28",
        database="capstone"
    )
   

# Function to fetch data from MySQL
def handle_sql_queries(query):
    data = pd.read_sql(query, db)
    db.close()
    return data