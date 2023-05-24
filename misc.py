from typing import List
import pandas as pd

def check_string_in_list(string: str, string_list: List[str]) -> bool:
  """
  Check if a string is present in a list of strings and raise an error if not found.
  
  Args:
      string (str): The string to check.
      string_list (list): The list of strings to search in.
      
  Raises:
      ValueError: If the string is not found in the list.
  
  Returns:
      bool: True if string is in string_list
  """
  if string not in string_list:
      raise ValueError(f"The string '{string}' is not in the list.")
  else:
      return True



def calculate_five_number_summary(df: pd.DataFrame) -> dict:
    """
    Calculates the five number summary (minimum, 1st quartile, median, 3rd quartile, maximum)
    for numerical columns in a pandas DataFrame.
    
    Parameters:
    - df: A pandas DataFrame.
    
    Returns:
    - A dictionary containing the five number summary for each numerical column.
    """
    summary = {}
    
    # Iterate over each column in the DataFrame
    for column_name in df.columns:
        column = df[column_name]
        
        # Calculate the five number summary for the numerical column
        if pd.api.types.is_numeric_dtype(column):
            minimum = column.min()
            q1 = column.quantile(0.25)
            median = column.median()
            q3 = column.quantile(0.75)
            maximum = column.max()
            
            # Store the five number summary in the dictionary
            summary[column_name] = {
                'Minimum': minimum,
                '1st Quartile': q1,
                'Median': median,
                '3rd Quartile': q3,
                'Maximum': maximum
            }
    
    return summary


def calculate_proportions(df: pd.DataFrame, column: str) -> pd.Series:
    """
    Calculates the proportion of each unique level from a categorical variable in pandas DataFrame.
    
    Parameters:
    - data: pandas DataFrame containing the data.
    - column: Name of the column representing the categorical variable.
    
    Returns:
    - pandas Series containing the proportions of each unique level.
    """
    # Calculate the count of each unique level
    counts = df[column].value_counts()
    
    # Calculate the proportion of each unique level
    proportions = counts / counts.sum()
    
    return proportions