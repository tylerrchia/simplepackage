import pandas as pd
import numpy as np

def subset_df(df: pd.DataFrame, column_type: type) -> pd.DataFrame:
    """
    Subsets a pandas DataFrame based on a given column data type.
    
    Parameters:
    - df: The pandas DataFrame to be subsetted.
    - column_type: The data type of the column used for subsetting.
    
    Returns:
    - The subsetted pandas DataFrame containing only columns of the specified type.
    """
    subset_cols = df.select_dtypes(include=[column_type])
    return subset_cols



def generate_random_data(num_rows: int, num_cols: int, seed: int = 123) -> pd.DataFrame:
    """
    Generates random data in a pandas DataFrame with various datatypes.
    
    Parameters:
    - num_rows: The number of rows in the DataFrame.
    - num_cols: The number of columns in the DataFrame.
    
    Returns:
    - A pandas DataFrame with random data.
    """
    data = {}
    rng = np.random.default_rng(seed=seed)
    
    # Generate random data for each column
    for i in range(num_cols):
        column_name = f'Column_{i}'
        
        # Generate random data based on datatype
        if i % 3 == 0:
            # Integer column
            data[column_name] = rng.integers(low = 0, high= 100, size=num_rows)
        elif i % 3 == 1:
            # Float column
            data[column_name] = rng.uniform(low =0.0, high = 10.0, size = num_rows)
        else:
            # String column
            data[column_name] = rng.choice(['A', 'B', 'C'], size=num_rows)
    
    df = pd.DataFrame(data)
    return df
