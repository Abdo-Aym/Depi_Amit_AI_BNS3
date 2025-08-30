import pandas as pd
def null_ratio(df):
    null = df.isnull().sum()
    ratio = (null/df.shape[0])*100
    return pd.DataFrame({"Null_sum":null,"Ratio %": ratio}).T