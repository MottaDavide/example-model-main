# %%
from pathlib import Path
from sklearn import datasets
import pandas as pd
import pyarrow as pa
# import pyarrow.parquet as pq
from app.core.config import config

# Settings
logger = config.logger
logger.info("settings")
import_storage = config.params.import_storage

# %%
logger.info("importing data")
#
# This could come from reading data from a database, 
# or from a data/00_raw
iris = datasets.load_iris()
X = iris.data
y = iris.target

# gather data into a dataframe
iris_df = pd.DataFrame(X, columns=iris.feature_names).assign(target=y)
import_storage.save(iris_df)

# %%
