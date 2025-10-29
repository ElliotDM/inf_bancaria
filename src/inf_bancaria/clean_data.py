def remove_columns(df, columns):
    """
    Processes the data frame removing 
    unnecessary columns for the project.

    :param pd.DataFrame df: A pandas dataframe.
    :param list columns: A list of columns names intended to be removed
    :returns df: A modified dataframe.
    """
    return df.drop(columns, axis=1)
