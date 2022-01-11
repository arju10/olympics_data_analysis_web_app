import pandas as pd

def preprocess(df, region_df):
    # global df, region_df
    # filtering for summer season olympics
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    # By merging df & region_df based on NOC . We can find out the Region of NOC.
    df = df.merge(region_df, on='NOC', how='left')  # here NOC is common column
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # Apply One Hot Encoding on Medal
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df



