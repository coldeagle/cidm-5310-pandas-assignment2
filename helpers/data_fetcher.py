import sqlite3
import pandas as pd

# Setting up the DB cursor
db_path = '../data/supply_company.db'
cursor = sqlite3.connect(db_path)

# Setting up the car data frame
car_data_path = '../data/car.csv'
car_data = pd.read_csv(car_data_path)


# This function will get all tables from the DB
def get_tables():
    tableQ = "SELECT name FROM sqlite_master WHERE type = 'table'"
    return pd.read_sql(tableQ, cursor)


# This function will get all orders from the DB
def get_orders():
    ordersQ = "SELECT * FROM Orders"
    return pd.read_sql(ordersQ, cursor)


# This method will get the customer record based on the customer number
def get_customer(customer_num):
    if customer_num is None:
        raise Exception('A customer number is required!')

    custQ = 'SELECT * FROM Customers WHERE Customer_Number = ' + customer_num

    return pd.read_sql(custQ, cursor)


# This function will get all unique values from the data frame
def get_num_all_unique_vals(df: pd.DataFrame):
    if df is None:
        raise Exception('The dataframe passed was None!')
    for col in df:
        print(f'{col}: {get_num_unique_column(df=df, col_name=col)}')


# This function will get the number of unique values in a specific column
def get_num_unique_column(df: pd.DataFrame, col_name: str):
    if df is None:
        raise Exception('The dataframe passed was None!')
    if col_name is None:
        raise  Exception('A column name must be passed!')
    if df[col_name] is None:
        raise Exception(f'The column {col_name} does not exist in the dataframe!')

    return df[col_name].nunique()