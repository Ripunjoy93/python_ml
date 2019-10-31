# coding: utf-8
# !/usr/bin/env python3
import os
import pandas as pd

__doc__ = """
General Helper Functions
"""
__author__ = "Ripunjoy Gohain"
__copyright__ = "Ripunjoy Gohain"
__credits__ = []
__maintainer__ = "ripunjoygohain79@gmail.com"
__email__ = "ripunjoygohain79@gmail.com"
__status__ = "Development"
__date__ = ""


def get_col_dtype(col):
    """
    Infer datatype of a pandas column, process only if the column dtype is object.
    input:   col: a pandas Series representing a df column.
    """
    if col.dtype == "object":
        try:
            col_new = pd.to_numeric(col.dropna().unique())
            return col_new.dtype
        except:
            return "object"
    else:
        return col.dtype


def data_frame_object_column_to_numeric(data_frame):
    """
    Convert object column to numeric is possible
    """
    data_frame = data_frame.copy()
    obj_cols = list(data_frame.select_dtypes(include="object").columns)
    for col in obj_cols:
        try:
            data_frame[col] = data_frame[col].astype(get_col_dtype(data_frame[col]))
        except Exception as e:
            print("Column: {} got Exception as: {}".format(col, e))
    return data_frame


def get_parent_path():
    """
    Helper function to maintain path structure
    It helps because it give the path of current file location only when it is called from another location
    """
    path = os.path.abspath(__file__ + "/../../")
    return path
