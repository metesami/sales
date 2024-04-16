import psycopg2

# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
conn.autocommit = True
cursor = conn.cursor()

# Import data from the CSV file
csv_file_path = 'C:/Users/Dear User classic/Downloads/Compressed/K24-Data-Engineering-Challenge/sales_data_cleaned.csv'
import_csv_sql = f'''
    COPY oltp.Sales(TransactionID, ProductID, Quantity, SalePrice, PurchasePrice)
    FROM '{csv_file_path}'
    DELIMITER ','
    CSV HEADER;
'''
cursor.execute(import_csv_sql)

# Query the table to verify the data
select_sql = "SELECT * FROM oltp.Sales;"
cursor.execute(select_sql)
for row in cursor.fetchall():
    print(row)

# Clean up
conn.commit()
conn.close()
