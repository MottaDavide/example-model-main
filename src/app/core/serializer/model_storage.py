
import pandas as pd
from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq
from typing import Union
import pickle
from sklearn.ensemble._forest import RandomForestClassifier


class RandomForestClassifierStorage:

    # using pickle to store the model
    def __init__(self, path: Union[Path, str]):
        self.path = path

    def save(self, model: RandomForestClassifier) -> None:
        with open(self.path, "wb") as f:
            pickle.dump(model, f)

    def load(self) -> RandomForestClassifier:
        with open(self.path, "rb") as f:
            return pickle.load(f)
