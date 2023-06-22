# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/06_utils.ipynb.

# %% auto 0
__all__ = ['select_rows']

# %% ../nbs/06_utils.ipynb 3
import pandas as pd
import numpy as np
from typing import Tuple, Dict, Callable

# %% ../nbs/06_utils.ipynb 4
def select_rows(df:pd.DataFrame, #  DataFrame whose rows should be selected
                where:Dict[str, Callable], # Pandas columns as keys & predicates as values.
               ) -> pd.DataFrame:
    "When passed to Pandas pipe, perform row selection given multiple predicates"
    df = df.copy()
    for col, f in where.items():
        df = df[df[col].apply(f)]
    return df
