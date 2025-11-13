def remove_variables(df, columns):
    """
    Processes the data frame removing 
    unnecessary columns for the project.

    :param pandas.DataFrame df: A pandas dataframe.
    :param list columns: A list of columns to be removed.
    :return pandas.DataFrame: A transformed dataframe
    """
    
    return df.drop(columns, axis=1)
