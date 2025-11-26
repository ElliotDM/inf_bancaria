def remove_variables(df, columns):
    """
    Processes the data frame removing 
    unnecessary columns for the project.

    :param df: A pandas dataframe.
    :type df: pandas.DataFrame
    :param columns: A list of columns to be removed.
    :type columns: list
    :return: A transformed dataframe
    :rtype: pandas.DataFrame 
    """

    return df.drop(columns, axis=1)


def remove_percent(data: str) -> str:
    """
    Checks whether a string contains 
    the percent sign (%) and removes it; 
    otherwise, returns the same string.
    
    :param data: Some data to be processed.
    :type data: str
    :return: Processed data.
    :rtype: str
    """
    
    if "%" in data:
        return data.replace("%", "")
    return data


def normalize_percentage(data: float) -> float:
    """
    Divides one value by 100.
    
    :param data: Some data to be processed.
    :type data: float
    :return: Processed data.
    :rtype: float
    """
    
    return data/100
