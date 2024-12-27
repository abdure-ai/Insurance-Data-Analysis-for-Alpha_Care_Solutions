# Data Summarization Functions
def summarize_data(df):
    """
    Summarizes the dataset by providing descriptive statistics.

    Parameters:
        df (pd.DataFrame): Input DataFrame
    
    Returns:
        dict: Summary statistics
    """
    return {
        "shape": df.shape,
        "info": df.info(),
        "description": df.describe().transpose()
    }