 %%
from pathlib import Path
from app.core.serializer.dataframe import DataFrameStorage
from app.core.serializer.model_storage import RandomForestClassifierStorage


# %%
# Settings
test_storage = DataFrameStorage(Path("data/02_prepare/test.parquet"))
model_fit_file = Path("./model_fit.pkl")
model_fit_storage = RandomForestClassifierStorage(model_fit_file)

# %%
clf = model_fit_storage.load()
iris_test = test_storage.load()

predictor_df = iris_test.drop("target", axis=1)

clf.predict(predictor_df)

