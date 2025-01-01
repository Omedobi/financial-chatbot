import pandas as pd
import numpy as np


def clean_dataset(df, rename_columns):
    """
    Cleans the dataset by renaming columns and dropping the first row.

    Parameters:
    df (pd.DataFrame): The DataFrame to clean.
    rename_columns (dict): Dictionary mapping old column names to new names.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    df.columns = df.columns.astype(str)
    
    if rename_columns:
        df = df.rename(columns=rename_columns)

    # Drop the first row 
    if 0 in df.index:
        df = df.drop(index=0)

    return df
