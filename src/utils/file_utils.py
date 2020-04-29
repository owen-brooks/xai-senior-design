import pandas as pd
import os
import sys

import tensorflow as tf

CURR_DIR = os.path.dirname(os.path.realpath("__file__"))
ROOT_DIR = os.path.abspath(os.path.join(CURR_DIR, ".."))


def save_df(df, filename, sub_dir=None, withIndex=False):
    """Saves df to data dir as csv"""
    data_dir = os.path.join(ROOT_DIR, "data")
    if sub_dir:
        data_dir = os.path.join(data_dir, sub_dir)
    df.to_csv(os.path.join(data_dir, filename), index=withIndex)
    print(f"df successfully saved | filename: {filename}, dir: {data_dir}")    

def load_df(file_path, indexCol=None):
    """loads df from data dir"""
    file_path = os.path.join(ROOT_DIR, "data", file_path)
    df = pd.read_csv(file_path, index_col=indexCol)
    return df


def save_model(model, filename):
    """Saves model to model dir"""
    file_path = os.path.join(ROOT_DIR, "models", filename)
    model.save(file_path)
    print(f"model successfully saved | file_location: {file_path}")


def load_model(filename):
    """Saves model to model dir"""
    file_path = os.path.join(ROOT_DIR, "models", filename)
    model = tf.keras.models.load_model(file_path, custom_objects=None, compile=True)
    print(f"Model successfully loaded | file_location: {file_path}")
    return model
