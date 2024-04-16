1- I cleaned data in jupyter notebook and after that bring the data in our project folder for loading in postgres with docker 
2- we have 3 container overall
3- the python script for load data in postgres is fisrt part of 'transfer_sales_data_.py' and the fucntion of 'process_data' is in the same file.
    
    3.1- actually in our python container we load data at database after that extract it and use 'process_data' function for do some transformation

4- we have 'Dockerfile' for image of python container  

5- i dont concider any Constraint for my table and hold it simple.