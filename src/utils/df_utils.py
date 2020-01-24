import pandas as pd
import os
import sys

CURR_DIR = os.path.dirname(os.path.realpath("__file__"))
ROOT_DIR = os.path.abspath(os.path.join(CURR_DIR, '..'))

def save_df(df, filename, sub_dir=None):
    """Saves df to data dir as csv

    Meant to be used with cookiecutter layout
    """

    data_dir = os.path.join(ROOT_DIR, 'data')
    if sub_dir:
        data_dir = os.path.join(data_dir, sub_dir)
    df.to_csv(os.path.join(data_dir, filename), )
    print(f"df successfully saved | filename: {filename}, dir: {data_dir}")

def load_df(file_path):
    """loads df from dat dir

    Meant to be used with cookiecutter layout
    """
    file_path = os.path.join(ROOT_DIR, "data", file_path)
    df = pd.read_csv(file_path)
    return df
