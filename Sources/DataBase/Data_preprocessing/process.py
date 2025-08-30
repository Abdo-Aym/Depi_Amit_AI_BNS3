import pandas as pd
def chk_types(df):
    """
    This method takes df and returns the dtypes and number of unique values
    par_1 : df
    type_par_1 : dataframe

    return: data
    """
    dtypes = df.dtypes
    n_unique = df.nunique()
    return pd.DataFrame({"Dtypes":dtypes, "Num_uniques":n_unique}).T