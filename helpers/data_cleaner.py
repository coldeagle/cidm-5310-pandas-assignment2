import pandas

VALID_VAR_TYPES = ['int', 'bool', 'str', 'datetime', 'date', 'float', 'category']
MATH_TYPES = ['float', 'float64', 'int', 'int64']


# This function will fill blank values and format the columns
def fill_blanks_and_format(df: pandas.DataFrame):
    if df is None:
        raise Exception('The dataframe passed was None!')
    
    for col in df:
        df_col = df[col]
        dt = df_col.dtype

        if dt in MATH_TYPES:
            df_col.fillna(round(df_col.mean()), inplace=True)
            convert_data_type(df=df, column_name=col, var_type='int')
        else:
            df_col.fillna('No Info', inplace=True)
            convert_data_type(df=df, column_name=col, var_type='category')


# This function will convert the data type for a column in the data frame
def convert_data_type(df: pandas.DataFrame, column_name: str, var_type: str):
    if df is None:
        raise Exception('The dataframe passed was None!')
    elif var_type is None or str(var_type).lower() not in VALID_VAR_TYPES:
        var_type = 'None' if var_type is None else var_type
        raise Exception(f'Please pass a valid var type! {var_type} is not valid a valid option!')
    else:
        df[column_name] = df[column_name].astype(var_type)
    
