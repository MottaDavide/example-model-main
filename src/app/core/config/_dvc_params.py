from typing import Any, Dict, Optional
from pathlib import Path
import dvc.api
from app.core.serializer.dataframe import DataFrameStorage
from app.core.serializer.json_storage import JsonStorage
from app.core.serializer.model_storage import RandomForestClassifierStorage


class Params:
    """Class that reads the params.yaml file of DVC."""

    def __init__(self, dvc_params_yaml: Path) -> None:
        self.dvc_params_yaml = dvc_params_yaml
        self.params = dvc.api.params_show()
        # import stage
        self.import_storage = DataFrameStorage(Path(self.params["import"]["iris_parquet"]))
        # prepare stage
        self.prepare_random_seed = int(self.params["prepare"]["seed"])
        self.train_storage = DataFrameStorage(Path(self.params["prepare"]["train_parquet"]))
        self.valid_storage = DataFrameStorage(Path(self.params["prepare"]["valid_parquet"]))
        self.test_storage = DataFrameStorage(Path(self.params["prepare"]["test_parquet"]))
        # train stage
        self.model_fit_storage = RandomForestClassifierStorage(Path(self.params["train"]["model_fit_file"]))
        # predict stage
        self.pred_storage = DataFrameStorage(Path(self.params["predict"]["pred_parquet"]))
        # dvc general
        self.metric_storage = JsonStorage(Path("evaluation") / "metrics.json")

    def params_show(self, *args, **kwargs) -> Dict[str, Any]:  # type: ignore
        """Wrap of dvc.api.params_show()"""
        params = dvc.api.params_show(*args, **kwargs, repo=str(self.dvc_params_yaml))
        return params
