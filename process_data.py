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