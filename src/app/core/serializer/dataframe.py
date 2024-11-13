
import pandas as pd
from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq
from typing import Union


class DataFrameStorage:

    def __init__(self, path: Union[Path, str]):
        if isinstance(path, str):
            path = Path(path)
        self.path: Path = path

    def save(self, df: pd.DataFrame) -> None:
        # cast data into pyarrow table
        iris_table: pa.Table = pa.Table.from_pandas(df)
        # create the parent directory if it does not exist
        self.path.parent.mkdir(parents=True, exist_ok=True)
        # Write a table to a dataset directory
        pq.write_table(iris_table, str(self.path))

    def load(self) -> pd.DataFrame:
        return pq.read_pandas(str(self.path)).to_pandas()


