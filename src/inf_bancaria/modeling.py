from sklearn.preprocessing import LabelEncoder


def encode_categorical_vars(df, columns):
    """
    Transform categorical variables to ordinary values.

    :param pandas.DataFrame df: A pandas Dataframe.
    :param lits columns: A list of categorical variables.
    :return pandas.DataFrame: A transformed Dataframe
    """

    for col in columns:
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))

    return df
