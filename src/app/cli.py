from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from app.core.serializer.dataframe import DataFrameStorage
from app.core.serializer.model_storage import RandomForestClassifierStorage
from app.core.serializer.yaml_storage import YamlStorage
from sklearn.ensemble import RandomForestClassifier
import typer


app = typer.Typer()


@app.command()
def train(
    train_file: Path = typer.Option("", help="The Path to the train file"),
    valid_file: Path = typer.Option("", help="The Path to the valid file"),
    model_fit_file: Path = typer.Option(..., help="The Path to the model fit file"),
    param_file: Path = typer.Option(..., help="The Path to the yaml storage"),
) -> None:
    train_storage = DataFrameStorage(train_file)
    valid_storage = DataFrameStorage(valid_file)

    param_storage = YamlStorage(param_file)
    params = param_storage.load()
    seed = params["train"]["seed"]
    model_params = params["train"]["model"]

    model_fit_storage = RandomForestClassifierStorage(model_fit_file)

    iris_train = train_storage.load()

    predictor_df = iris_train.drop("target", axis=1)
    target_vec = iris_train["target"]

    clf = RandomForestClassifier(max_depth=model_params["max_depth"], random_state=seed)
    clf.fit(predictor_df, target_vec)

    model_fit_file.parent.mkdir(parents=True, exist_ok=True)
    model_fit_storage.save(clf)


if __name__ == "__main__":
    app()
