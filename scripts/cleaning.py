import numpy as np
# Data Cleaning Functions
def handle_missing_values(df):
    """
    Handles missing values in the dataframe.
    - Uses mean for numerical columns.
    - Uses mode for non-numerical (object) columns.

    Parameters:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: DataFrame with handled missing values
    """
    for col in df.columns:
        if df[col].dtype in [np.float64, np.int64]:  # Numerical columns
            df[col].fillna(df[col].mean(), inplace=True)
        else:  # Non-numerical columns
            df[col].fillna(df[col].mode()[0], inplace=True)
    return df


def convert_dtypes(df):
    """
    Converts data types of the dataframe for optimization.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: Optimized DataFrame
    """
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category')
    return df