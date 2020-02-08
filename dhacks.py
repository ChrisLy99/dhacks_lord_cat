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