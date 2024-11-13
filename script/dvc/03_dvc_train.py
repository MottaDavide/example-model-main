
# %%
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from app.core.serializer.dataframe import DataFrameStorage
from app.core.serializer.model_storage import RandomForestClassifierStorage
from sklearn.ensemble import RandomForestClassifier
from app.tool import config
import dvc.api


# %%
logger = config.logger
logger.info("settings")
params = dvc.api.params_show()
import_file = Path(params["import"]["import_parquet"])
random_seed = 42
import_storage = DataFrameStorage(import_file)
train_file = Path(params["prepare"]["train_parquet"])
train_storage = DataFrameStorage(train_file)
valid_storage = DataFrameStorage(Path(params["prepare"]["valid_parquet"]))
test_storage = DataFrameStorage(Path(params["prepare"]["test_parquet"]))
model_fit_file = Path(params["train"]["model_fit_file"])
model_fit_storage = RandomForestClassifierStorage(model_fit_file)
model_max_depth = params["train"]["model"]["max_depth"]

# %%
logger.info("train model")

iris_train = train_storage.load()

predictor_df = iris_train.drop("target", axis=1)
target_vec = iris_train["target"]

clf = RandomForestClassifier(max_depth=model_max_depth, random_state=random_seed)
clf.fit(predictor_df, target_vec)

model_fit_file.parent.mkdir(parents=True, exist_ok=True)
model_fit_storage.save(clf)

# %%
