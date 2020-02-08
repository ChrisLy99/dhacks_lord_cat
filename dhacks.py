"""
Authors: Cat
Date: 2020.02.08
Github: https://github.com/ChrisLy99/dhacks_lord_cat
"""

import numpy as np
import pandas as pd

def read_csv(fn):
    out = pd.read_csv(f"data/{fn}.csv")
    return out

def read_data():
    ds1 = read_csv('barts_hotspots')
    ds2 = read_csv('barts_to_all')
    ds3 = read_csv('hotspots_to_all')
    ds4 = read_csv('hours_q1')
    ds5 = read_csv('hours_q2')
    return [ds1, ds2, ds3, ds4, ds5]