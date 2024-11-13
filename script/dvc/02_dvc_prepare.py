# %%
from pathlib import Path
from sklearn.model_selection import train_test_split
from app.core.config import config

# Settings
logger = config.logger
logger.info("settings")


# %%
logger.info("load import data")
iris_df = config.params.import_storage.load()
import numpy as np
iris_df.target =np.where(iris_df["target"]==2, 0, iris_df["target"])

iris_train_valid, iris_test = train_test_split(
    iris_df, test_size=0.50, random_state=config.params.prepare_random_seed
)
iris_train, iris_valid = train_test_split(
    iris_train_valid, test_size=0.20, random_state=config.params.prepare_random_seed
)


# %%
logger.info("save prepared data")
config.params.train_storage.save(iris_train)
config.params.valid_storage.save(iris_valid)
config.params.test_storage.save(iris_test)

# %%
