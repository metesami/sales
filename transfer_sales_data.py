import pandas as pd
from sqlalchemy import create_engine

csv_file = 'sales_data_cleaned.csv'
table_name = 'sales'


engine=create_engine('postgresql://{}:{}@{}/{}'.format('postgres', 'postgres', 'postgres:5432', 'postgres'))



with open(csv_file, 'r') as file:
    data_df = pd.read_csv(file)
data_df.to_sql(table_name, con=engine, index=False, if_exists='replace')
print(data_df)

engine.connect().commit()


#Extract data from Postgres 

# SQL query
sql = "SELECT * from sales"

# Execute SQL query and fetch results 
trans_df = pd.read_sql_query(sql, con=engine)
csv_filename = 'Data_for_transform.csv' # hear we put a name for the csv_file
trans_df.to_csv(csv_filename)

def process_data(absolute_path: str) -> pd.DataFrame:
    trans_df = pd.read_csv(absolute_path)
    trans_df[['TransactionID','ProductID']]=trans_df[['TransactionID','ProductID']].astype(int)
    #total profit
    trans_df['TotalProfit']=(trans_df['Quantity'] * (trans_df['SalePrice'] - trans_df['PurchasePrice'])).astype(float).round(2)
    #total profit for each product
    ProductProfit = trans_df.groupby('ProductID')['TotalProfit'].sum().astype(float).round(2)
    #The product IDs of the 2 top-selling products.
    ProductQuantity = trans_df.groupby('ProductID')['Quantity'].sum().sort_values(ascending=False).head(2)
    TransactionTotalProfit = trans_df.set_index('TransactionID')['TotalProfit'].to_dict()
    ProductTotalProfit = ProductProfit.to_dict()
    TopSellProduct = ProductQuantity.astype(int).to_list()
    ResultTuple = (TransactionTotalProfit,ProductTotalProfit,TopSellProduct)
    return ResultTuple


print(process_data('Data_for_transform.csv'))
