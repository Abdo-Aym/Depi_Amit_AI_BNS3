# File 2
import pandas as pd
# import numpy as np
import warnings
warnings.filterwarnings('ignore')

def chk_dtype(df):
    dtypes = df.dtypes
    n_unique = df.nunique()
    return pd.DataFrame({"Dtypes":dtypes, "Num_uniques":n_unique}).T



def change2cat(df):
    cols = df.columns
    dtypes = df.dtypes
    n_unique = df.nunique()
    for col in cols:
        if df[col].nunique() < 10:
            df[col] = df[col].astype("category")
    dtypes = df.dtypes
    n_unique = df.nunique()
    return pd.DataFrame({"Dtypes":dtypes, "Num_uniques":n_unique}).T


#### Check_nulls
def chk_nulls(df):
    null = df.isnull().sum()
    ratio = round((null/df.shape[0])*100,2)
    return pd.DataFrame({"Null_sum":null,"Ratio %": ratio}).T




#### Change_nulls
def change_nulls(df):
    cols = df.columns
    null = df.isnull().sum()
    ratio = round((null/df.shape[0])*100,2)
    for col in cols:
        if ratio[col] > 0:
            if ratio[col] > 50:
                df.drop(col, axis=1, inplace= True)
                print(f"dropped column: {col}")
            else:
                mode =  df[col].mode()
                df[col].fillna(mode[0], inplace= True)
                print(f"filled {col} nulls with mode")
    null = df.isnull().sum()
    ratio = round((null/df.shape[0])*100,2)
        
    return pd.DataFrame({"Null_sum":null,"Ratio %": ratio}).T