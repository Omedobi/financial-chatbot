import pandas as pd

def load_and_merge_datasets(file_paths):
    """
    Loads multiple datasets from file paths and appends them into one DataFrame.

    Parameters:
    file_paths (list of str): List of file paths to load datasets from.

    Returns:
    pd.DataFrame: The appended DataFrame.
    """
    
    if not file_paths:
        raise ValueError("file_paths cannot be empty.")

    # Create an empty dataframe
    merged_df = pd.DataFrame()

    # Iteratively merge the remaining datasets
    for file_path in file_paths:
        current_df = pd.read_csv(file_path)
        merged_df = pd.concat([merged_df, current_df], ignore_index=True)

    return merged_df
